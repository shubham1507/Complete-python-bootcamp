import re

from parser import Parser


# TODO 4 - Create UK parser class which inherits from Parser class
class UKParser(Parser):
    def __init__(self, text):
        super().__init__(text=text)

    def phone(self):
        match = re.search(r'(\+\d{1}-\d{3}-\d{3}-\d{4})', self.text)
        if match:
            return match.group(0)
        return None
