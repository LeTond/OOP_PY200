
import Drivers

from typing import Optional, Any, Iterable
from typing import Dict

import weakref


class _Node:
    def __init__(self, data: Any, prev_node: Optional["_Node"] = None, next_node: Optional["_Node"] = None):
        self.prev_node = prev_node
        self.data = data
        self.next_node = next_node

    @property
    def prev_node(self):
        return self._prev_node() if self._prev_node else None

    @prev_node.setter
    def prev_node(self, value):
        if value is None:
            self._prev_node = None
        else:
            self._prev_node = weakref.ref(value)


class LinkedList:
    def __init__(self):
        self.head: Optional[_Node] = None
        self.tail: Optional[_Node] = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        list_ = str()
        for node in self:
            list_ += f" {node} =>"
        return list_

    def __iter__(self):
        for node in self._node_iter():
            yield node.data

    def _node_iter(self) -> Iterable[_Node]:
        current = self.head
        while current:
            yield current
            current = current.next_node

    def append(self, node: Any):
        """
        Добавление ДАННЫХ в конец списка
        """
        if self.head is None:
            self.head = _Node(node, None, None)  # None <- node -> None
        elif self.tail is None:
            self.tail = _Node(node, self.head, None)  # Если хвоста нет, то создаем хвост со ссылками на ГН назад
            self.head.next_node = self.tail  # Ссылка от ГН к хвосту (второй ноде)
        else:
            current_node = self.tail  # Назначаем значение хвостовой ноды как "текущую"
            self.tail = _Node(node, current_node, None)  # Назначаем хвостовой ноде новое значение
            # со ссылками на текущую ноду
            current_node.next_node = self.tail
        self._size += 1

    def insert(self, node: Any, index: int = 0):
        """
        Добавление ДАННЫХ в список по индексу
        """
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть числом")

        if index == 0:
            head = self.head  # Переназначаем ГН
            self.head = _Node(node, None, head)  # Назначаем новую ноду головной
            self._size += 1

        elif index > self._size:
            self.append(node)

        else:
            old_head = self.head  # Переназначаем ГН
            after_head = old_head.next_node  # Делаем головную ноду "следующей"
            counter = 1
            while counter < self._size:
                if counter == index:
                    old_head.next_node = None  # Делаем ссылку на следующую ноду None
                    after_head.prev_node = None  # Делаем ссылку следующей ноды взад None
                    new_node = _Node(node, old_head, after_head)  # Создаем новую ноду
                    old_head.next_node = new_node  # Ссылка от ГН к новой ноде
                    after_head.prev_node = new_node  # Ссылка от "следующей ноды" к новой назад
                old_head = old_head.next_node  # Если индекс не равен, то переназначаем ГН на следуюущую...
                after_head = old_head.next_node
                counter += 1
            self._size += 1

    def clear(self):
        """
        Очистка списка
        """
        self._size = 0
        self.head = None
        self.tail = None

    def find(self, data: Any):
        """
        Поиск ИНДЕКСА узла (Node'ы), в котором хранятся данные
        """
        for i, node_data in enumerate(self):
            if node_data == data:
                return i
        return "Пустота"

    def delete(self, index: int):
        """
        Удаление узла (Node'ы) по индексу
        """
        prev_node: Optional[_Node] = None
        for i, node in enumerate(self._node_iter()):
            if i == index:
                if prev_node is None:
                    self.head = node.next_node
                else:
                    prev_node.next_node = node.next_node
                self._size -= 1
                break
            prev_node = node

    def index(self, index: int):
        """
        Получение данных по индексу
        """
        for ind, value in enumerate(self):
            if ind == index:
                return value
        return "Пустота"

    def save_dict(self):
        linked_list = {}
        for node in self._node_iter():
            linked_list[id(node)] = {
                "data": node.data,
                "prev_node": id(node.prev_node) if node.prev_node else None,
                "next_node": id(node.next_node) if node.next_node else None
            }
        return linked_list

    def load_dict(self, value: Dict):
        self.clear()
        for ind, val in value.items():
            node_dict = val
            self.append(node_dict["data"])
        print(self.save_dict())

    def set_structure_driver(self, driver):
        self.__structure_driver = driver

    def save(self):
        self.__structure_driver.write(self.save_dict())

    def load(self):
        self.load_dict(self.__structure_driver.read())


if __name__ == '__main__':
    ll = LinkedList()
    ll.append("some_data_4")
    ll.append("some_data_5")
    ll.append("some_data_6")
    ll.insert("some_data_0", 0)
    ll.insert("some_data_1", 3)
    ll.insert("some_data_2", 2)
    ll.insert("some_data_3", 0)
    # print(ll)
    # print(ll.find("some_data_5"))

    obj = {
        "a": [
            {"a": 1, "b": 5, "c": True, "d": "some_str"}, {"first": 54, "second": "some_str"}
        ],
        "value": (1, 2, 3)
    }

    dct = ll.save_dict()
    # print(dct)
    print(ll.load_dict(dct))
    print(dct)

    # print(ll)
    # ll.delete(5)
    # print(len(ll))
    # print(ll)
    # ll.delete(1)
    # print(len(ll))
    # print(ll)
    # print(ll)
    # print(len(ll))
    # print(ll.index(1))
    # print(ll.index(3))
    # print(ll.index(14))
