# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1097)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signalPlotGroup = QtWidgets.QGroupBox(self.groupBox_2)
        self.signalPlotGroup.setTitle("")
        self.signalPlotGroup.setObjectName("signalPlotGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.signalPlotGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aSlider = QtWidgets.QSlider(self.signalPlotGroup)
        self.aSlider.setMinimum(1)
        self.aSlider.setMaximum(100)
        self.aSlider.setOrientation(QtCore.Qt.Vertical)
        self.aSlider.setObjectName("aSlider")
        self.gridLayout_3.addWidget(self.aSlider, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.signalPlotGroup)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 2, 1, 1)
        self.nSlider = QtWidgets.QSlider(self.signalPlotGroup)
        self.nSlider.setMinimum(5)
        self.nSlider.setMaximum(200)
        self.nSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nSlider.setObjectName("nSlider")
        self.gridLayout_3.addWidget(self.nSlider, 1, 1, 1, 1)
        self.bSlider = QtWidgets.QSlider(self.signalPlotGroup)
        self.bSlider.setOrientation(QtCore.Qt.Vertical)
        self.bSlider.setObjectName("bSlider")
        self.gridLayout_3.addWidget(self.bSlider, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.signalPlotGroup)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.init_signal_group_box = QtWidgets.QGroupBox(self.signalPlotGroup)
        self.init_signal_group_box.setTitle("")
        self.init_signal_group_box.setObjectName("init_signal_group_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.init_signal_group_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 781, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.init_signal_vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.init_signal_vlayout.setContentsMargins(0, 0, 0, 0)
        self.init_signal_vlayout.setObjectName("init_signal_vlayout")
        self.gridLayout_3.addWidget(self.init_signal_group_box, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.signalPlotGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.signalPlotGroup)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.noisySignalPlotGroup = QtWidgets.QGroupBox(self.groupBox_2)
        self.noisySignalPlotGroup.setTitle("")
        self.noisySignalPlotGroup.setObjectName("noisySignalPlotGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.noisySignalPlotGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sigmaSlider = QtWidgets.QSlider(self.noisySignalPlotGroup)
        self.sigmaSlider.setMinimum(1)
        self.sigmaSlider.setMaximum(50)
        self.sigmaSlider.setOrientation(QtCore.Qt.Vertical)
        self.sigmaSlider.setObjectName("sigmaSlider")
        self.gridLayout_5.addWidget(self.sigmaSlider, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.noisySignalPlotGroup)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.meanSlider = QtWidgets.QSlider(self.noisySignalPlotGroup)
        self.meanSlider.setMinimum(1)
        self.meanSlider.setMaximum(40)
        self.meanSlider.setOrientation(QtCore.Qt.Vertical)
        self.meanSlider.setObjectName("meanSlider")
        self.gridLayout_5.addWidget(self.meanSlider, 0, 0, 1, 1)
        self.noisy_signal_group_box = QtWidgets.QGroupBox(self.noisySignalPlotGroup)
        self.noisy_signal_group_box.setTitle("")
        self.noisy_signal_group_box.setObjectName("noisy_signal_group_box")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.noisy_signal_group_box)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 781, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.noisy_signal_vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.noisy_signal_vlayout.setContentsMargins(0, 0, 0, 0)
        self.noisy_signal_vlayout.setObjectName("noisy_signal_vlayout")
        self.gridLayout_5.addWidget(self.noisy_signal_group_box, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.noisySignalPlotGroup)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.noisySignalPlotGroup)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.binsSlider = QtWidgets.QSlider(self.noisySignalPlotGroup)
        self.binsSlider.setMinimum(2)
        self.binsSlider.setMaximum(15)
        self.binsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.binsSlider.setObjectName("binsSlider")
        self.gridLayout_5.addWidget(self.binsSlider, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.noisySignalPlotGroup)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.noiseGroup = QtWidgets.QGroupBox(self.groupBox)
        self.noiseGroup.setTitle("")
        self.noiseGroup.setObjectName("noiseGroup")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.noiseGroup)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.noiseType = QtWidgets.QComboBox(self.noiseGroup)
        self.noiseType.setObjectName("noiseType")
        self.noiseType.addItem("")
        self.noiseType.addItem("")
        self.gridLayout_6.addWidget(self.noiseType, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.noiseGroup)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.noise_dist_group_box = QtWidgets.QGroupBox(self.noiseGroup)
        self.noise_dist_group_box.setTitle("")
        self.noise_dist_group_box.setObjectName("noise_dist_group_box")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.noise_dist_group_box)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 841, 421))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.noise_distribution_vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.noise_distribution_vlayout.setContentsMargins(0, 0, 0, 0)
        self.noise_distribution_vlayout.setObjectName("noise_distribution_vlayout")
        self.verticalLayout_7.addWidget(self.noise_dist_group_box)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 2)
        self.gridLayout_10.addWidget(self.noiseGroup, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.resultsCalculationBox = QtWidgets.QGroupBox(self.groupBox_5)
        self.resultsCalculationBox.setTitle("")
        self.resultsCalculationBox.setObjectName("resultsCalculationBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.resultsCalculationBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.errorsLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.errorsLabel.setObjectName("errorsLabel")
        self.horizontalLayout_4.addWidget(self.errorsLabel)
        self.errorALabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.errorALabel.setObjectName("errorALabel")
        self.horizontalLayout_4.addWidget(self.errorALabel)
        self.errorBLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.errorBLabel.setObjectName("errorBLabel")
        self.horizontalLayout_4.addWidget(self.errorBLabel)
        self.errorSigmaLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.errorSigmaLabel.setObjectName("errorSigmaLabel")
        self.horizontalLayout_4.addWidget(self.errorSigmaLabel)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.RLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.RLabel.setMinimumSize(QtCore.QSize(450, 0))
        self.RLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RLabel.setObjectName("RLabel")
        self.gridLayout_8.addWidget(self.RLabel, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.resultsCalculationBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.initialValuesLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.initialValuesLabel.setObjectName("initialValuesLabel")
        self.horizontalLayout_5.addWidget(self.initialValuesLabel)
        self.initialALabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.initialALabel.setObjectName("initialALabel")
        self.horizontalLayout_5.addWidget(self.initialALabel)
        self.initialBLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.initialBLabel.setObjectName("initialBLabel")
        self.horizontalLayout_5.addWidget(self.initialBLabel)
        self.initialSigmaLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.initialSigmaLabel.setObjectName("initialSigmaLabel")
        self.horizontalLayout_5.addWidget(self.initialSigmaLabel)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.estimatedLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.estimatedLabel.setObjectName("estimatedLabel")
        self.horizontalLayout_3.addWidget(self.estimatedLabel)
        self.estimatedALabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.estimatedALabel.setObjectName("estimatedALabel")
        self.horizontalLayout_3.addWidget(self.estimatedALabel)
        self.estimatedBLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.estimatedBLabel.setObjectName("estimatedBLabel")
        self.horizontalLayout_3.addWidget(self.estimatedBLabel)
        self.estimatedSigmaLabel = QtWidgets.QLabel(self.resultsCalculationBox)
        self.estimatedSigmaLabel.setObjectName("estimatedSigmaLabel")
        self.horizontalLayout_3.addWidget(self.estimatedSigmaLabel)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.resultsCalculationBox)
        self.gridLayout_7.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.noisePlotVLayout = QtWidgets.QVBoxLayout()
        self.noisePlotVLayout.setObjectName("noisePlotVLayout")
        self.noise_vlayout = QtWidgets.QVBoxLayout()
        self.noise_vlayout.setObjectName("noise_vlayout")
        self.noisePlotVLayout.addLayout(self.noise_vlayout)
        self.gridLayout_9.addLayout(self.noisePlotVLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_11)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "B"))
        self.label_2.setText(_translate("MainWindow", "A"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.label_7.setText(_translate("MainWindow", "Bins"))
        self.label_6.setText(_translate("MainWindow", "S"))
        self.label_5.setText(_translate("MainWindow", "M"))
        self.noiseType.setItemText(0, _translate("MainWindow", "Gaussian"))
        self.noiseType.setItemText(1, _translate("MainWindow", "Uniform"))
        self.label.setText(_translate("MainWindow", "Noise Distribution"))
        self.errorsLabel.setText(_translate("MainWindow", "Errors"))
        self.errorALabel.setText(_translate("MainWindow", "0"))
        self.errorBLabel.setText(_translate("MainWindow", "0"))
        self.errorSigmaLabel.setText(_translate("MainWindow", "0"))
        self.RLabel.setText(_translate("MainWindow", "R^2=0"))
        self.label_10.setText(_translate("MainWindow", "Results"))
        self.initialValuesLabel.setText(_translate("MainWindow", "Initial values"))
        self.initialALabel.setText(_translate("MainWindow", "0"))
        self.initialBLabel.setText(_translate("MainWindow", "0"))
        self.initialSigmaLabel.setText(_translate("MainWindow", "0"))
        self.estimatedLabel.setText(_translate("MainWindow", "Estimated"))
        self.estimatedALabel.setText(_translate("MainWindow", "0"))
        self.estimatedBLabel.setText(_translate("MainWindow", "0"))
        self.estimatedSigmaLabel.setText(_translate("MainWindow", "0"))