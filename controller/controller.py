import typing

from PySide6.QtCore import QObject, Slot

if typing.TYPE_CHECKING:
    from model.model import Model


class Controller(QObject):
    def __init__(self, model: 'Model'):
        super().__init__()

        self._model = model

    @Slot(int)
    def change_a(self, value: int):
        self._model.a = value

    @Slot(int)
    def change_b(self, value: int):
        self._model.b = value

    @Slot(int)
    def change_c(self, value: int):
        self._model.c = value
