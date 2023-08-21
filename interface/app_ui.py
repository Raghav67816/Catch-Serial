# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMaximumSize(QSize(800, 300))
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        self.actionOpen_Project = QAction(MainWindow)
        self.actionOpen_Project.setObjectName(u"actionOpen_Project")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionApperance = QAction(MainWindow)
        self.actionApperance.setObjectName(u"actionApperance")
        self.actionData_Collection = QAction(MainWindow)
        self.actionData_Collection.setObjectName(u"actionData_Collection")
        self.actionData_Storage = QAction(MainWindow)
        self.actionData_Storage.setObjectName(u"actionData_Storage")
        self.actionAbout_CatchSerial = QAction(MainWindow)
        self.actionAbout_CatchSerial.setObjectName(u"actionAbout_CatchSerial")
        self.actionGuide = QAction(MainWindow)
        self.actionGuide.setObjectName(u"actionGuide")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralLayyout = QVBoxLayout(self.centralwidget)
        self.centralLayyout.setSpacing(0)
        self.centralLayyout.setObjectName(u"centralLayyout")
        self.centralLayyout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.terminal_container = QFrame(self.content)
        self.terminal_container.setObjectName(u"terminal_container")
        self.terminal_container.setMinimumSize(QSize(350, 0))
        self.terminal_container.setMaximumSize(QSize(350, 16777215))
        self.terminal_container.setFrameShape(QFrame.StyledPanel)
        self.terminal_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.terminal_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.terminal = QTextBrowser(self.terminal_container)
        self.terminal.setObjectName(u"terminal")

        self.verticalLayout.addWidget(self.terminal)


        self.horizontalLayout.addWidget(self.terminal_container)

        self.controls_container = QFrame(self.content)
        self.controls_container.setObjectName(u"controls_container")
        self.controls_container.setFrameShape(QFrame.StyledPanel)
        self.controls_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.controls_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.controlsLabel = QLabel(self.controls_container)
        self.controlsLabel.setObjectName(u"controlsLabel")

        self.verticalLayout_3.addWidget(self.controlsLabel, 0, Qt.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.portLabel = QLabel(self.controls_container)
        self.portLabel.setObjectName(u"portLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.portLabel)

        self.baudRateLabel = QLabel(self.controls_container)
        self.baudRateLabel.setObjectName(u"baudRateLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.baudRateLabel)

        self.portBox = QComboBox(self.controls_container)
        self.portBox.setObjectName(u"portBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.portBox)

        self.baudRateInput = QLineEdit(self.controls_container)
        self.baudRateInput.setObjectName(u"baudRateInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.baudRateInput)
        self.formLayout.setSpacing(10)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.btnContainer = QFrame(self.controls_container)
        self.btnContainer.setObjectName(u"btnContainer")
        self.btnContainer.setMinimumSize(QSize(0, 80))
        self.btnContainer.setMaximumSize(QSize(16777215, 80))
        self.btnContainer.setFrameShape(QFrame.StyledPanel)
        self.btnContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.btnContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.recordingLoopBtn = QPushButton(self.btnContainer)
        self.recordingLoopBtn.setObjectName(u"recordingLoopBtn")

        self.verticalLayout_2.addWidget(self.recordingLoopBtn)

        self.clickRecordBtn = QPushButton(self.btnContainer)
        self.clickRecordBtn.setObjectName(u"clickRecordBtn")

        self.verticalLayout_2.addWidget(self.clickRecordBtn)


        self.verticalLayout_3.addWidget(self.btnContainer)


        self.horizontalLayout.addWidget(self.controls_container)


        self.centralLayyout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPreferences = QMenu(self.menubar)
        self.menuPreferences.setObjectName(u"menuPreferences")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPreferences.addAction(self.actionApperance)
        self.menuPreferences.addAction(self.actionData_Collection)
        self.menuHelp.addAction(self.actionAbout_CatchSerial)
        self.menuHelp.addAction(self.actionGuide)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
#if QT_CONFIG(shortcut)
        self.actionNew_Project.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Project.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionApperance.setText(QCoreApplication.translate("MainWindow", u"Set Fields", None))
#if QT_CONFIG(shortcut)
        self.actionApperance.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionData_Collection.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
#if QT_CONFIG(shortcut)
        self.actionData_Collection.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionData_Storage.setText(QCoreApplication.translate("MainWindow", u"Data Storage", None))
#if QT_CONFIG(shortcut)
        self.actionData_Storage.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout_CatchSerial.setText(QCoreApplication.translate("MainWindow", u"About CatchSerial", None))
        self.actionGuide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.controlsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Controls</span></p></body></html>", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Port ", None))
        self.baudRateLabel.setText(QCoreApplication.translate("MainWindow", u"Baud Rate", None))
        self.recordingLoopBtn.setText(QCoreApplication.translate("MainWindow", u"Start Recording", None))
        self.clickRecordBtn.setText(QCoreApplication.translate("MainWindow", u"Click and Record", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

