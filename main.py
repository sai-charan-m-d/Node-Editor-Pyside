from PySide6.QtWidgets import QGraphicsView, QApplication
from PySide6.QtCore import Qt
from main_window import NodeEditorWindow
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = NodeEditorWindow()
    window.show()
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)


    app.exec()