"""Шаблон проектирования (Стратегия)"""

from abc import ABC, abstractmethod
from typing import Dict
import pickle
import json


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def write(self, value: Dict):
        raise NotImplementedError


class JSONFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self.__filename = filename

    def read(self) -> Dict:
        with open(self.__filename, encoding='UTF-8') as file:
            return json.load(file)

    def write(self, value: Dict):
        with open(self.__filename, 'w', encoding='UTF-8') as file:
            json.dump(value, file, ensure_ascii=False)


class PickleDriver(IStructureDriver):
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> Dict:
        with open(self.__filename, 'rb') as file:
            return pickle.load(file)

    def write(self, value: Dict):
        with open(self.__filename, 'wb') as file:
            pickle.dump(value, file)


class JSONStringDriver(IStructureDriver):
    def __init__(self, string: str = '{}'):
        self.__string = string

    def get_string(self):
        return self.__string

    def read(self) -> Dict:
        return json.loads(self.__string)

    def write(self, value):
        self.__string = json.dumps(value)


class SDWorkers:
    def __init__(self, structure_driver: IStructureDriver):
        self.__structure_driver = structure_driver

    def load(self):
        return self.__structure_driver.read()

    def save(self, value):
        self.__structure_driver.write(value)

    def set_structure_driver(self, driver):
        self.__structure_driver = driver




obj = {
    "a": [
        {"a": 1, "b": 5, "c": True, "d": "some_str"}, {"first": 54, "second": "some_str"}
    ],
    "value": (1, 2, 3)
}


# fd_string = JSONStringDriver()
# fd_string.write(obj)
# print(fd_string.get_string())
#
# print(id(1))
# print(id(2))


# fd = JSONFileDriver("some_fie.json")
# fd.write(obj)
# obj2 = fd.read()
# obj2["value"] = tuple(obj2["value"])
# assert obj == obj2

# s = json.dumps([1, 3, "kfhgg"])
# print(s, type(s))
# obj5 = json.loads(s)
# print(obj5, type(obj5))

# fd_pickle = PickleDriver("some_file_picle.json")
# fd_pickle.write(obj)
# obj4 = fd_pickle.read()
# print(obj4)

# id(1)
#
# Node: {
#     "id": 325346547467568,
#     "data": "some_data",
#     "prev_node": "Node",
#     "next_node": 4653476477
# }
#
# LinkedList: {
#     124323543674: Node,
#     245465346354: Node,
# }
#
#
# ["some_data", 1, 10]
































# В JSON только двойные кавычки. число-число, словарь-словарь, список-список, tuple-список, None-null, True-true


# try:
#     print("Hello")
# except RuntimeError:
#     raise
# except ConnectionError:
#     raise
# else:
#     print("Not exception")
# finally:
#     print("End")

# Менеджер контекста
# class some_method:
#     def __enter__(self):
#         ...
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         ...
# return False(True)

# with some_method(Exception):
# raise Exception("EERRROR")
