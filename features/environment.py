import sys
from PySide6.QtWidgets import QApplication

from Quill import MainWindow


def before_scenario(context, scenario):
    context.app = QApplication(sys.argv)
    context.window = MainWindow()
