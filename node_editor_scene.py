from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from node_editor_settings import NodeEditorSettings

class NodeEditorGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.settings = NodeEditorSettings()
        self.setSceneRect(-self.settings._scene_width//2,-self.settings._scene_height//2, self.settings._scene_width, self.settings._scene_height)
        self.settings.scene = self
        self.update_background()

    def drawBackground(self, painter: QPainter, rect: QRectF):
        painter.fillRect(rect, self.settings._scene_bg_color)

        left_edge, right_edge = int(rect.left()), int(rect.right())
        top_edge, bottom_edge = int(rect.top()), int(rect.bottom())

        first_left = left_edge - (left_edge % self.settings._grid_size)
        first_top = top_edge - (top_edge % self.settings._grid_size)

        print(left_edge, right_edge, top_edge, bottom_edge)

        for x in range(first_left,right_edge,self.settings._grid_size):
            if (x % (self.settings._grid_squares * self.settings._grid_size)==0):
                painter.setPen(self.settings._scene_grid_color_darker)
                painter.drawLine(x,top_edge,x,bottom_edge)
            else:
                painter.setPen(self.settings._scene_grid_color_dark)
                painter.drawLine(x,top_edge,x,bottom_edge)                

        for y in range(first_top,bottom_edge,self.settings._grid_size):
            if (y % (self.settings._grid_squares *self.settings._grid_size)==0):
                painter.setPen(self.settings._scene_grid_color_darker)
                painter.drawLine(right_edge,y,left_edge,y)
            else:
                painter.setPen(self.settings._scene_grid_color_dark)
                painter.drawLine(right_edge,y,left_edge,y)               

    def update_background(self):
        self.update()



