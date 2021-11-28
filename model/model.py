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
    def a(self) -> int:
        return self._a

    @a.setter
    def a(self, value: int):
        if self._a == value:
            return
        self._a = value

        if self._a > self.b:
            self._b = value
        if self._a > self.c:
            self._c = value
        self.emit_signals()

    @property
    def b(self) -> int:
        return self._b

    @b.setter
    def b(self, value: int):
        if self._b == value:
            return
        b_prev = self._b
        if self.a <= value <= self.c:
            self._b = value
        else:
            self._b = b_prev

        self.b_changed.emit(self._b)

    @property
    def c(self) -> int:
        return self._c

    @c.setter
    def c(self, value: int):
        if self._c == value:
            return
        self._c = value
        self.c_changed.emit(value)

        if self._c < self.b:
            self._b = value
        if self._c < self.a:
            self._a = value
        self.emit_signals()

    def emit_signals(self):
        self.a_changed.emit(self._a)
        self.b_changed.emit(self._b)
        self.c_changed.emit(self._c)

    def __str__(self) -> str:
        return f"{self.a}, {self.b}, {self.c}"

    @classmethod
    def parse(cls, s: str) -> 'Model':
        model = cls()
        (model._a, model._b, model._c, *_) = map(int, filter(str.isalnum, map(str.strip, s.split(","))))
        return model

    @classmethod
    def from_values(cls, a: int, b: int, c: int) -> 'Model':
        model = cls()
        model._a, model._b, model._c = a, b, c
        return model
