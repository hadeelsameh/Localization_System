import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush ,QFont ,QPainter, QColor ,QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLabel
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt ,QTimer
import urllib.request
import re
import time
import datetime
class QTimerWithPause (QTimer):
     def init (self, parent = None, name = ""):
           QTimer.__init__ (self, parent, name)

           self.startTime = 0
           self.interval  = 0

class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(700,200,300,200)
       oImage = QImage("sbme.png")
       sImage = oImage.scaled(QSize(276,424))                  
       palette = QPalette()
       palette.setBrush(QPalette.Window, QBrush(sImage))                        
       self.setPalette(palette)
       self.label = QLabel('*', self)
       self.label.setGeometry(150,220,200,50)
       self.timer = QTimer()
       self.timer.setInterval(1000)
       self.update_location()
       self.timer.timeout.connect(self.update_location)
       self.show()

    def startTimer (self, interval):
        self.interval    = interval
        self.startTime = time.time ()
        QTimer.start (self, interval, True)

    def update_location(self):
        self.timer.start()
        data=urllib.request.urlopen("https://api.thingspeak.com/channels/1207778/fields/1.json?results=2")
        select=repr(data.read())
        select=select[300:]
        self.pick_data=re.search('field1":"(.+?)"' ,select)
        self.pick_data=self.pick_data.group(1)
        self.pick_data=re.findall(r'[0-9$]+\d*', self.pick_data)[0]
        print(self.pick_data)
        if (self.pick_data == '00'):                   
            w=70
            l=25
        elif(self.pick_data == '01'):
            w=135
            l=30
        elif(self.pick_data == '02'):
            w=140
            l=80
        elif(self.pick_data == '03'):
            w=140
            l=270
        elif(self.pick_data == '04'):
            w=80
            l=305
        elif(self.pick_data == '05'):
            w=140
            l=200
        elif(self.pick_data == '06'):
            w=70
            l=190
        self.label.move(w,l)
        self.label.setFont(QFont('Arial' ,30))
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    oMainwindow.resize(276, 424)
    sys.exit(app.exec_())