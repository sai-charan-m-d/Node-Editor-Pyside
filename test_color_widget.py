from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class ColorPicker(QWidget):
    colorChangedSignal = Signal(QColor)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ColorPicker")
        layout = QVBoxLayout()
        self.sx = 300
        self.setFixedSize(self.sx,self.sx)
        self.img = self.getRamp()

        self.markerSize =15
        self.markerPos = None
        self.preview = None
        self.setAttribute(Qt.WA_Hover)
        self.installEventFilter(self)
        self.setCursor(Qt.BlankCursor)

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = event.rect() 
        painter.drawImage(0,0,self.img)
        if self.markerPos:
            painter.setPen(QPen(QBrush(Qt.black),1))
            painter.drawEllipse(self.markerPos, self.markerSize,self.markerSize )
        if self.preview:
            painter.setPen(QPen(QBrush(QColor(0,0,0,50)),3))
            painter.drawEllipse(self.preview, self.markerSize,self.markerSize )


        painter.end()

    def getRamp(self):
        img = QImage(self.sx,self.sx,QImage.Format_RGB32)
        color = QColor()
        for x in range(self.sx):
            h = x/float(self.sx)
            for y in range(self.sx):
                s = y/float(self.sx)
                v = 1
                color.setHsvF(h,s,v)
                img.setPixel(x,y,color.rgb())
        return img

    def mousePressEvent(self,event):
        super(ColorPicker,self).mousePressEvent(event)
        self.markerPos = event.pos()
        self.getColor(event.pos())
        self.update()

    def mouseMoveEvent(self,event):
        super(ColorPicker,self).mouseMoveEvent(event)
        self.markerPos = event.pos()
        self.getColor(event.pos())
        self.update()
    
    def eventFilter(self,obj,event):
        if event.type() == QEvent.HoverMove:
            self.preview = event.pos()
            self.update()
            return True
        return False


    def getColor(self,pos):
        print(pos)
        h=pos.x()/float(self.sx)
        s=pos.y()/float(self.sx)
        c= QColor()
        c.setHsvF(h,s,1)
        self.colorChangedSignal.emit(c)

class ColorPickerWindow(QWidget):
    def __init__(self):
        super(ColorPickerWindow,self).__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.colors_layout = QHBoxLayout()
        self.color = QLabel()
        self.color2 = QLabel()
        self.color.setAutoFillBackground(True)
        self.color2.setAutoFillBackground(True)
        self.color.setMinimumHeight(40)
        self.color.setMinimumHeight(40)
        self.colors_layout.addWidget(self.color)
        self.colors_layout.addWidget(self.color2)
        self.layout.addLayout(self.colors_layout)

        self.picker = ColorPicker()
        self.layout.addWidget(self.picker)
        self.picker.colorChangedSignal.connect(self.updateColor)

    def updateColor(self,color):
        print(color.name())
        pallete = self.color.palette()
        pallete.setColor(self.color.backgroundRole(),color)
        self.color.setPalette(pallete)




if __name__ == "__main__":
    app = QApplication([])
    window = ColorPickerWindow()
    window.show()
    app.exec()
