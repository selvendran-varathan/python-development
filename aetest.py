'Test packages'

import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Testcase:
    pass
class Setup:
    pass
class Cleanup:
    pass

def run_test(testcase):
    testclass = testcase.__class__
    for attrname in dir(testclass):
        test = getattr(testclass,attrname)
        if getattr(test, 'test', False):
            LOGGER.info('Running tests')
            try:
                test(testcase)
            except AssertionError:
                LOGGER.exception('Failed teststep: %r ' % test.__name__)
            else:
                LOGGER.info('Success teststep: %r' % test.__name__)

