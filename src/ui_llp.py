# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\LLP\src\llp.ui'
#
# Created: Fri Jan 27 11:28:13 2012
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(758, 174)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(758, 174))
        MainWindow.setMaximumSize(QtCore.QSize(758, 174))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.volumeSlider.setMaximumSize(QtCore.QSize(44, 10000))
        self.volumeSlider.setMaximumVolume(1.0)
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setMuteVisible(True)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.verticalLayout.addWidget(self.volumeSlider)
        self.openButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setMinimumSize(QtCore.QSize(44, 40))
        self.openButton.setMaximumSize(QtCore.QSize(44, 40))
        self.openButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Open")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon)
        self.openButton.setIconSize(QtCore.QSize(32, 32))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.verticalLayout.addWidget(self.openButton)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.markFrame = QtGui.QFrame(self.centralwidget)
        self.markFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.markFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.markFrame.setObjectName(_fromUtf8("markFrame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.markFrame)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.markButton = QtGui.QPushButton(self.markFrame)
        self.markButton.setObjectName(_fromUtf8("markButton"))
        self.verticalLayout_5.addWidget(self.markButton)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.prevMarkButton = QtGui.QPushButton(self.markFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevMarkButton.sizePolicy().hasHeightForWidth())
        self.prevMarkButton.setSizePolicy(sizePolicy)
        self.prevMarkButton.setMinimumSize(QtCore.QSize(28, 24))
        self.prevMarkButton.setMaximumSize(QtCore.QSize(28, 24))
        self.prevMarkButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/PreviousMark")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevMarkButton.setIcon(icon1)
        self.prevMarkButton.setObjectName(_fromUtf8("prevMarkButton"))
        self.horizontalLayout_7.addWidget(self.prevMarkButton)
        self.nextMarkButton = QtGui.QPushButton(self.markFrame)
        self.nextMarkButton.setMinimumSize(QtCore.QSize(28, 24))
        self.nextMarkButton.setMaximumSize(QtCore.QSize(28, 24))
        self.nextMarkButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/NextMark")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextMarkButton.setIcon(icon2)
        self.nextMarkButton.setObjectName(_fromUtf8("nextMarkButton"))
        self.horizontalLayout_7.addWidget(self.nextMarkButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        spacerItem = QtGui.QSpacerItem(20, 90, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_10.addWidget(self.markFrame)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.markView = QtGui.QGraphicsView(self.centralwidget)
        self.markView.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markView.sizePolicy().hasHeightForWidth())
        self.markView.setSizePolicy(sizePolicy)
        self.markView.setMinimumSize(QtCore.QSize(394, 104))
        self.markView.setMaximumSize(QtCore.QSize(394, 104))
        self.markView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.markView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.markView.setObjectName(_fromUtf8("markView"))
        self.verticalLayout_3.addWidget(self.markView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.controlsFrame = QtGui.QFrame(self.centralwidget)
        self.controlsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.controlsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.controlsFrame.setObjectName(_fromUtf8("controlsFrame"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.controlsFrame)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.startButton = QtGui.QPushButton(self.controlsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(44, 40))
        self.startButton.setMaximumSize(QtCore.QSize(44, 40))
        self.startButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Start")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon3)
        self.startButton.setIconSize(QtCore.QSize(32, 32))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout_9.addWidget(self.startButton)
        self.rewindButton = QtGui.QPushButton(self.controlsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rewindButton.sizePolicy().hasHeightForWidth())
        self.rewindButton.setSizePolicy(sizePolicy)
        self.rewindButton.setMinimumSize(QtCore.QSize(44, 40))
        self.rewindButton.setMaximumSize(QtCore.QSize(44, 40))
        self.rewindButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Rewind")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rewindButton.setIcon(icon4)
        self.rewindButton.setIconSize(QtCore.QSize(32, 32))
        self.rewindButton.setObjectName(_fromUtf8("rewindButton"))
        self.horizontalLayout_9.addWidget(self.rewindButton)
        self.playButton = QtGui.QPushButton(self.controlsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QtCore.QSize(44, 40))
        self.playButton.setMaximumSize(QtCore.QSize(44, 40))
        self.playButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Play")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon5)
        self.playButton.setIconSize(QtCore.QSize(32, 32))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout_9.addWidget(self.playButton)
        self.forwardButton = QtGui.QPushButton(self.controlsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardButton.sizePolicy().hasHeightForWidth())
        self.forwardButton.setSizePolicy(sizePolicy)
        self.forwardButton.setMinimumSize(QtCore.QSize(44, 40))
        self.forwardButton.setMaximumSize(QtCore.QSize(44, 40))
        self.forwardButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Forward")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forwardButton.setIcon(icon6)
        self.forwardButton.setIconSize(QtCore.QSize(32, 32))
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.horizontalLayout_9.addWidget(self.forwardButton)
        self.endButton = QtGui.QPushButton(self.controlsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endButton.sizePolicy().hasHeightForWidth())
        self.endButton.setSizePolicy(sizePolicy)
        self.endButton.setMinimumSize(QtCore.QSize(44, 40))
        self.endButton.setMaximumSize(QtCore.QSize(44, 40))
        self.endButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/End")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.endButton.setIcon(icon7)
        self.endButton.setIconSize(QtCore.QSize(32, 32))
        self.endButton.setObjectName(_fromUtf8("endButton"))
        self.horizontalLayout_9.addWidget(self.endButton)
        self.horizontalLayout.addWidget(self.controlsFrame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.positionIndicator = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.positionIndicator.sizePolicy().hasHeightForWidth())
        self.positionIndicator.setSizePolicy(sizePolicy)
        self.positionIndicator.setMinimumSize(QtCore.QSize(0, 20))
        self.positionIndicator.setMaximumSize(QtCore.QSize(16777215, 20))
        self.positionIndicator.setObjectName(_fromUtf8("positionIndicator"))
        self.horizontalLayout_2.addWidget(self.positionIndicator)
        self.dividerLabel = QtGui.QLabel(self.centralwidget)
        self.dividerLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.dividerLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dividerLabel.setObjectName(_fromUtf8("dividerLabel"))
        self.horizontalLayout_2.addWidget(self.dividerLabel)
        self.totalLabel = QtGui.QLabel(self.centralwidget)
        self.totalLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.totalLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.totalLabel.setObjectName(_fromUtf8("totalLabel"))
        self.horizontalLayout_2.addWidget(self.totalLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.rightFrame = QtGui.QFrame(self.centralwidget)
        self.rightFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.rightFrame.setObjectName(_fromUtf8("rightFrame"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.rightFrame)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.setBeginButton = QtGui.QPushButton(self.rightFrame)
        self.setBeginButton.setMinimumSize(QtCore.QSize(60, 23))
        self.setBeginButton.setObjectName(_fromUtf8("setBeginButton"))
        self.horizontalLayout_6.addWidget(self.setBeginButton)
        spacerItem3 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.setEndButton = QtGui.QPushButton(self.rightFrame)
        self.setEndButton.setMinimumSize(QtCore.QSize(60, 23))
        self.setEndButton.setObjectName(_fromUtf8("setEndButton"))
        self.horizontalLayout_6.addWidget(self.setEndButton)
        spacerItem4 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem5 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.loopButton = QtGui.QPushButton(self.rightFrame)
        self.loopButton.setMinimumSize(QtCore.QSize(60, 23))
        self.loopButton.setMaximumSize(QtCore.QSize(109, 23))
        self.loopButton.setCheckable(True)
        self.loopButton.setObjectName(_fromUtf8("loopButton"))
        self.horizontalLayout_5.addWidget(self.loopButton)
        spacerItem6 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.selectionButton = QtGui.QPushButton(self.rightFrame)
        self.selectionButton.setMinimumSize(QtCore.QSize(60, 23))
        self.selectionButton.setMaximumSize(QtCore.QSize(109, 23))
        self.selectionButton.setCheckable(True)
        self.selectionButton.setObjectName(_fromUtf8("selectionButton"))
        self.horizontalLayout_5.addWidget(self.selectionButton)
        spacerItem7 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem8 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.countButton = QtGui.QPushButton(self.rightFrame)
        self.countButton.setMinimumSize(QtCore.QSize(75, 23))
        self.countButton.setCheckable(False)
        self.countButton.setFlat(False)
        self.countButton.setObjectName(_fromUtf8("countButton"))
        self.horizontalLayout_4.addWidget(self.countButton)
        spacerItem9 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.beatsBox = QtGui.QSpinBox(self.rightFrame)
        self.beatsBox.setMaximumSize(QtCore.QSize(65, 20))
        self.beatsBox.setMaximum(16)
        self.beatsBox.setObjectName(_fromUtf8("beatsBox"))
        self.horizontalLayout_3.addWidget(self.beatsBox)
        self.label = QtGui.QLabel(self.rightFrame)
        self.label.setMaximumSize(QtCore.QSize(10, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.bpmBox = QtGui.QSpinBox(self.rightFrame)
        self.bpmBox.setMaximumSize(QtCore.QSize(65, 20))
        self.bpmBox.setMinimum(60)
        self.bpmBox.setMaximum(300)
        self.bpmBox.setProperty(_fromUtf8("value"), 120)
        self.bpmBox.setObjectName(_fromUtf8("bpmBox"))
        self.horizontalLayout_3.addWidget(self.bpmBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.rightFrame)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPlay = QtGui.QAction(MainWindow)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.actionMark = QtGui.QAction(MainWindow)
        self.actionMark.setObjectName(_fromUtf8("actionMark"))
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionEnd = QtGui.QAction(MainWindow)
        self.actionEnd.setObjectName(_fromUtf8("actionEnd"))
        self.actionPreviousMark = QtGui.QAction(MainWindow)
        self.actionPreviousMark.setObjectName(_fromUtf8("actionPreviousMark"))
        self.actionNextMark = QtGui.QAction(MainWindow)
        self.actionNextMark.setObjectName(_fromUtf8("actionNextMark"))
        self.actionCountIn = QtGui.QAction(MainWindow)
        self.actionCountIn.setObjectName(_fromUtf8("actionCountIn"))
        self.actionMark_2 = QtGui.QAction(MainWindow)
        self.actionMark_2.setObjectName(_fromUtf8("actionMark_2"))
        self.actionSelection = QtGui.QAction(MainWindow)
        self.actionSelection.setObjectName(_fromUtf8("actionSelection"))
        self.actionLoop = QtGui.QAction(MainWindow)
        self.actionLoop.setObjectName(_fromUtf8("actionLoop"))
        self.actionToggleMute = QtGui.QAction(MainWindow)
        self.actionToggleMute.setObjectName(_fromUtf8("actionToggleMute"))
        self.actionVolumeUp = QtGui.QAction(MainWindow)
        self.actionVolumeUp.setObjectName(_fromUtf8("actionVolumeUp"))
        self.actionVolumeDown = QtGui.QAction(MainWindow)
        self.actionVolumeDown.setObjectName(_fromUtf8("actionVolumeDown"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.openButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionOpen.trigger)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.playButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionPlay.trigger)
        QtCore.QObject.connect(self.markButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionMark.trigger)
        QtCore.QObject.connect(self.nextMarkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionNextMark.trigger)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionHome.trigger)
        QtCore.QObject.connect(self.endButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionEnd.trigger)
        QtCore.QObject.connect(self.countButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionCountIn.trigger)
        QtCore.QObject.connect(self.actionMark_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.actionMark.trigger)
        QtCore.QObject.connect(self.prevMarkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionPreviousMark.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Listen, Learn, Play", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeSlider.setToolTip(QtGui.QApplication.translate("MainWindow", "Mute [Esc]\n"
"Volume Up [+]\n"
"Volume Down [-]", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Open a new music file</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Ctrl+N]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.markButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Add/delete a mark at the current position</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Return]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.markButton.setText(QtGui.QApplication.translate("MainWindow", "Mark", None, QtGui.QApplication.UnicodeUTF8))
        self.prevMarkButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Jump to the previous mark</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Up]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.nextMarkButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Jump to the next mark</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Down]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To Start</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Home]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rewindButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Rewind", None, QtGui.QApplication.UnicodeUTF8))
        self.playButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Play</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Space]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.forwardButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Fast Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.endButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To End</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[End]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.positionIndicator.setText(QtGui.QApplication.translate("MainWindow", "--", None, QtGui.QApplication.UnicodeUTF8))
        self.dividerLabel.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.totalLabel.setText(QtGui.QApplication.translate("MainWindow", "--", None, QtGui.QApplication.UnicodeUTF8))
        self.setBeginButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set the beginning of the selection</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.setBeginButton.setText(QtGui.QApplication.translate("MainWindow", "Begin", None, QtGui.QApplication.UnicodeUTF8))
        self.setEndButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set the end of the selection</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.setEndButton.setText(QtGui.QApplication.translate("MainWindow", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.loopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Repeat endlessly or play once</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[L]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.loopButton.setText(QtGui.QApplication.translate("MainWindow", "Once", None, QtGui.QApplication.UnicodeUTF8))
        self.selectionButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Switch between playing song and selection</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[S]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectionButton.setText(QtGui.QApplication.translate("MainWindow", "Song", None, QtGui.QApplication.UnicodeUTF8))
        self.countButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Count in to playing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[Ctril+Space]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.countButton.setText(QtGui.QApplication.translate("MainWindow", "Count In", None, QtGui.QApplication.UnicodeUTF8))
        self.beatsBox.setSuffix(QtGui.QApplication.translate("MainWindow", " beats", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "at", None, QtGui.QApplication.UnicodeUTF8))
        self.bpmBox.setSuffix(QtGui.QApplication.translate("MainWindow", " bpm", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("MainWindow", "play", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setShortcut(QtGui.QApplication.translate("MainWindow", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMark.setText(QtGui.QApplication.translate("MainWindow", "mark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMark.setShortcut(QtGui.QApplication.translate("MainWindow", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setText(QtGui.QApplication.translate("MainWindow", "home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setShortcut(QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnd.setText(QtGui.QApplication.translate("MainWindow", "end", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnd.setShortcut(QtGui.QApplication.translate("MainWindow", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreviousMark.setText(QtGui.QApplication.translate("MainWindow", "previousMark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreviousMark.setShortcut(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNextMark.setText(QtGui.QApplication.translate("MainWindow", "nextMark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNextMark.setShortcut(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCountIn.setText(QtGui.QApplication.translate("MainWindow", "countIn", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCountIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMark_2.setText(QtGui.QApplication.translate("MainWindow", "mark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMark_2.setShortcut(QtGui.QApplication.translate("MainWindow", "Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setText(QtGui.QApplication.translate("MainWindow", "selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setShortcut(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoop.setText(QtGui.QApplication.translate("MainWindow", "loop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoop.setShortcut(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleMute.setText(QtGui.QApplication.translate("MainWindow", "toggleMute", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleMute.setShortcut(QtGui.QApplication.translate("MainWindow", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVolumeUp.setText(QtGui.QApplication.translate("MainWindow", "volumeUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVolumeUp.setShortcut(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVolumeDown.setText(QtGui.QApplication.translate("MainWindow", "volumeDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVolumeDown.setShortcut(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import phonon
import llp_rc
