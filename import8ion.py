import ast
from collections import namedtuple
import itertools


Import = namedtuple('Import', 'module name')

def make_import(module, name=None):
    return Import(module, name)


class ExtractsImports(object):

    @classmethod
    def extract(cls, source):
        tree = ast.parse(source)
        return list(itertools.chain(*map(cls._make_imports, ast.walk(tree))))

    @classmethod
    def _make_imports(cls, node):
        if isinstance(node, ast.Import):
            for name in node.names:
                yield make_import(name.name)
        elif isinstance(node, ast.ImportFrom):
            for name in node.names:
                yield make_import(node.module, name.name)
