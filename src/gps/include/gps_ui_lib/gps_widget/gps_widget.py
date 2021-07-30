import sys
import numpy as np
import os
from ui_data.ui_other import*
from ui_data.ui_image import *
from .ui_element_style import *
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPalette, QImage, QPixmap,QIcon
from PyQt5.QtCore import Qt, pyqtSlot,QSize
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from .ui_widget import Ui_Widget



class gpsWidget(QWidget):
    def __init__(self,parent=None):

        super().__init__(parent)
        rospy.init_node('gps_ui')
        self.ui=Ui_Widget()
        self.ui.setupUi(self)

        #============Set Image=========
        #=====And Function still use camel case====
        self.__gps_map_i=ImageUi("gps_map/image",ui_size=self.ui.label_gps_map.geometry(),open_thread=True)
        self.__gps_map_i.image_thread.image_changed.connect(self.do_gpsRgb)
        self.__gps_map_i.InitImage()
        #============Set lon_lat_value========
        self.__gps_data = lat_lon_Ui("lat_lon_topic")
        self.__gps_data.gps_data_changed.connect(self.do_gps_data_change)

#======================ui self slot function===============

    @pyqtSlot(list)
    def do_gps_data_change(self,data):
        self.ui.label_lat_value.setText(data[0])
        self.ui.label_lon_value.setText(data[1])

    @pyqtSlot(QImage)
    def do_gpsRgb(self,data):
        self.ui.label_gps_map.setPixmap(QPixmap.fromImage(data))
