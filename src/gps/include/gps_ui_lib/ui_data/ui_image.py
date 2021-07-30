import cv2 as cv
import numpy as np
import rospy
from enum import Enum
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QObject,pyqtSlot,pyqtSignal, QThread
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

class ImageEncoding(Enum):
    CV_8UC1=0
    CV_8UC3=1


## define PictureUi
class NoImage:
    def __init__(self,encoding):
        height=900
        width=1440
        if encoding==ImageEncoding.CV_8UC3:
            font_color=(0,0,0)
            self.__data=np.zeros((height,width,3),dtype=np.uint8)
        elif encoding==ImageEncoding.CV_8UC1:
            font_color=(0)
            self.__data=np.zeros((height,width,3),dtype=np.uint8)
            self.__data=cv.cvtColor(self.__data,cv.COLOR_BGR2GRAY)
            print(self.__data.shape)

        self.__data.fill(255)

        text="ICAL"
        font=cv.FONT_HERSHEY_SIMPLEX
        font_scale=6
        line_type=2
        text_size,text_base_line=cv.getTextSize(text,font,font_scale,line_type)
        bottom_left_corner_of_text=(int((width-text_size[0])/2),int((height-text_size[1])/2))

        cv.putText(self.__data,text,bottom_left_corner_of_text,font,font_scale,font_color,line_type)
        #self.__data=cv.imread('/home/ical/chi-chun/lena.jpg',-1)
    def GetData(self):
        return self.__data

class ImageProcessThread(QThread):
    image_changed=pyqtSignal(QImage)

    def __init__(self,ui_size,encoding=ImageEncoding.CV_8UC3):
        QThread.__init__(self)
        self.__finish=True
        self.__encoding=encoding
        self.__ui_size=ui_size
        self.__test = 0
    def __del__(self):
        self.wait()

    def SetData(self,data):
        #self.__finish=False
        self.__data=data
    def GetFinsh(self):
        return self.__finish

    def run(self):
        self.__finish=False
        if self.__encoding==ImageEncoding.CV_8UC3:
            ui_img=np.zeros((self.__ui_size.height(),self.__ui_size.width(),3),dtype=np.uint8)
        if self.__encoding==ImageEncoding.CV_8UC1:
            ui_img=np.zeros((self.__ui_size.height(),self.__ui_size.width()),dtype=np.uint8)

        ui_img.fill(0)
        imgsize=self.__data.shape
        if int(imgsize[1]*self.__ui_size.height()/imgsize[0]<self.__ui_size.width()):
            self.__data=cv.resize(self.__data,(int(imgsize[1]*self.__ui_size.height()/imgsize[0]),self.__ui_size.height()),interpolation=cv.INTER_AREA)

        else:
            self.__data=cv.resize(self.__data,(self.__ui_size.width(),int(imgsize[0]*self.__ui_size.width()/imgsize[1])),interpolation=cv.INTER_AREA)

        paste_y=int((ui_img.shape[0]-self.__data.shape[0])/2)
        paste_x=int((ui_img.shape[1]-self.__data.shape[1])/2)

        ui_img[paste_y:paste_y+self.__data.shape[0],paste_x:paste_x+self.__data.shape[1]]=self.__data
        if self.__encoding==ImageEncoding.CV_8UC3:
            self.qImg=QImage(ui_img,self.__ui_size.width(),self.__ui_size.height(),self.__ui_size.width()*3,QImage.Format_RGB888).rgbSwapped()
        if self.__encoding==ImageEncoding.CV_8UC1:
            ui_img=cv.cvtColor(ui_img,cv.COLOR_GRAY2BGR)
            #self.qImg=QImage(ui_img,self.__ui_size.width(),self.__ui_size.height(),self.__ui_size.width(),QImage.Format_Grayscale8).rgbSwapped()
            self.qImg=QImage(ui_img,self.__ui_size.width(),self.__ui_size.height(),self.__ui_size.width()*3,QImage.Format_RGB888).rgbSwapped()
        self.image_changed.emit(self.qImg)
        self.__finish=True

## define L515RGBUi
class ImageUi(QObject):
    image_changed=pyqtSignal(np.ndarray)
    def __init__(self,topic_name,ui_size=None,encoding=ImageEncoding.CV_8UC3,open_thread=None):
        super().__init__()
        self.bridge=CvBridge()
        self.__encoding=encoding
        self.__open_thread=open_thread

        rospy.Subscriber(topic_name,Image, self.CallBack)

        if encoding==ImageEncoding.CV_8UC1:
            self.__cv_bridge_encoding='mono8'
        elif encoding==ImageEncoding.CV_8UC3:
            self.__cv_bridge_encoding='bgr8'

        #Open thread to process the Image
        if self.__open_thread:
            if self.__encoding==ImageEncoding.CV_8UC3:
                self.image_thread=ImageProcessThread(ui_size)
            if self.__encoding==ImageEncoding.CV_8UC1:
                self.image_thread=ImageProcessThread(ui_size,encoding=ImageEncoding.CV_8UC1)
    def InitImage(self):
        no_image=NoImage(self.__encoding)
        self.__data=no_image.GetData()#init self.__data

        if self.__open_thread==None:
            self.image_changed.emit(self.__data)

        elif self.__open_thread==True:
            if(self.image_thread.GetFinsh()):
                self.image_thread.SetData(self.__data)
                self.image_thread.start()

    def CallBack(self,data):
        try:
            self.__data=self.bridge.imgmsg_to_cv2(data,self.__cv_bridge_encoding)
            #self.image_changed.emit(self.__data)
            if self.__open_thread==None:
                self.image_changed.emit(self.__data)
            elif self.__open_thread==True:
                if(self.image_thread.GetFinsh()):
                    self.image_thread.SetData(self.__data)
                    self.image_thread.start()
        except CvBridgeError as e:
            print(e)

    def GetData(self):
        return self.__data

    def GetImageEncoding(self):
        return self.__encoding

