import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QApplication,
)

# Import snake_case and true_property after PySide6 imports.
from __feature__ import snake_case, true_property  # noqa


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_fixed_size(300, 100)
        self.window_title = "Quill"

        self.greeting = QLabel("Hello world!")
        self.greeting.alignment = Qt.AlignCenter

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.add_widget(self.greeting)

        self.widget_container = QWidget()
        self.widget_container.set_layout(self.vertical_layout)

        self.set_central_widget(self.widget_container)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
