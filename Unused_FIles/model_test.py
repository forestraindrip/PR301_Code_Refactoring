import unittest


class ModelTest(unittest.TestCase):

    def test(self):
        from drawer_kieran import DrawerKieran
        from parser_dang import ParserDang
        to_draw = open('test.txt', "r+").read()
        parser = ParserDang(DrawerKieran())
        s = parser.parse(to_draw)
        self.assertEqual(s, 'pen down')


if __name__ == '__main__':
    unittest.main()
