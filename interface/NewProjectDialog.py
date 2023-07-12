# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class NewProjectUi(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.content = QFrame(Dialog)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.contentLayout = QVBoxLayout(self.content)
        self.contentLayout.setSpacing(0)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.projectNameLabel = QLabel(self.content)
        self.projectNameLabel.setObjectName(u"projectNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.projectNameLabel)

        self.projectNameInput = QLineEdit(self.content)
        self.projectNameInput.setObjectName(u"projectNameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.projectNameInput)

        self.projectAuthorLabel = QLabel(self.content)
        self.projectAuthorLabel.setObjectName(u"projectAuthorLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.projectAuthorLabel)

        self.projectFolderLabel = QLabel(self.content)
        self.projectFolderLabel.setObjectName(u"projectFolderLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.projectFolderLabel)

        self.maxClusterLabel = QLabel(self.content)
        self.maxClusterLabel.setObjectName(u"maxClusterLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.maxClusterLabel)

        self.clusterInput = QLineEdit(self.content)
        self.clusterInput.setObjectName(u"clusterInput")
        self.clusterInput.setMaxLength(4)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.clusterInput)

        self.projectAuthorInput = QLineEdit(self.content)
        self.projectAuthorInput.setObjectName(u"projectAuthorInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.projectAuthorInput)

        self.projectFolderFrame = QFrame(self.content)
        self.projectFolderFrame.setObjectName(u"projectFolderFrame")
        self.projectFolderFrame.setFrameShape(QFrame.StyledPanel)
        self.projectFolderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.projectFolderFrame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.projectFolderInput = QLineEdit(self.projectFolderFrame)
        self.projectFolderInput.setObjectName(u"projectFolderInput")

        self.horizontalLayout.addWidget(self.projectFolderInput)

        self.browseBtn = QToolButton(self.projectFolderFrame)
        self.browseBtn.setObjectName(u"browseBtn")

        self.horizontalLayout.addWidget(self.browseBtn)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.projectFolderFrame)

        self.descLabel = QLabel(self.content)
        self.descLabel.setObjectName(u"descLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.descLabel)

        self.textEdit = QTextEdit(self.content)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit)


        self.contentLayout.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.content, 0, Qt.AlignVCenter)

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
        self.projectNameLabel.setText(QCoreApplication.translate("Dialog", u"Project Name: ", None))
        self.projectAuthorLabel.setText(QCoreApplication.translate("Dialog", u"Project Author: ", None))
        self.projectFolderLabel.setText(QCoreApplication.translate("Dialog", u"Project Folder: ", None))
        self.maxClusterLabel.setText(QCoreApplication.translate("Dialog", u"Max Cluster Size: ", None))
        self.browseBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.descLabel.setText(QCoreApplication.translate("Dialog", u"Desc", None))
    # retranslateUi

