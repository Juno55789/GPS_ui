# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(716, 299)
        self.label_gps_map = QtWidgets.QLabel(Widget)
        self.label_gps_map.setGeometry(QtCore.QRect(299, 30, 392, 233))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_gps_map.setFont(font)
        self.label_gps_map.setScaledContents(False)
        self.label_gps_map.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gps_map.setObjectName("label_gps_map")
        self.layoutWidget = QtWidgets.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 130, 228, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_lon = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lon.setFont(font)
        self.label_lon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lon.setObjectName("label_lon")
        self.horizontalLayout_3.addWidget(self.label_lon)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_lon_value = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lon_value.setFont(font)
        self.label_lon_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lon_value.setObjectName("label_lon_value")
        self.horizontalLayout_3.addWidget(self.label_lon_value)
        self.layoutWidget_2 = QtWidgets.QWidget(Widget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(31, 90, 214, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_lat = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lat.setFont(font)
        self.label_lat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lat.setObjectName("label_lat")
        self.horizontalLayout_4.addWidget(self.label_lat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_lat_value = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lat_value.setFont(font)
        self.label_lat_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lat_value.setObjectName("label_lat_value")
        self.horizontalLayout_4.addWidget(self.label_lat_value)
        self.pushButton_start = QtWidgets.QPushButton(Widget)
        self.pushButton_start.setGeometry(QtCore.QRect(60, 240, 131, 31))
        self.pushButton_start.setObjectName("pushButton_start")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_gps_map.setText(_translate("Widget", "gps_map"))
        self.label_lon.setText(_translate("Widget", "longitude"))
        self.label_lon_value.setText(_translate("Widget", "lonfitude value"))
        self.label_lat.setText(_translate("Widget", "latitude"))
        self.label_lat_value.setText(_translate("Widget", "latitude value"))
        self.pushButton_start.setText(_translate("Widget", "Start"))
