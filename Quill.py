import sys
from configparser import ConfigParser

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QApplication,
    QPushButton,
    QFileDialog,
)

from fugle_trade.sdk import SDK

# Import snake_case and true_property after PySide6 imports.
from __feature__ import snake_case, true_property  # noqa


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_fixed_size(300, 100)
        self.window_title = "Quill"

        self.button = QPushButton("Select config.ini")
        self.button.clicked.connect(self.setup_sdk)

        self.certname = QLabel()
        self.certname.alignment = Qt.AlignCenter

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.add_widget(self.certname)
        self.vertical_layout.add_widget(self.button)

        self.widget_container = QWidget()
        self.widget_container.set_layout(self.vertical_layout)

        self.set_central_widget(self.widget_container)

    def setup_sdk(self):
        browser = QFileDialog()
        browser.file_mode = QFileDialog.ExistingFiles
        browser.name_filter = "Config files (*.ini)"

        if browser.exec():
            names = browser.selected_files()
            path = names[0]

            self.config = ConfigParser()
            self.config.read(path)
            self.sdk = SDK(self.config)

            certinfo = self.sdk.certinfo()

            self.certname.text = f"Cert Name: {certinfo.get("cn")}"


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
