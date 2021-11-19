from PySide6.QtCore import QObject, Signal


class Model(QObject):
    a_changed = Signal(int)
    b_changed = Signal(int)
    c_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self._a = 0
        self._b = 0
        self._c = 0

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
        self.a_changed.emit(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
        self.b_changed.emit(value)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
        self.c_changed.emit(value)
