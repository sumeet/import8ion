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


class AcceptanceTest(object):

    def test_organizes_imports(self):
        expect(organize(unorganized_imports)) == organized_imports


class ExtractsImportsTest(object):

    def test_finds_imports(self):
        imports = ExtractsImports.extract('import name\n'
                                          'from module import name')
        expect(imports) == [Import('name', None), Import('module', 'name')]


class WritesImportsTest(object):

    def test_writes_imports(self):
        imports = [make_import('b'), make_import('a', 'name')]
        expect(WritesImports.write(imports)) == 'import b\nfrom a import name'


class AlphabetizesImportsTest(object):

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
