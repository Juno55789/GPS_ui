#!/usr/bin/env python3

import signal
import sys
sys.path.append('/home/juno/GPS/ros_test/gps/src/gps/include/gps_ui_lib/')
#sys.path.append('$(find gps)/include/gps_ui_lib/')

from gps_widget.gps_widget import gpsWidget
from ui_data.ui_other import *
from PyQt5.QtWidgets import QApplication,QWidget


def signal_handler(sig, frame):
    print("ctrl c")
    app.quit()

if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)
    app =QApplication(sys.argv)
    form=gpsWidget()
    form.show()
    sys.exit(app.exec_())
