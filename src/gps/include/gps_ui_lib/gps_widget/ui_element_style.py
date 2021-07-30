from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QEvent,QObject,QSize
from PyQt5.QtGui import QIcon,QFont
from .ui_widget import Ui_Widget

class ButtonHover(QObject):
    def eventFilter(self,camera,event):
        if event.type()==QEvent.EnabledChange:
            self.state=self.state*(-1)
            if self.state==-1:
                self.icon_name=self.icon_file+'disable-'+self.name+self.file_style
                camera.setIcon(QIcon(self.icon_name))
                camera.setIconSize(QSize(32,32))
            else:
                self.icon_name=self.icon_file+''+self.name+self.file_style
                camera.setIcon(QIcon(self.icon_name))
                camera.setIconSize(QSize(32,32))

        if self.state==1:
            if event.type()==QEvent.Enter:
                #camera.setIcon(QIcon(":/icons/stackedWidget_icon/hover-camera.png"))
                self.icon_name=self.icon_file+'hover-'+self.name+self.file_style
                camera.setIcon(QIcon(self.icon_name))
                camera.setIconSize(QSize(32,32))

                return True

            if event.type()==QEvent.Leave:
                self.icon_name=self.icon_file+''+self.name+self.file_style
                camera.setIcon(QIcon(self.icon_name))
                camera.setIconSize(QSize(32,32))
                return True
        #if event.type()==QEvent.MouseButtonPress:
        #    camera.setIcon(QIcon(":/icons/arm_icon/press-camera.png"))

        #if event.type()==QEvent.MouseButtonRelease:
        #    camera.setIcon(QIcon(":/icons/arm_icon/hover-camera.png"))

        return False
    def SetName(self,name,has_disable=True):
        self.icon_file=':/icons/stackedWidget_icon/'
        self.file_style='.png'
        self.name=name
        if has_disable==True:
            self.state=-1
        else:
            self.state=1

