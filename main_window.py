from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QWidget, QVBoxLayout, QGraphicsItem
from PySide6.QtGui import *
from PySide6.QtCore import *
from node_editor_scene import NodeEditorGraphicsScene
from node_editor_view import NodeEditorGraphicsView


class NodeEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Node Editor")

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        #Central Widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        #Creating the graphics scene
        self.node_editor_scene = NodeEditorGraphicsScene()

        #Creatign the Graphics View

        self.view = NodeEditorGraphicsView(self.node_editor_scene)
        self.layout.addWidget(self.view)
        self.show()