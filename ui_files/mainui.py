# Form implementation generated from reading ui file 'ui_files/main2.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1231, 671)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        Dialog.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 610, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.openGLWidget = GLViewWidget(Dialog)
        self.openGLWidget.setGeometry(QtCore.QRect(20, 10, 761, 581))
        self.openGLWidget.setObjectName("openGLWidget")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(800, 160, 391, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Save STL"))
from pyqtgraph.opengl import GLViewWidget
