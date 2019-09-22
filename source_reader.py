from tigr import AbstractSourceReader


class SourceReader(AbstractSourceReader):
    def __init__(self, parser, optional_file_name=None):
        super().__init__(parser, optional_file_name)

    def go(self):
        with open(self.file_name) as file:
            for line in file.readlines():
                self.source.append(line)

        self.parser.parse(self.source)
