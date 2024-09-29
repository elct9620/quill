import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from ui_mainwindow import Ui_MainWindow


# Import snake_case and true_property after PySide6 imports.
from __feature__ import snake_case, true_property  # noqa


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
