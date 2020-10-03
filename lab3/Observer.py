"""Реализация наблюдателя"""
import weakref


class Observer:
    def update(self, *args):
        pass


class Subject:
    def __init__(self):
        self.__obs = set()

    def add_observer(self, obs: Observer):
        self.__obs.add((weakref.ref(obs)))

    def remove_observer(self, obs: Observer):
        self.__obs[obs].remove(obs)

    def notify(self):
        for obs in self.__obs:
            obs().update()


class Data(Subject):
    def __init__(self, data):
        super().__init__()
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if self._data != data:
            self._data = data
            self.notify()


# class PrintView(Observer):
#     def update(self, subject):
#         print(f'Value changed: {hex(id(subject))}')
#
#
# class SimpleView(Observer):
#     def update(self, subject):
#         print(f'SimpleView: {hex(id(subject))}')
#
#
# class InputSubject(Subject):
#     def __init__(self):
#         super().__init__()
#         self.__value = 0
#
#     def enter_value(self):
#         value = input("Enter new value >")
#         if value != self.__value:
#             self.__value = value
#             self.notify()


# s = InputSubject()
# s.add_observer(PrintView())
# s.add_observer(SimpleView())

# for _ in range(2):
#     s.enter_value()



"""Адаптер"""
# import numpy as np
#
#
# a = np.array([1, 4, 6, 7, 8])
#
#
# class ListAdapter:
#     def __init__(self, nparray):
#         self.__nparray = nparray
#
#     def __len__(self):
#         return len(self.__nparray)
#
#     def index(self, elem):
#
#         for ind, el in enumerate(self.__nparray):
#             if el == elem:
#                 return ind
#         return -1
        # return list(self.__nparray).index(elem)


# la = ListAdapter(a)
# print(la.index(99))


