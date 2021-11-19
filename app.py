import sys

from PySide6.QtWidgets import QApplication

from controller.controller import Controller
from model.model import Model
from views.main_view import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = MainView(self.model, self.controller)
        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
