from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView

class NodeEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node Editor")
        self.setGeometry(100,100,800,600)

        self.scene = QGraphicsScene()
        self.scene.addText("Hello World")
        self.view = QGraphicsView(self.scene, self)
        self.view.show()
