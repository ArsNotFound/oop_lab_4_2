import os.path
import sys

from PySide6.QtWidgets import QApplication

from controller.controller import Controller
from model.model import Model
from views.main_view import MainView

DATA_FILE = "lab_4.txt"


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = self.get_model()
        self.controller = Controller(self.model)
        self.view = MainView(self.model, self.controller)
        self.view.show()

        self.lastWindowClosed.connect(self.save_model)

    def save_model(self):
        with open(DATA_FILE, "w") as f:
            f.write(str(self.model))

    @staticmethod
    def get_model():
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                s = f.readline()
            model = Model.parse(s)
        else:
            model = Model.from_values(10, 50, 90)
        return model


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
