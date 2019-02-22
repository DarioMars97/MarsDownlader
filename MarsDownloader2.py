# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MarsDownloader2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 226)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/index.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 26, 243, 187))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_location = QtWidgets.QLineEdit(self.widget)
        self.save_location.setObjectName("save_location")
        self.horizontalLayout.addWidget(self.save_location)
        self.save_location_button = QtWidgets.QPushButton(self.widget)
        self.save_location_button.setObjectName("save_location_button")
        self.horizontalLayout.addWidget(self.save_location_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.download_button = QtWidgets.QPushButton(self.widget)
        self.download_button.setObjectName("download_button")
        self.verticalLayout_2.addWidget(self.download_button)
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setObjectName("close_button")
        self.verticalLayout_2.addWidget(self.close_button)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.credits = QtWidgets.QLabel(self.widget)
        self.credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.credits.setObjectName("credits")
        self.verticalLayout.addWidget(self.credits)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MarsDownloader"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "URL"))
        self.save_location.setPlaceholderText(_translate("Dialog", "Save Location"))
        self.save_location_button.setText(_translate("Dialog", "..."))
        self.download_button.setText(_translate("Dialog", "Download"))
        self.close_button.setText(_translate("Dialog", "Close"))
        self.credits.setText(_translate("Dialog", "Dola credits"))

