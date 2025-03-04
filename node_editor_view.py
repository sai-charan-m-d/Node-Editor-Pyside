from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from node_editor_settings import NodeEditorSettings

class NodeEditorGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__()
        self.setScene(scene)

