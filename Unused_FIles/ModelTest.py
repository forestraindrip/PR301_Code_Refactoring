import unittest


class ModelTest(unittest.TestCase):

    def test(self):
        from DrawerKieran import Drawer
        from ParserDang import Parser
        to_draw = open('test.txt', "r+").read()
        parser = Parser(Drawer())
        s = parser.parse(to_draw)
        self.assertEqual(s, 'pen down')


if __name__ == '__main__':
    unittest.main()
