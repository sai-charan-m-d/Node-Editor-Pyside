from PySide6.QtGui import QColor
class NodeEditorSettings:
    def __init__(self):
        # Scene Settings

        self._scene_bg_color = QColor("#363636")
        self._scene_width = 64000
        self._scene_height = 64000

        # Scene Grid Settings
        self._scene_grid_color = QColor("#0f0f0f")
        self._grid_size = 30



    def set_scene_bg_color(self,color):
        self._scene_bg_color = color