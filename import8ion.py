import ast
from collections import namedtuple
import itertools
import sys


Import = namedtuple('Import', 'module name asname')

def make_import(module, name=None, asname=None):
    return Import(module, name, asname)


class ExtractsImports(object):

    @classmethod
    def extract(cls, source):
        tree = ast.parse(source)
        return list(itertools.chain(*map(cls._make_imports, ast.walk(tree))))

    @classmethod
    def _make_imports(cls, node):
        if isinstance(node, ast.Import):
            for name in node.names:
                yield make_import(name.name, asname=name.asname)
        elif isinstance(node, ast.ImportFrom):
            for name in node.names:
                yield make_import(node.module, name.name, name.asname)


class AlphabetizesImports(object):

    @classmethod
    def alphabetize(cls, imports):
        return sorted(imports)


class WritesImports(object):

    @classmethod
    def write(cls, imports):
        return '\n'.join(cls._write(import_) for import_ in imports)

    @classmethod
    def _write(cls, import_):
        statement = ('from %s import %s' % (import_.module, import_.name) if
                     import_.name else 'import %s' % import_.module)
        if import_.asname:
            statement += ' as ' + import_.asname
        return statement


def organize(code):
    return WritesImports.write(
        AlphabetizesImports.alphabetize(set(ExtractsImports.extract(code))))


if __name__ == '__main__':
    print organize(sys.stdin.read())
