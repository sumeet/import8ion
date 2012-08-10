import unittest

from expecter import expect

from import8ion import AlphabetizesImports
from import8ion import ExtractsImports
from import8ion import Import
from import8ion import WritesImports
from import8ion import make_import
from import8ion import organize


unorganized_imports = """\
import datetime, mock
from decimal import Decimal
import datetime
from myproj import something
from decimal import getcontext
import import8ion
import os
import os.path"""


organized_imports = """\
import datetime
from decimal import Decimal
from decimal import getcontext
import import8ion
import mock
from myproj import something
import os
import os.path"""


class AcceptanceTest(unittest.TestCase):

    def test_organizes_imports(self):
        expect(organize(unorganized_imports)) == organized_imports


class ExtractsImportsTest(unittest.TestCase):

    def test_finds_imports(self):
        imports = ExtractsImports.extract('import name\n'
                                          'from module import name')
        expect(imports) == [make_import('name', None),
                            make_import('module', 'name')]

    def test_extracts_module_as_imports(self):
        imports = ExtractsImports.extract('import name as other_name')
        expect(imports) == [make_import('name', None, 'other_name')]

    def test_extracts_from_as_imports(self):
        imports = ExtractsImports.extract('from mod import name as other_name')
        expect(imports) == [make_import('mod', 'name', 'other_name')]


class WritesImportsTest(unittest.TestCase):

    def test_writes_imports(self):
        imports = [make_import('b'), make_import('a', 'name')]
        expect(WritesImports.write(imports)) == 'import b\nfrom a import name'

    def test_writes_imports_with_as_names(self):
        imports = [make_import('module', asname='asmodule'),
                   make_import('module', 'name', 'asname')]
        expected = ('import module as asmodule\n'
                    'from module import name as asname')
        expect(WritesImports.write(imports)) == expected


class AlphabetizesImportsTest(unittest.TestCase):

    def test_uppercase_comes_before_lowercase(self):
        imports = [make_import('b'), make_import('a'), make_import('C')]
        expect(AlphabetizesImports.alphabetize(imports)) == [make_import('C'),
                                                             make_import('a'),
                                                             make_import('b')]

    def test_periods_come_before_after_letters(self):
        imports = [make_import('ab'), make_import('a.c'), make_import('a.b')]
        expect(AlphabetizesImports.alphabetize(imports)) == [make_import('a.b'),
                                                             make_import('a.c'),
                                                             make_import('ab')]

    def test_periods_come_before_underscores(self):
        imports = [make_import('a.b'), make_import('a_b')]
        expect(AlphabetizesImports.alphabetize(imports)) == [make_import('a.b'),
                                                             make_import('a_b')]


if __name__ == '__main__':
    unittest.main()
