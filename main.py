from PySide6.QtWidgets import QGraphicsView, QApplication
from main_window import NodeEditorWindow
import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = NodeEditorWindow()
    window.show()
    sys.exit(app.exec())