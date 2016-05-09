# ats.tcl.KeyedList

from attrdict import AttrDict
from collections import MutableMapping

class KeyedList(AttrDict, MutableMapping):
    '''
    KeyedList Class (AttrDict)

    This class mimics the Tcl Keyed List variable behavior, allowing users to
    save a Tcl Keyed List in Python, and use it throughout the rest of their
    codes.

    This class extends the AttrDict class.

    Many operations with KeyedList classes are recursive, made to correspond to
    how the Tcl KeyedList behaves.

    Keyed List behaviors:
        - keyed lists are basically key-value pairs (similar to dict in Python)
        - keys could have sub-keys, and sub-keys could be values, or another
          keyed list
        - keys and subkeys are identifed/separated by a "."

    Special Notes:
        - KeyedList extends AttrDict, which extends (based on) dict()
        - Accessing keys and subkeys can be achieved by var['key.subkey'] etc
        - subkeys that are keyed lists are also a KeyedList object
            - thus access to their values from top level is done recursively

    Examples:
        >>> klist = KeyedList()
        >>> klist['name.first'] = 'Garrosh'
        >>> klist['name.last']  = 'Hellscream'
        >>> klist['boss.number'] = '14'
        >>> klist['boss.instance'] = 'Siege of Orgrimmar'
        >>> klist['boss.location'] = 'The Inner Sanctum'
        >>> klist.keys()
        ['name', 'boss']
        >>> klist.boss.location
        'The Inner Sanctum'
    '''
    def __init__(self, *args, **kwargs):
        '''KeyedList init (built-in)

        This API initializes the KeyedList instance object. It first creates
        the top level key/value pairs, then iterate through each child
        key-value to instanciate them as keyed-lists

        Arguments:
            *args: supports creating keyed lists from keyed tuples (pairs of
                   two, with first being key name and 2nd being value)
            **kwargs: supports creating keyed lists from dict style keyword
                      arguments.

        Returns:
            initialized new KeyedList object.

        Examples:
            klist = KeyedList((('name', (('last', 'schwarzenegger'),
                                        ('first', 'arnold'))), ))
            klist = KeyedList({'name' : {'last': 'schwarzenegger',
                                         'first': 'arnold'}, })
            klist = KeyedList('{name {{last schwarzenegger} {first arnold}}}')
        '''

        super(KeyedList, self).__init__()
        dsc = dict(*args, **kwargs)
        for key, value in dsc.items():
            if not isinstance(value, KeyedList):
                try:
                    dsc[key] = KeyedList(value)
                except (ValueError, TypeError):
                    pass
        self.update(dsc)

    def __getitem__(self, key):
        '''KeyedList __getitem__ (built_in)

        This API enables the recursive get operations through []
        Arguments:
            key (str): key to read, separated by '.' when needed

        >>> klist['name.last']
        'schwarzenegger'

        '''
        if '.' in key:
            key, subkeys = key.split('.', 1)
            return super(KeyedList, self).__getitem__(key)[subkeys]
        else:
            return super(KeyedList, self).__getitem__(key)

    def __setitem__(self, key, value):
        '''KeyedList __setitem__ (built_in)

        This API enables the recursive set operations through []
        Arguments:
            key (str): key to set, separated by '.' when needed

        >>> klist['name.last'] = 'schwarzenegger'

        '''

        if '.' in key:
            key, subkeys = key.split('.', 1)

            try:
                subkl = self[key]
            except KeyError:
                subkl = KeyedList()
                super(KeyedList, self).__setitem__(key, subkl)
            else:
                if not isinstance(subkl, KeyedList):
                    raise KeyError('target key "%s" is a value, cannot update '
                            'value against another keyed list' % (key,))

            subkl[subkeys] = value

        else:
            if isinstance(value, KeyedList):
                try:
                    subkl = self[key]
                except KeyError:
                    pass
                else:
                    if not isinstance(subkl, KeyedList):
                        raise KeyError('target key "%s" is a value, cannot '
                                'update value against another keyed list' %
                                (key,))

            super(KeyedList, self).__setitem__(key, value)

    def __contains__(self, key):
        '''KeyedList __contains__ (built_in)

        This API enables the python in operator
        Arguments:
            key (str): key to check for, separated by '.' when needed

            >>> 'name.last' in klist
            True

        '''
        if '.' in key:
            key, subkeys = key.split('.', 1)

            if super(KeyedList, self).__contains__(key):
                subkl = super(KeyedList, self).__getitem__(key)
                return subkl.__contains__(subkeys)
            else:
                return False
        else:
            return super(KeyedList, self).__contains__(key)

    def __delitem__(self, key):
        '''KeyedList __delitem__ (built_in)

        This API enables the python del call
        Arguments:
            key (str): key to delete, separated by '.' when needed

        Examples:
            >>> del klist['name.last']
            True

        '''
        if '.' in key:
            key, subkeys = key.split('.', 1)

            del super(KeyedList, self).__getitem__(key)[subkeys]

            if not super(KeyedList, self).__getitem__(key):
                super(KeyedList, self).__delitem__(key)
        else:
            super(KeyedList, self).__delitem__(key)

    get = MutableMapping.get
    pop = MutableMapping.pop
    setdefault = MutableMapping.setdefault

    def update(self, *args, **kwargs):

        if len(args) > 1:
            raise TypeError("update() takes at most 1 positional "
                            "arguments ({} given)".format(len(args)))
        if len(args) >= 1:
            other = args[0]
            if isinstance(other, KeyedList):
                # Merge
                for key, value in other.all_items():
                    self[key] = value
            else:
                MutableMapping.update(self, other)

        for key, value in kwargs.items():
            if isinstance(value, KeyedList):
                try:
                    subkl = self[key]
                except KeyError:
                    subkl = KeyedList()
                    self[key] = subkl
                else:
                    if not isinstance(subkl, KeyedList):
                        raise KeyError('target key "%s" is a value, cannot '
                                'update value against another keyed list' %
                                (key,))
                subkl.update(value)
            else:
                self[key] = value

    def all_keys(self):
        '''KeyedList all_keys

        This API returns all keys (including subkeys) in this KeyedList. This
        operation is recursive: all fully qualified keys will be returned.

        >>> klist.all_keys()
        ['name.last', 'name.first']

        '''
        ret = []

        for key, value in self.items():
            if isinstance(value, KeyedList):
                for subkey in value.all_keys():
                    ret.append(key + '.' + subkey)
            else:
                ret.append(key)

        return ret

    def all_items(self):
        '''KeyedList all_items

        This API returns all key-value pairs (including subkeys) in this
        KeyedList. This operation is recursive: all fully qualified keys will
        be returned.

        >>> klist.all_items()
        [('name.last', 'Hellscream'), ('name.first', 'Garrosh')]


        '''
        ret = []

        for key, value in self.items():
            if isinstance(value, KeyedList):
                for subkey, subvalue in value.all_items():
                    ret.append((key + '.' + subkey, subvalue))
            else:
                ret.append((key, value))

        return ret

    has_key = __contains__


