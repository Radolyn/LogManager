import os
import unittest
import LogManager

if os.path.exists(LogManager.FILE_NAME):
    os.remove(LogManager.FILE_NAME)


class TestLogging(unittest.TestCase):
    def test_print(self):
        LogManager.debug('haha')
        LogManager.info('haha')
        LogManager.warning('haha')
        LogManager.error('haha')

        f = open(LogManager.FILE_NAME, 'r')
        length = os.fstat(f.fileno()).st_size
        self.assertGreaterEqual(length, 10)
        f.close()


if __name__ == '__main__':
    unittest.main()
