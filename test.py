from expecter import expect

from import8ion import organize



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
