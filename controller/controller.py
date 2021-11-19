import typing

from PySide6.QtCore import QObject, Slot

if typing.TYPE_CHECKING:
    from model.model import Model


class Controller(QObject):
    def __init__(self, model: Model):
        super().__init__()

        self._model = model

    @Slot(int)
    def change_a(self, value: int):
        if self._model.a == value:
            return
        self._model.a = value
        if value > self._model.b:
            self._model.b = value
        if value > self._model.c:
            self._model.c = value

    @Slot(int)
    def change_b(self, value: int):
        if self._model.b == value:
            return
        b_prev = self._model.b
        if self._model.a <= value <= self._model.c:
            self._model.b = value
        else:
            self._model.b = b_prev

    @Slot(int)
    def change_c(self, value: int):
        if self._model.c == value:
            return
        self._model.c = value
        if value < self._model.b:
            self._model.b = value
        if value < self._model.a:
            self._model.a = value
