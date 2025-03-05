from PySide6.QtGui import QColor
class NodeEditorSettings:
    def __init__(self):
        # Scene Settings

        self._scene_bg_color = QColor("#363636")
        self._scene_width = 64000
        self._scene_height = 64000

        # Scene Grid Settings
        self._scene_grid_color_dark = QColor("#1d1d1d")
        self._scene_grid_color_darker = QColor("#0f0f0f")
        self._grid_size = 15
        self._grid_squares = 4
        self.scene = None

    def update_background(self,color):
        self._scene_bg_color = color
        if self.scene:
            self.scene.update_background()