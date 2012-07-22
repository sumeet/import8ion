from expecter import expect

from import8ion import ExtractsImports
from import8ion import Import



unorganized_imports = """\
import datetime, mock
from decimal import Decimal
from myproj import something
from decimal import getcontext
import import8ion
import os
import os.path
"""


organized_imports = """\
import datetime
from decimal import Decimal
from decimal import getcontext
import os
import os.path

import mock

import import8ion
from myproj import something
"""


#class AcceptanceTest(object):

#    def test_organizes_imports(self):
#        expect(organize(unorganized_imports)) == organized_imports


class ExtractsImportsTest(object):

    def test_finds_imports(self):
        imports = ExtractsImports.extract('import name\n'
                                          'from module import name')
        expect(imports) == [Import('name', None), Import('module', 'name')]
