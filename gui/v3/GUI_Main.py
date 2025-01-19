#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- This is the main window that will be used to display the key parameters recieved from the on-board sensors of the Hyperloop pod.
- This window also enables you to launch the statesWindow where control commands can be accessed.
- An emergancy stop or a total shutdown of the Hyperloop pod can be enabled by accessing the estopWindow and shutdownWindow respectively.

* This interface is still currently in the development stage, so modifications to its design and functionality will be added overtime.

@author: SupaeroHyperloop
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
# import sip
import os
#import pyqtgraph as pg
#from pyqtgraph import PlotWidget, plot


from statesWindow import Ui_statesWindow
from estopWindow import Ui_estopWindow
from shutdownWindow import Ui_shutdownWindow

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.time = 0.000
        self.timeState = 0.000
        self.log = str()
        self.timestamps = []
        self.velocities = []
        
        # create a timer to update the LCD number
        self.timeTotal = QtCore.QTimer()
        self.timeTotal.setInterval(50)  # update every 50 millisecond
        self.timeTotal.timeout.connect(self.setTotalTimer)
        
        self.stateTime=QtCore.QTimer()
        self.stateTime.setInterval(50) # update every 50 millisecond
        self.stateTime.timeout.connect(self.setStateTimeLCD)

    def openStatesWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_statesWindow()
        self.ui.setupUi(self.window,self,self.getLogList(),self.getTotalTimer())
        self.window.show()
        
    def openEstopWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_estopWindow()
        self.ui.setupUi(self.window,self,self.getLogList())
        self.window.show()
        
    def openShutdownWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_shutdownWindow()
        self.ui.setupUi(self.window,self,self.getLogList())
        self.window.show()
        
#-----------Set clock and update Log of UI --------------------# 
    def startTotalTimer(self):
        self.timeTotal.start()

    def setTotalTimer(self):   
        self.time = self.time + 0.05
        m, s = divmod(self.time, 60)
        self.totalTimerLCD.display('{:02d}:{:02d}'.format(int(m), int(s)))
    
    def getTotalTimer(self):
        return self.time

    def setStateTimer(self):
        self.stateTime.stop()
        self.stateTime.start()
        self.timeState = 0.000

    def setStateTimeLCD(self):    
        self.timeState += 0.05
        self.stateTimerLCD.display("{:.2f}".format(self.timeState))  

    def updateLogList(self, logList):
        self.log = logList

    def getLogList(self):
        return self.log
        

#-----------Simulation of the pod --------------------#   
  
    def computeAccel(self):
        self.computedAccel= 0.000
        self.accelCounter.setInterval(1000)
        self.accelCounter.timeout.connect(self.setAccel)
        self.accelCounter.start()

    def computeVelocity(self):
        self.computedVelocity= 0.000
        self.velocityCounter.setInterval(1000)
        self.velocityCounter.timeout.connect(self.setVelocity)
        self.velocityCounter.start()

    def computeDistance(self):
        self.computedDistance= 0.000
        self.distanceCounter.setInterval(1000)
        self.distanceCounter.timeout.connect(self.setDistance)
        self.distanceCounter.start()
        
    def setAccel(self):
        self.computedAccel+=0.05
        self.AccelReading.setText("{:.2f}".format(self.computedAccel))

    def setVelocity(self):
        self.computedVelocity += (self.computedAccel/20)
        self.VelocityReading.setText("{:.2f}".format(self.computedVelocity))
        self.velocities.append(self.computedVelocity)
        self.timestamps.append(self.time)
        # self.graphWidget.plot(self.timestamps, self.velocities)
    
    def setDistance(self):
        self.computedDistance += 1.0
        self.DistanceReading.setText("{:.2f}".format(self.computedDistance))

