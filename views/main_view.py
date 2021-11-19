import typing

from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow

from views.main_view_ui import Ui_Form

if typing.TYPE_CHECKING:
    from controller.controller import Controller
    from model.model import Model


class MainView(QMainWindow):
    def __init__(self, model: Model, controller: Controller):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = Ui_Form()
        self._ui.setupUi(self)

        self._ui.a_spinBox.valueChanged.connect(self._controller.change_a)
        self._ui.a_horizontalSlider.valueChanged.connect(self._controller.change_a)
        self._ui.a_lineEdit.setValidator(QIntValidator(0, 100, self))
        self._ui.a_lineEdit.returnPressed.connect(
            lambda: self._controller.change_a(int(self._ui.a_lineEdit.text() or "0"))
        )

        self._ui.b_spinBox.valueChanged.connect(self._controller.change_b)
        self._ui.b_horizontalSlider.valueChanged.connect(self._controller.change_b)
        self._ui.b_lineEdit.setValidator(QIntValidator(0, 100, self))
        self._ui.b_lineEdit.returnPressed.connect(
            lambda: self._controller.change_b(int(self._ui.b_lineEdit.text() or "0"))
        )

        self._ui.c_spinBox.valueChanged.connect(self._controller.change_c)
        self._ui.c_horizontalSlider.valueChanged.connect(self._controller.change_c)
        self._ui.c_lineEdit.setValidator(QIntValidator(0, 100, self))
        self._ui.c_lineEdit.returnPressed.connect(
            lambda: self._controller.change_c(int(self._ui.c_lineEdit.text() or "0"))
        )

        self._model.a_changed.connect(self.a_changed)
        self._model.b_changed.connect(self.b_changed)
        self._model.c_changed.connect(self.c_changed)

        self._model.emit_signals()

    @Slot(int)
    def a_changed(self, value: int):
        self._ui.a_spinBox.setValue(value)
        self._ui.a_horizontalSlider.setValue(value)
        self._ui.a_lineEdit.setText(str(value))

    @Slot(int)
    def b_changed(self, value: int):
        self._ui.b_spinBox.setValue(value)
        self._ui.b_horizontalSlider.setValue(value)
        self._ui.b_lineEdit.setText(str(value))

    @Slot(int)
    def c_changed(self, value: int):
        self._ui.c_spinBox.setValue(value)
        self._ui.c_horizontalSlider.setValue(value)
        self._ui.c_lineEdit.setText(str(value))
