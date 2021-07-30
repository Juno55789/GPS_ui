import cv2 as cv
import numpy as np
import rospy
from std_msgs.msg import Float64MultiArray
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject,pyqtSlot,pyqtSignal
from cv_bridge import CvBridge



class lat_lon_Ui(QObject):
    gps_data_changed=pyqtSignal(list)
    def __init__(self,topic_name="lat_lon_topic",parent=None):
        super().__init__(parent)
        self.__data=[]
        rospy.Subscriber(topic_name,Float64MultiArray , self.CallBack)

    def CallBack(self,msg):

        self.__data.clear()
        self.__data.append(str(round(msg.data[0],4)))
        self.__data.append(str(round(msg.data[1],4)))
        self.gps_data_changed.emit(self.__data)