#------------------------------------------------------#   

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1465, 1049)
        MainWindow.setStyleSheet("background-color: #1050a9;")
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        #Set font size for the labels
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
         
        self.TimeTotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeTotalLabel.setGeometry(QtCore.QRect(10, 20, 171, 25))
        self.TimeTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeTotalLabel.setFont(font)
        self.TimeTotalLabel.setObjectName("TimeTotalLabel")
        self.TimeTotalLabel.setStyleSheet("background-color: white;")

        self.TimeStateLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeStateLabel.setGeometry(QtCore.QRect(10, 60, 171, 25))
    
        #Time Readings
        self.TimeStateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeStateLabel.setFont(font)
        self.TimeStateLabel.setObjectName("TimeStateLabel")
        self.TimeStateLabel.setStyleSheet("background-color: white;")
        
        self.stateTimerLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.stateTimerLCD.setGeometry(QtCore.QRect(210, 57, 101, 31))
        self.stateTimerLCD.setStyleSheet("QLCDNumber{\n" "\n" "background-color:black;\n" "}")
        self.stateTimerLCD.setObjectName("stateTimerLCD")
        self.totalTimerLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.totalTimerLCD.setGeometry(QtCore.QRect(210, 17, 101, 31))
        self.totalTimerLCD.setStyleSheet("QLCDNumber{\n" "\n" "background-color:black;\n" "}")
        self.totalTimerLCD.setObjectName("totalTimerLCD")

        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QPixmap('GUI_V3\HyperloopLabel.png').scaled(820, 200, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation) #Remember to add your own path
        self.label_Logo.setPixmap(self.pixmap)
        self.label_Logo.setGeometry(QtCore.QRect(400, 650, 900, 500))

        #HVAL Status
        self.HVALStateLabel = QtWidgets.QLabel(self.centralwidget)
        self.HVALStateLabel.setGeometry(QtCore.QRect(10, 220, 171, 25))

        self.HVALStateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HVALStateLabel.setFont(font)
        self.HVALStateLabel.setObjectName("HVALStateLabel")
        self.HVALStateLabel.setStyleSheet("background-color: grey;")

        self.HVALStateLED = QtWidgets.QLabel(self.centralwidget)
        self.HVALredPixmap = QPixmap("GUI_V3\images\HVALred.png").scaled(171, 171, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
        self.HVALStateLED.setPixmap(self.HVALredPixmap)
        self.HVALStateLED.setGeometry(QtCore.QRect(10, 270, 171, 171))

        #IMD Status
        self.IMDStateLabel = QtWidgets.QLabel(self.centralwidget)
        self.IMDStateLabel.setGeometry(QtCore.QRect(201, 220, 171, 25))

        self.IMDStateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IMDStateLabel.setFont(font)
        self.IMDStateLabel.setObjectName("IMDStateLabel")
        self.IMDStateLabel.setStyleSheet("background-color: grey;")

        self.IMDStateLED = QtWidgets.QLabel(self.centralwidget)
        self.IMDredPixmap = QPixmap("GUI_V3\images\HVALred.png").scaled(171, 171, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
        self.IMDStateLED.setPixmap(self.IMDredPixmap)
        self.IMDStateLED.setGeometry(QtCore.QRect(201, 270, 171, 171))

        #BMS HV Status
        self.BMSHVStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.BMSHVStatusLabel.setGeometry(QtCore.QRect(10, 481, 181, 25))

        self.BMSHVStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BMSHVStatusLabel.setFont(font)
        self.BMSHVStatusLabel.setObjectName("BMSHVStatusLabel")
        self.BMSHVStatusLabel.setStyleSheet("background-color: grey;")

        #BMS HV Labels
        self.PackVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.PackVoltageLabel.setGeometry(QtCore.QRect(10, 516, 170, 25))
        self.PackVoltageLabel.setObjectName("PackVoltageLabel")
        self.PackVoltageLabel.setStyleSheet("background-color: white;")

        self.MaximumCellVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaximumCellVoltageLabel.setGeometry(QtCore.QRect(10, 546, 170, 25))
        self.MaximumCellVoltageLabel.setObjectName("MaximumCellVoltageLabel")
        self.MaximumCellVoltageLabel.setStyleSheet("background-color: white;")

        self.MinimumCellVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.MinimumCellVoltageLabel.setGeometry(QtCore.QRect(10, 576, 170, 25))
        self.MinimumCellVoltageLabel.setObjectName("MinimumCellVoltageLabel")
        self.MinimumCellVoltageLabel.setStyleSheet("background-color: white;")

        self.MaximumCellTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaximumCellTempLabel.setGeometry(QtCore.QRect(10, 606, 170, 25))
        self.MaximumCellTempLabel.setObjectName("MaximumCellTempLabel")
        self.MaximumCellTempLabel.setStyleSheet("background-color: white;")

        self.MinimumCellTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.MinimumCellTempLabel.setGeometry(QtCore.QRect(10, 636, 170, 25))
        self.MinimumCellTempLabel.setObjectName("MinimumCellTempLabel")
        self.MinimumCellTempLabel.setStyleSheet("background-color: white;")

        self.PackCurrentLabel = QtWidgets.QLabel(self.centralwidget)
        self.PackCurrentLabel.setGeometry(QtCore.QRect(10, 666, 170, 25))
        self.PackCurrentLabel.setObjectName("PackCurrentLabel")
        self.PackCurrentLabel.setStyleSheet("background-color: white;")

        #BMS HV Readings
        self.PackVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.PackVoltageReading.setGeometry(QtCore.QRect(200, 516, 101, 25))
        self.PackVoltageReading.setObjectName("PackVoltageReading")
        self.PackVoltageReading.setStyleSheet("background-color: white;")

        self.MaximumCellVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.MaximumCellVoltageReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 546, 101, 25)))
        self.MaximumCellVoltageReading.setObjectName("PackVoltageReading")
        self.MaximumCellVoltageReading.setStyleSheet("background-color: white;")

        self.MinimumCellVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.MinimumCellVoltageReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 576, 101, 25)))
        self.MinimumCellVoltageReading.setObjectName("MinimumCellVoltageReading")
        self.MinimumCellVoltageReading.setStyleSheet("background-color: white;")

        self.MaximumCellTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.MaximumCellTempReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 606, 101, 25)))
        self.MaximumCellTempReading.setObjectName("MaximumCellTempReading")
        self.MaximumCellTempReading.setStyleSheet("background-color: white;")

        self.MinimumCellTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.MinimumCellTempReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 636, 101, 25)))
        self.MinimumCellTempReading.setObjectName("MinimumCellTempReading")
        self.MinimumCellTempReading.setStyleSheet("background-color: white;")

        self.PackCurrentReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.PackCurrentReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 666, 101, 25)))
        self.PackCurrentReading.setObjectName("PackCurrentReading")
        self.PackCurrentReading.setStyleSheet("background-color: white;")

        #BMS LV Status
        # self.BMSLVStatusLabel = QtWidgets.QLabel(self.centralwidget)
        # self.BMSLVStatusLabel.setGeometry(QtCore.QRect(10, 706, 181, 25))

        # self.BMSLVStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.BMSLVStatusLabel.setFont(font)
        # self.BMSLVStatusLabel.setObjectName("BMSHVStatusLabel")
        # self.BMSLVStatusLabel.setStyleSheet("background-color: grey;")

        #BMS LV Labels
        # self.LPackVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        # self.LPackVoltageLabel.setGeometry(QtCore.QRect(10, 741, 170, 25))
        # self.LPackVoltageLabel.setObjectName("LPackVoltageLabel")
        # self.LPackVoltageLabel.setStyleSheet("background-color: white;")

        # self.LMaximumCellVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        # self.LMaximumCellVoltageLabel.setGeometry(QtCore.QRect(10, 771, 170, 25))
        # self.LMaximumCellVoltageLabel.setObjectName("LMaximumCellVoltageLabel")
        # self.LMaximumCellVoltageLabel.setStyleSheet("background-color: white;")

        # self.LMinimumCellVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        # self.LMinimumCellVoltageLabel.setGeometry(QtCore.QRect(10, 801, 170, 25))
        # self.LMinimumCellVoltageLabel.setObjectName("LMinimumCellVoltageLabel")
        # self.LMinimumCellVoltageLabel.setStyleSheet("background-color: white;")

        # self.LMaximumCellTempLabel = QtWidgets.QLabel(self.centralwidget)
        # self.LMaximumCellTempLabel.setGeometry(QtCore.QRect(10, 831, 170, 25))
        # self.LMaximumCellTempLabel.setObjectName("LMaximumCellTempLabel")
        # self.LMaximumCellTempLabel.setStyleSheet("background-color: white;")

        # self.LMinimumCellTempLabel = QtWidgets.QLabel(self.centralwidget)
        # self.LMinimumCellTempLabel.setGeometry(QtCore.QRect(10, 861, 170, 25))
        # self.LMinimumCellTempLabel.setObjectName("LMinimumCellTempLabel")
        # self.LMinimumCellTempLabel.setStyleSheet("background-color: white;")

        # self.LPackCurrentLabel = QtWidgets.QLabel(self.centralwidget)
        # self.LPackCurrentLabel.setGeometry(QtCore.QRect(10, 891, 170, 25))
        # self.LPackCurrentLabel.setObjectName("LPackCurrentLabel")
        # self.LPackCurrentLabel.setStyleSheet("background-color: white;")

        #BMS LV Readings
        # self.LPackVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        # self.LPackVoltageReading.setGeometry(QtCore.QRect(200, 741, 101, 25))
        # self.LPackVoltageReading.setObjectName("LPackVoltageReading")
        # self.LPackVoltageReading.setStyleSheet("background-color: white;")

        # self.LMaximumCellVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        # self.LMaximumCellVoltageReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 771, 101, 25)))
        # self.LMaximumCellVoltageReading.setObjectName("LMaximumCellVoltageReading")
        # self.LMaximumCellVoltageReading.setStyleSheet("background-color: white;")

        # self.LMinimumCellVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        # self.LMinimumCellVoltageReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 801, 101, 25)))
        # self.LMinimumCellVoltageReading.setObjectName("LMinimumCellVoltageReading")
        # self.LMinimumCellVoltageReading.setStyleSheet("background-color: white;")

        # self.LMaximumCellTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        # self.LMaximumCellTempReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 831, 101, 25)))
        # self.LMaximumCellTempReading.setObjectName("LMaximumCellTempReading")
        # self.LMaximumCellTempReading.setStyleSheet("background-color: white;")

        # self.LMinimumCellTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        # self.LMinimumCellTempReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 861, 101, 25)))
        # self.LMinimumCellTempReading.setObjectName("LMinimumCellTempReading")
        # self.LMinimumCellTempReading.setStyleSheet("background-color: white;")

        # self.LPackCurrentReading = QtWidgets.QTextBrowser(self.centralwidget)
        # self.LPackCurrentReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 891, 101, 25)))
        # self.LPackCurrentReading.setObjectName("LPackCurrentReading")
        # self.LPackCurrentReading.setStyleSheet("background-color: white;")

        #DC-Link Status
        self.DCLinktatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.DCLinktatusLabel.setGeometry(QtCore.QRect(10, 706, 241, 25))

        self.DCLinktatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DCLinktatusLabel.setFont(font)
        self.DCLinktatusLabel.setObjectName("DCLinktatusLabel")
        self.DCLinktatusLabel.setStyleSheet("background-color: grey;")

        #HV DC-Link Status Reading
        self.DCLinkVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.DCLinkVoltageLabel.setGeometry(QtCore.QRect(10, 741, 170, 25))
        self.DCLinkVoltageLabel.setObjectName("DCLinkVoltageLabel")
        self.DCLinkVoltageLabel.setStyleSheet("background-color: white;")

        self.DCLinkVoltageReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.DCLinkVoltageReading.setGeometry(QtCore.QRect(QtCore.QRect(200, 741, 101, 25)))
        self.DCLinkVoltageReading.setObjectName("DCLinkVoltageReading")
        self.DCLinkVoltageReading.setStyleSheet("background-color: white;")

        #Temperature Readings

        self.PodTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.PodTempReading.setGeometry(QtCore.QRect(460, 85, 101, 28))
        self.PodTempReading.setObjectName("PodTempReading")
        self.PodTempReading.setStyleSheet("background-color: white;")

        self.BrakesTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.BrakesTempReading.setGeometry(QtCore.QRect(460, 115, 101, 28))
        self.BrakesTempReading.setObjectName("BrakesTempReading")
        self.BrakesTempReading.setStyleSheet("background-color: white;")

        self.ClampTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.ClampTempReading.setGeometry(QtCore.QRect(460, 145, 101, 28))
        self.ClampTempReading.setObjectName("ClampTempReading")
        self.ClampTempReading.setStyleSheet("background-color: white;")

        self.BatteryTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.BatteryTempReading.setGeometry(QtCore.QRect(460, 175, 101, 28))
        self.BatteryTempReading.setObjectName("BatteryTempReading")
        self.BatteryTempReading.setStyleSheet("background-color: white;")

        self.TemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.TemperatureLabel.setGeometry(QtCore.QRect(355, 45, 225, 35))

        self.TemperatureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TemperatureLabel.setFont(font)
        self.TemperatureLabel.setObjectName("TemperatureLabel")
        self.TemperatureLabel.setStyleSheet("background-color: grey;")

        #IMU labels

        self.AccelLabel = QtWidgets.QLabel(self.centralwidget)
        self.AccelLabel.setGeometry(QtCore.QRect(670, 145, 121, 28))
        self.AccelLabel.setObjectName("AccelLabel")
        self.AccelLabel.setStyleSheet("background-color: white;")

        self.DistanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.DistanceLabel.setGeometry(QtCore.QRect(670, 85, 121, 28))
        self.DistanceLabel.setObjectName("DistanceLabel")
        self.DistanceLabel.setStyleSheet("background-color: white;")
        
        self.VelocityLabel = QtWidgets.QLabel(self.centralwidget)
        self.VelocityLabel.setGeometry(QtCore.QRect(670, 115, 121, 28))
        self.VelocityLabel.setObjectName("VelocityLabel")
        self.VelocityLabel.setStyleSheet("background-color: white;")

        #IMU Readings

        self.VelocityReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.VelocityReading.setGeometry(QtCore.QRect(795, 115, 101, 28))
        self.VelocityReading.setObjectName("VelocityReading")
        self.VelocityReading.setStyleSheet("background-color: white;")
        
        self.DistanceReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.DistanceReading.setGeometry(QtCore.QRect(795, 85, 101, 28))
        self.DistanceReading.setStyleSheet("background-color: white;")
        self.DistanceReading.setObjectName("DistanceReading")
        
        self.AccelReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.AccelReading .setGeometry(QtCore.QRect(795, 145, 101, 28))
        self.AccelReading .setObjectName("AccelReading ")
        self.AccelReading .setStyleSheet("background-color: white")
        
        #Temperature labels
        
        self.PodTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.PodTempLabel.setGeometry(QtCore.QRect(360, 85, 81, 28))
        self.PodTempLabel.setObjectName("PodTempLabel")
        self.PodTempLabel.setStyleSheet("background-color: white;")
        
        self.BrakesTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrakesTempLabel.setGeometry(QtCore.QRect(360, 115, 81, 28))
        self.BrakesTempLabel.setObjectName("BrakesTempLabel")
        self.BrakesTempLabel.setStyleSheet("background-color: white;")
        
        self.ClampsTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClampsTempLabel.setGeometry(QtCore.QRect(360, 145, 81, 28))
        self.ClampsTempLabel.setObjectName("ClampsTempLabel")
        self.ClampsTempLabel.setStyleSheet("background-color: white;")
        
        self.BatteryTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryTempLabel.setGeometry(QtCore.QRect(360, 175, 81, 28))
        self.BatteryTempLabel.setObjectName("BatteryTempLabel")
        self.BatteryTempLabel.setStyleSheet("background-color: white;")
        
        
        self.IMULabel= QtWidgets.QLabel(self.centralwidget)
        self.IMULabel.setGeometry(QtCore.QRect(675, 45, 225, 35))

        self.IMULabel.setFont(font)
        self.IMULabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IMULabel.setObjectName("IMULabel")
        self.IMULabel.setStyleSheet("background-color: grey;")
        
        self.accelCounter=QtCore.QTimer()
        self.velocityCounter=QtCore.QTimer()
        self.distanceCounter=QtCore.QTimer()
       
       # Levitation labels
        
        self.RearLeftLabel = QtWidgets.QLabel(self.centralwidget)
        self.RearLeftLabel.setGeometry(QtCore.QRect(970, 145, 151, 28))
        self.RearLeftLabel.setObjectName("RearLeftLabel")
        self.RearLeftLabel.setStyleSheet("background-color: white;")
        
        self.FrontRightLabel = QtWidgets.QLabel(self.centralwidget)
        self.FrontRightLabel.setGeometry(QtCore.QRect(970, 115, 151, 28))
        self.FrontRightLabel.setObjectName("FrontRightLabel")
        self.FrontRightLabel.setStyleSheet("background-color: white;")
        
        self.FrontLeftLabel = QtWidgets.QLabel(self.centralwidget)
        self.FrontLeftLabel.setGeometry(QtCore.QRect(970, 85, 151, 28))
        self.FrontLeftLabel.setObjectName("FrontLeftLabel")
        self.FrontLeftLabel.setStyleSheet("background-color: white;")
        
        self.RearRightLabel = QtWidgets.QLabel(self.centralwidget)
        self.RearRightLabel.setGeometry(QtCore.QRect(970, 175, 151, 28))
        self.RearRightLabel.setObjectName("RearRightLabel")
        self.RearRightLabel.setStyleSheet("background-color: white;")

        self.LevitationLabel = QtWidgets.QLabel(self.centralwidget)
        self.LevitationLabel.setGeometry(QtCore.QRect(990, 45, 225, 35))
        self.LevitationLabel.setFont(font)
        self.LevitationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LevitationLabel.setObjectName("LevitationLabel")
        self.LevitationLabel.setStyleSheet("background-color: grey;")
                
        self.RearLeftReading  = QtWidgets.QTextBrowser(self.centralwidget)
        self.RearLeftReading.setGeometry(QtCore.QRect(1130, 145, 101, 28))
        self.RearLeftReading.setObjectName("RearLeftReading ")
        self.RearLeftReading.setStyleSheet("background-color: white;")
        
        self.FrontRightReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.FrontRightReading.setGeometry(QtCore.QRect(1130, 115, 101, 28))
        self.FrontRightReading.setObjectName("FrontRightReading")
        self.FrontRightReading.setStyleSheet("background-color: white;")
        
        self.FrontLeftReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.FrontLeftReading.setGeometry(QtCore.QRect(1130, 85, 101, 28))
        self.FrontLeftReading.setObjectName("FrontLeftReading")
        self.FrontLeftReading.setStyleSheet("background-color: white;")
        
        self.RearRightReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.RearRightReading.setGeometry(QtCore.QRect(1130, 175, 101, 28))
        self.RearRightReading.setObjectName("RearRightReading")
        self.RearRightReading.setStyleSheet("background-color: white;")
        
        # Tab Options
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(400, 220, 921, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.ModeTab = QtWidgets.QWidget()
        self.ModeTab.setObjectName("ModeTab")
        
        self.tabWidget.addTab(self.ModeTab, "")
        self.TeleopTab = QtWidgets.QWidget()
        self.TeleopTab.setObjectName("TeleopTab")
        self.tabWidget.addTab(self.TeleopTab, "")
        self.LowSpeedTab = QtWidgets.QWidget()
        self.LowSpeedTab.setObjectName("LowSpeedTab")
        self.tabWidget.addTab(self.LowSpeedTab, "")
        self.NavTab = QtWidgets.QWidget()
        self.NavTab.setObjectName("NavTab")
        self.tabWidget.addTab(self.NavTab, "")
        
        #Graph for plotting velocity of the pod
        # self.graphWidget = pg.PlotWidget(self.NavTab)

        # plot data: x, y values
        #self.graphWidget.plot(hour, temperature)
        #self.graphWidget.setGeometry(QtCore.QRect(100, 50, 800, 400))
    
        # Enable scrolling option
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Button Options
        
        self.estopButton = QtWidgets.QPushButton(self.ModeTab,
                                                 clicked=lambda:self.openEstopWindow())
        self.estopButton.setGeometry(QtCore.QRect(40, 200, 221, 61))
        self.estopButton.setBaseSize(QtCore.QSize(100, 100))
        self.estopButton.setFont(font)
        self.estopButton.setObjectName("estopButton")
        self.estopButton.setStyleSheet("background-color: gray;")
        
        self.PodModeLabel = QtWidgets.QLabel(self.ModeTab)
        self.PodModeLabel.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.PodModeLabel.setObjectName("PodModeLabel")
        self.PodModeLabel.setFont(font)
        self.PodModeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PodModeLabel.setStyleSheet("background-color: white;")
        
        self.shutdownButton = QtWidgets.QPushButton(self.ModeTab,
                                    clicked=lambda: self.openShutdownWindow())
        self.shutdownButton.setGeometry(QtCore.QRect(40, 261, 221, 61))
        self.shutdownButton.setBaseSize(QtCore.QSize(100, 100))
        self.shutdownButton.setFont(font)
        self.shutdownButton.setAutoFillBackground(True)
        self.shutdownButton.setAutoDefault(False)
        self.shutdownButton.setObjectName("shutdownButton")
        self.shutdownButton.setStyleSheet("background-color: gray;")
        
        self.changeStateButton = QtWidgets.QPushButton(self.ModeTab,
                                    clicked=lambda: self.openStatesWindow())
        self.changeStateButton.setGeometry(QtCore.QRect(40, 140, 221, 61))
        self.changeStateButton.setBaseSize(QtCore.QSize(100, 100))
        self.changeStateButton.setFont(font)
        self.changeStateButton.setObjectName("changeStateButton")
        self.changeStateButton.setStyleSheet("background-color: gray;")
        
        self.LogLabel = QtWidgets.QLabel(self.ModeTab)
        self.LogLabel.setGeometry(QtCore.QRect(330, 170, 581, 381))
        self.LogLabel.setFont(font)
        self.LogLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LogLabel.setObjectName("LogLabel")
        self.LogLabel.setStyleSheet("background-color: gray;")
        
        self.Mode_logging = QtWidgets.QScrollArea(self.ModeTab)
        self.Mode_logging.setGeometry(QtCore.QRect(330, 170, 581, 381))
        self.Mode_logging.setWidgetResizable(True)
        self.Mode_logging.setObjectName("Mode_logging")
        self.Mode_logging.setWidget(self.scrollAreaWidgetContents)
        
        self.LogHistoryBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.LogHistoryBrowser.moveCursor(QtGui.QTextCursor.End) #the self.scrollbar is the same as your self.console_window
        self.LogHistoryBrowser.setVerticalScrollBarPolicy(2)
        self.LogHistoryBrowser.setGeometry(QtCore.QRect(0, 0, 581, 301))
        self.LogHistoryBrowser.setObjectName("LogHistoryBrowser")
        self.LogHistoryBrowser.setStyleSheet("background-color: white;")
        
        self.PodModeReading = QtWidgets.QTextBrowser(self.ModeTab)
        self.PodModeReading.setGeometry(QtCore.QRect(20, 70, 891, 31))
        self.PodModeReading.setStyleSheet("background-color: white;")
        self.PodModeReading.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TimeTotalLabel.setText(_translate("MainWindow", "Time (total)"))
        self.TimeStateLabel.setText(_translate("MainWindow", "Time (state)"))

        self.HVALStateLabel.setText(_translate("MainWindow", "HVAL Status"))
        self.IMDStateLabel.setText(_translate("MainWindow", "IMD Status"))

        self.BMSHVStatusLabel.setText(_translate("MainWindow", "BMS HV Status"))

        self.PackVoltageLabel.setText(_translate("MainWindow", "Pack Voltage (V)"))
        self.PackVoltageReading.setHtml(_translate("MainWindow", "15"))

        self.MaximumCellVoltageLabel.setText(_translate("MainWindow", "Max. Cell Voltage (V)"))
        self.MaximumCellVoltageReading.setHtml(_translate("MainWindow", "15"))

        self.MinimumCellVoltageLabel.setText(_translate("MainWindow", "Min. Cell Voltage (V)"))
        self.MinimumCellVoltageReading.setHtml(_translate("MainWindow", "15"))

        self.MaximumCellTempLabel.setText(_translate("MainWindow", "Max. Cell Temp. (°C)"))
        self.MaximumCellTempReading.setHtml(_translate("MainWindow", "15"))

        self.MinimumCellTempLabel.setText(_translate("MainWindow", "Min. Cell Temp. (°C)"))
        self.MinimumCellTempReading.setHtml(_translate("MainWindow", "15"))

        self.PackCurrentLabel.setText(_translate("MainWindow", "Pack Current (A)"))
        self.PackCurrentReading.setHtml(_translate("MainWindow", "15"))

        self.DCLinktatusLabel.setText(_translate("MainWindow", "HV DC-Link Status"))
        self.DCLinkVoltageLabel.setText(_translate("MainWindow", "Voltage (V)"))
        self.DCLinkVoltageReading.setHtml(_translate("MainWindow", "15"))

        # self.BMSLVStatusLabel.setText(_translate("MainWindow", "BMS LV Status"))

        # self.LPackVoltageLabel.setText(_translate("MainWindow", "Pack Voltage (V)"))
        # self.LPackVoltageReading.setHtml(_translate("MainWindow", "15"))

        # self.LMaximumCellVoltageLabel.setText(_translate("MainWindow", "Max. Cell Voltage (V)"))
        # self.LMaximumCellVoltageReading.setHtml(_translate("MainWindow", "15"))

        # self.LMinimumCellVoltageLabel.setText(_translate("MainWindow", "Min. Cell Voltage (V)"))
        # self.LMinimumCellVoltageReading.setHtml(_translate("MainWindow", "15"))

        # self.LMaximumCellTempLabel.setText(_translate("MainWindow", "Max. Cell Temp. (°C)"))
        # self.LMaximumCellTempReading.setHtml(_translate("MainWindow", "15"))

        # self.LMinimumCellTempLabel.setText(_translate("MainWindow", "Min. Cell Temp. (°C)"))
        # self.LMinimumCellTempReading.setHtml(_translate("MainWindow", "15"))

        # self.LPackCurrentLabel.setText(_translate("MainWindow", "Pack Current (A)"))
        # self.LPackCurrentReading.setHtml(_translate("MainWindow", "15"))

        
        self.PodTempLabel.setText(_translate("MainWindow", "Pod:"))
        self.PodTempReading.setHtml(_translate("MainWindow", "15"))
        self.BrakesTempLabel.setText(_translate("MainWindow", "Brakes:"))
        self.BrakesTempReading.setHtml(_translate("MainWindow", "15"))
        self.TemperatureLabel.setText(_translate("MainWindow", "Temperature (°C)"))
        self.ClampTempReading.setHtml(_translate("MainWindow", "15"))   
        self.BatteryTempReading.setHtml(_translate("MainWindow", "15"))  
        self.ClampsTempLabel.setText(_translate("MainWindow", "Clamp:"))
        self.BatteryTempLabel.setText(_translate("MainWindow", "Battery:"))
        
        self.IMULabel.setText(_translate("MainWindow", "IMU"))
        self.DistanceLabel.setText(_translate("MainWindow", "Distance (m):"))
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity (m/s):"))
        self.AccelLabel.setText(_translate("MainWindow", "Accel (m/s2):"))
        self.VelocityReading.setHtml(_translate("MainWindow", "0"))
        self.DistanceReading.setHtml(_translate("MainWindow", "0"))
        self.AccelReading.setHtml(_translate("MainWindow", "0"))

        self.RearLeftLabel.setText(_translate("MainWindow", "Rear Left:"))
        self.FrontRightLabel.setText(_translate("MainWindow", "Front Right:"))
        self.FrontLeftLabel.setText(_translate("MainWindow", "Front Left:"))
        self.RearLeftReading .setHtml(_translate("MainWindow", "3"))

        self.LevitationLabel.setText(_translate("MainWindow", "Levitation (cm)"))
        self.FrontRightReading.setHtml(_translate("MainWindow", "3"))
        self.FrontLeftReading.setHtml(_translate("MainWindow", "3"))
        self.RearRightReading.setHtml(_translate("MainWindow", "3"))
        self.RearRightLabel.setText(_translate("MainWindow", "Rear Right:"))

        self.estopButton.setText(_translate("MainWindow", "ESTOP"))
        self.PodModeLabel.setText(_translate("MainWindow", "Pod Mode:"))
        self.PodModeReading.setHtml(_translate("MainWindow", ""))
        self.shutdownButton.setText(_translate("MainWindow", "Shutdown"))
        self.changeStateButton.setText(_translate("MainWindow", "Change State"))
        self.LogLabel.setText(_translate("MainWindow", "Log"))
        self.LogHistoryBrowser.setHtml(_translate("MainWindow",None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModeTab), _translate("MainWindow", "Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TeleopTab), _translate("MainWindow", "Teleop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LowSpeedTab), _translate("MainWindow", "Low Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NavTab), _translate("MainWindow", "Nav"))

