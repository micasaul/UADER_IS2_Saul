from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class OrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> OrderIterator:
        return OrderIterator(self._collection)

    def get_reverse_iterator(self) -> OrderIterator:
        return OrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)

caracteres = WordsCollection()
caracteres.add_item("e")
caracteres.add_item("@")
caracteres.add_item("a")
caracteres.add_item("-")

print("Straight traversal:")
print("\n".join(caracteres))
print("")

print("Reverse traversal:")
print("\n".join(caracteres.get_reverse_iterator()), end="")
print("\n")
