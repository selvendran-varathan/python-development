'Implement attribute dictionary datatype'

d = dict(tom='red',jenny='yellow')

class AttrDict(dict):
    ''' A trick to replace the instance dictionary with an inherited dict

 
    



'''

    def __init__(self):
        self.__dict__=self


d = AttrDict()
d['tom'] = 'red' # getitem
d['jenny'] = 'blue'
d.susan = 'yellow'
d.peter = 'purple' #getattribute



