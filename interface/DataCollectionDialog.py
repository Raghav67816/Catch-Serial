# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataCollectionDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class DataCollecUi(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QSize(300, 200))
        Dialog.setMaximumSize(QSize(300, 200))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contentContainer = QFrame(Dialog)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setFrameShape(QFrame.StyledPanel)
        self.contentContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 40)
        self.rBtnContainer = QFrame(self.contentContainer)
        self.rBtnContainer.setObjectName(u"rBtnContainer")
        self.rBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.rBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.rBtnContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.storeDataRBtn = QRadioButton(self.rBtnContainer)
        self.storeDataRBtn.setObjectName(u"storeDataRBtn")

        self.horizontalLayout.addWidget(self.storeDataRBtn)

        self.monitorOnlyRBtn = QRadioButton(self.rBtnContainer)
        self.monitorOnlyRBtn.setObjectName(u"monitorOnlyRBtn")

        self.horizontalLayout.addWidget(self.monitorOnlyRBtn)


        self.verticalLayout_2.addWidget(self.rBtnContainer, 0, Qt.AlignTop)

        self.dc_container = QFormLayout()
        self.dc_container.setObjectName(u"dc_container")
        self.dc_container.setHorizontalSpacing(50)
        self.dc_container.setVerticalSpacing(10)
        self.dc_container.setContentsMargins(-1, 0, -1, 0)
        self.portLabel = QLabel(self.contentContainer)
        self.portLabel.setObjectName(u"portLabel")

        self.dc_container.setWidget(0, QFormLayout.LabelRole, self.portLabel)

        self.portBox = QComboBox(self.contentContainer)
        self.portBox.addItem("")
        self.portBox.setObjectName(u"portBox")

        self.dc_container.setWidget(0, QFormLayout.FieldRole, self.portBox)

        self.baudRateLabel = QLabel(self.contentContainer)
        self.baudRateLabel.setObjectName(u"baudRateLabel")

        self.dc_container.setWidget(1, QFormLayout.LabelRole, self.baudRateLabel)

        self.baudRateInput = QLineEdit(self.contentContainer)
        self.baudRateInput.setObjectName(u"baudRateInput")

        self.dc_container.setWidget(1, QFormLayout.FieldRole, self.baudRateInput)


        self.verticalLayout_2.addLayout(self.dc_container)


        self.verticalLayout.addWidget(self.contentContainer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.storeDataRBtn.setText(QCoreApplication.translate("Dialog", u"Store Data", None))
        self.monitorOnlyRBtn.setText(QCoreApplication.translate("Dialog", u"Monitor Only", None))
        self.portLabel.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.portBox.setItemText(0, QCoreApplication.translate("Dialog", u"--Select Port--", None))

        self.baudRateLabel.setText(QCoreApplication.translate("Dialog", u"Baud Rate", None))
    # retranslateUi

