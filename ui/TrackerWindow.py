# Form implementation generated from reading ui file 'ui/TrackerWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1041, 753)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 247, 729))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.localport = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.localport.setObjectName("localport")
        self.localport.setColumnCount(2)
        self.localport.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.localport.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.localport.setHorizontalHeaderItem(1, item)
        self.localport.horizontalHeader().setVisible(True)
        self.localport.horizontalHeader().setCascadingSectionResizes(False)
        self.localport.horizontalHeader().setDefaultSectionSize(125)
        self.localport.horizontalHeader().setSortIndicatorShown(True)
        self.localport.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.localport, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 248, 729))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tracker_ipport = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tracker_ipport.setObjectName("tracker_ipport")
        self.tracker_ipport.setColumnCount(2)
        self.tracker_ipport.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tracker_ipport.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tracker_ipport.setHorizontalHeaderItem(1, item)
        self.tracker_ipport.horizontalHeader().setSortIndicatorShown(True)
        self.tracker_ipport.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tracker_ipport)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(Form)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 247, 729))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.peers = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.peers.setObjectName("peers")
        self.peers.setColumnCount(2)
        self.peers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.peers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.peers.setHorizontalHeaderItem(1, item)
        self.peers.horizontalHeader().setSortIndicatorShown(True)
        self.peers.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.peers)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.addWidget(self.scrollArea_3)
        self.scrollArea_4 = QtWidgets.QScrollArea(Form)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 248, 729))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.type_num = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_4)
        self.type_num.setObjectName("type_num")
        self.type_num.setColumnCount(2)
        self.type_num.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.type_num.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.type_num.setHorizontalHeaderItem(1, item)
        self.type_num.horizontalHeader().setDefaultSectionSize(110)
        self.type_num.horizontalHeader().setSortIndicatorShown(True)
        self.type_num.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.type_num)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout.addWidget(self.scrollArea_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "localport"))
        item = self.localport.horizontalHeaderItem(0)
        item.setText(_translate("Form", "port"))
        item = self.localport.horizontalHeaderItem(1)
        item.setText(_translate("Form", "num"))
        self.label_2.setText(_translate("Form", "tracker_ipport"))
        item = self.tracker_ipport.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ipport"))
        item = self.tracker_ipport.horizontalHeaderItem(1)
        item.setText(_translate("Form", "num"))
        self.label_3.setText(_translate("Form", "peers"))
        item = self.peers.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ip"))
        item = self.peers.horizontalHeaderItem(1)
        item.setText(_translate("Form", "port"))
        self.label_4.setText(_translate("Form", "type_num"))
        item = self.type_num.horizontalHeaderItem(0)
        item.setText(_translate("Form", "type"))
        item = self.type_num.horizontalHeaderItem(1)
        item.setText(_translate("Form", "num"))
