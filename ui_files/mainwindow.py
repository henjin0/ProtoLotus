# Form implementation generated from reading ui file 'ui_files/MainWindow2.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openGLWidget = GLViewWidget(self.centralwidget)
        self.openGLWidget.setMaximumSize(QtCore.QSize(460, 16777215))
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout.addWidget(self.openGLWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(472, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.holePatternCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.holePatternCombobox.setObjectName("holePatternCombobox")
        self.holePatternCombobox.addItem("")
        self.holePatternCombobox.addItem("")
        self.verticalLayout_2.addWidget(self.holePatternCombobox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.maxXScaleComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.maxXScaleComboBox.setObjectName("maxXScaleComboBox")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.maxXScaleComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.maxXScaleComboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.maxYScaleComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.maxYScaleComboBox.setObjectName("maxYScaleComboBox")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.maxYScaleComboBox.addItem("")
        self.verticalLayout_4.addWidget(self.maxYScaleComboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 24))
        self.menubar.setObjectName("menubar")
        self.menufiles = QtWidgets.QMenu(self.menubar)
        self.menufiles.setObjectName("menufiles")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionsave = QtGui.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionload = QtGui.QAction(MainWindow)
        self.actionload.setObjectName("actionload")
        self.actionexit = QtGui.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menufiles.addAction(self.actionsave)
        self.menufiles.addAction(self.actionload)
        self.menufiles.addAction(self.actionexit)
        self.menubar.addAction(self.menufiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Output STL file"))
        self.label.setText(_translate("MainWindow", "hole pattern"))
        self.holePatternCombobox.setItemText(0, _translate("MainWindow", "3mm"))
        self.holePatternCombobox.setItemText(1, _translate("MainWindow", "4.8mm"))
        self.label_2.setText(_translate("MainWindow", "max x scale"))
        self.maxXScaleComboBox.setItemText(0, _translate("MainWindow", "10"))
        self.maxXScaleComboBox.setItemText(1, _translate("MainWindow", "15"))
        self.maxXScaleComboBox.setItemText(2, _translate("MainWindow", "20"))
        self.maxXScaleComboBox.setItemText(3, _translate("MainWindow", "25"))
        self.maxXScaleComboBox.setItemText(4, _translate("MainWindow", "30"))
        self.maxXScaleComboBox.setItemText(5, _translate("MainWindow", "35"))
        self.maxXScaleComboBox.setItemText(6, _translate("MainWindow", "40"))
        self.maxXScaleComboBox.setItemText(7, _translate("MainWindow", "45"))
        self.maxXScaleComboBox.setItemText(8, _translate("MainWindow", "50"))
        self.maxXScaleComboBox.setItemText(9, _translate("MainWindow", "55"))
        self.maxXScaleComboBox.setItemText(10, _translate("MainWindow", "60"))
        self.maxXScaleComboBox.setItemText(11, _translate("MainWindow", "65"))
        self.maxXScaleComboBox.setItemText(12, _translate("MainWindow", "70"))
        self.maxXScaleComboBox.setItemText(13, _translate("MainWindow", "75"))
        self.maxXScaleComboBox.setItemText(14, _translate("MainWindow", "80"))
        self.maxXScaleComboBox.setItemText(15, _translate("MainWindow", "85"))
        self.maxXScaleComboBox.setItemText(16, _translate("MainWindow", "90"))
        self.maxXScaleComboBox.setItemText(17, _translate("MainWindow", "95"))
        self.maxXScaleComboBox.setItemText(18, _translate("MainWindow", "100"))
        self.label_3.setText(_translate("MainWindow", "max y scale"))
        self.maxYScaleComboBox.setItemText(0, _translate("MainWindow", "10"))
        self.maxYScaleComboBox.setItemText(1, _translate("MainWindow", "15"))
        self.maxYScaleComboBox.setItemText(2, _translate("MainWindow", "20"))
        self.maxYScaleComboBox.setItemText(3, _translate("MainWindow", "25"))
        self.maxYScaleComboBox.setItemText(4, _translate("MainWindow", "30"))
        self.maxYScaleComboBox.setItemText(5, _translate("MainWindow", "35"))
        self.maxYScaleComboBox.setItemText(6, _translate("MainWindow", "40"))
        self.maxYScaleComboBox.setItemText(7, _translate("MainWindow", "45"))
        self.maxYScaleComboBox.setItemText(8, _translate("MainWindow", "50"))
        self.maxYScaleComboBox.setItemText(9, _translate("MainWindow", "55"))
        self.maxYScaleComboBox.setItemText(10, _translate("MainWindow", "60"))
        self.maxYScaleComboBox.setItemText(11, _translate("MainWindow", "65"))
        self.maxYScaleComboBox.setItemText(12, _translate("MainWindow", "70"))
        self.maxYScaleComboBox.setItemText(13, _translate("MainWindow", "75"))
        self.maxYScaleComboBox.setItemText(14, _translate("MainWindow", "80"))
        self.maxYScaleComboBox.setItemText(15, _translate("MainWindow", "85"))
        self.maxYScaleComboBox.setItemText(16, _translate("MainWindow", "90"))
        self.maxYScaleComboBox.setItemText(17, _translate("MainWindow", "95"))
        self.maxYScaleComboBox.setItemText(18, _translate("MainWindow", "100"))
        self.menufiles.setTitle(_translate("MainWindow", "files"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionload.setText(_translate("MainWindow", "load"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
from pyqtgraph.opengl import GLViewWidget
