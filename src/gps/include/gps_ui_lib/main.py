import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon

from ui_widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.__ui=Ui_Widget()
        self.__ui.setupUi(self)

#    def setButtonText(self,text):
#        self.__ui.pushButton_start.setText(text)
    def setLabText(self,text):
        self.__ui.label_lon_value.setText(text)
    def on_pushButton_start_clicked(self):
        print("hello hello hello")

if __name__=="__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    form.setLabText("0")
    sys.exit(app.exec_())
