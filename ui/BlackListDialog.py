# Form implementation generated from reading ui file 'ui/BlackListDialog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 476)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 661, 411))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 431, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(460, 10, 93, 28))
        self.add.setObjectName("add")
        self.refreshFromServer = QtWidgets.QPushButton(Dialog)
        self.refreshFromServer.setGeometry(QtCore.QRect(562, 10, 111, 28))
        self.refreshFromServer.setObjectName("refreshFromServer")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add.setText(_translate("Dialog", "添加"))
        self.refreshFromServer.setText(_translate("Dialog", "从服务器获取"))
