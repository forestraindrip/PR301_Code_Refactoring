import unittest


class ModelTest(unittest.TestCase):

    def test(self):
        from drawer_kieran import Drawer
        from parser_dang import Parser
        to_draw = open('test.txt', "r+").read()
        parser = Parser(Drawer())
        s = parser.parse(to_draw)
        self.assertEqual(s, 'pen down')


if __name__ == '__main__':
    unittest.main()
