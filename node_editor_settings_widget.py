from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from node_editor_settings import NodeEditorSettings
from test_color_widget import ColorPickerWindow

class NodeEditorSettingsWidget(QWidget):
    def __init__(self, settings, scene):
        super().__init__()
        self.settings = settings
        self.scene = scene
        self.setWindowTitle("Settings")
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.color_button = QPushButton("Pick Backgound Color")
        self.color_button.clicked.connect(self.pick_color)
        layout.addWidget(self.color_button)

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            hex_color = color.name()
            self.color_button.setStyleSheet(f"background-color: {hex_color};") 
