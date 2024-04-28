import inspect
import sys


class Inspector:
    def __init__(self, py_name):
        """ Allows to easily access all objects in your python file / module
            without knowing their names. Usage: construct passing __name__ as parameter in your file """
        self.py_name = py_name
        self.classes = set()
        self.subclasses = set()
        self.functions = set()

        self.members = inspect.getmembers(sys.modules[self.py_name])

    def get_classes(self) -> set[tuple[str, object]]:
        """ Returns set of all classes in module/file"""
        for name, obj in self.members:
            if inspect.isclass(obj):
                self.classes.add((name, obj))
        return self.classes

    def get_subclasses(self, parent_cls: object) -> set[tuple[str, object]]:
        """ Class object to search for. Returns specific classes set without parent Class"""
        if not self.classes:
            self.get_classes()
        for name, obj in self.classes:
            if issubclass(obj, parent_cls) and name != parent_cls.__name__:
                self.subclasses.add((name, obj))
        return self.subclasses

    def get_functions(self) -> set[tuple[str, object]]:
        """ Returns set of all functions """
        for name, obj in self.members:
            if inspect.isfunction(obj):
                self.functions.add((name, obj))
        return self.functions

