import sys
from PyQt6 import QtCore,QtGui, QtWidgets #, QtOpenGLWidgets
import pyqtgraph.opengl as gl
from ui_files import mainwindow
from HolePlateMaker import NumpyArrayToHolePlate

import numpy as np
from stl import mesh

import json

class app_1(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):

        self.colorlist = [QtGui.QColor(70,70,70),\
                QtGui.QColor(96,240,168),\
                QtGui.QColor(240,168,96),\
                QtGui.QColor(240,96,96),\
                QtGui.QColor(168,96,240),\
                QtGui.QColor(96,240,240),\
                QtGui.QColor(240,240,96),\
                QtGui.QColor(96,96,240),\
                QtGui.QColor(0,255,0),\
                ]
        self.colorlist2 = [(255/255,255/255,255/255,1),\
                (96/(255*1.5),240/(255*1.5),168/(255*1.5),1),\
                (240/(255*1.5),168/(255*1.5),96/(255*1.5),1),\
                (240/(255*1.5),96/(255*1.5),96/(255*1.5),1),\
                (168/(255*1.5),96/(255*1.5),240/(255*1.5),1),\
                (96/(255*1.5),240/(255*1.5),240/(255*1.5),1),\
                (240/(255*1.5),240/(255*1.5),96/(255*1.5),1),\
                (96/(255*1.5),96/(255*1.5),240/(255*1.5),1),\
                (0/(255*1.5),255/(255*1.5),0/(255*1.5),1),\
                ]

        super(app_1,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ProtoLotus")
        self.pushButton.clicked.connect(self.on_push_b1)
        self.tableWidget.cellClicked.connect(self.on_clickcell)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)        

        self.initMenuAndToolbar()

        self.initTableValue()
        axis = gl.GLGridItem()
        axis.setSpacing(x=1,y=1,z=1)
        self.openGLWidget.addItem(axis)

        self.holePatternCombobox.addItems(['3mm', '4.8mm'])
        self.holePatternCombobox.setCurrentIndex(0)
        self.holePatternCombobox.currentIndexChanged.connect(self.changeIndex)

        self.OPlist = []

    @QtCore.pyqtSlot()
    def on_push_b1(self):
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"~/.", ("STL file (*.stl)"))
        if filepath[0] != "":
            datas = self.getTableValue()
            datas = np.array(datas)

            curMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(datas,self.holePatternCombobox.currentText())
            curMesh.save(filepath[0])
            QtWidgets.QMessageBox.information(self, "file",f"STLファイルの出力が完了しました。\n出力先:{filepath[0]}")

    def changeIndex(self,index):
        self.deleteAllShowMesh()
        self.changeAllOPType(self.holePatternCombobox.currentText())
        self.addAllShowMesh()

    def initTableValue(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(j,i,QtWidgets.QTableWidgetItem("0"))
                self.tableWidget.item(j,i).setBackground(\
                    self.colorlist[0])

    def setTableValue(self,data):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(j,i,QtWidgets.QTableWidgetItem(f"{data[j][i]}"))
                self.tableWidget.item(j,i).setBackground(\
                    self.colorlist[data[j][i]])

    def getTableValue(self):
        datas = []
        for i in range(self.tableWidget.columnCount()):
            row = []
            for j in range(self.tableWidget.rowCount()):
                row.append(int(self.tableWidget.item(j,i).text(),10))
            datas.append(row)
        return datas

    def on_clickcell(self,row,column):
        if self.tableWidget.item(row,column):

            if int(self.tableWidget.item(row,column).text(),10) >= 2:
                newItem = QtWidgets.QTableWidgetItem("0")
            else:
                newItem = QtWidgets.QTableWidgetItem(f"{int(self.tableWidget.item(row,column).text(),10) + 1}")
            
            #print(f"{int(self.tableWidget.item(row,column).text(),10) + 1}")
            self.tableWidget.setItem(row,column,newItem)
        else:
            self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem("0"))
        
        self.tableWidget.item(row,column).setBackground(\
            self.colorlist[int(self.tableWidget.item(row,column).text(),10)])

        datas = self.getTableValue()
        datas = np.array(datas)

        if int(self.tableWidget.item(row,column).text(),10)==1:
            addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(datas,\
                self.holePatternCombobox.currentText(),\
                self.colorlist2,self.OPlist,row,column)
            self.addShowMesh(addData.glMesh)

        elif int(self.tableWidget.item(row,column).text(),10)==0:
            deleteData,self.OPlist = NumpyArrayToHolePlate.GLViewDataPop(datas,\
                self.holePatternCombobox.currentText(),\
                self.colorlist2,self.OPlist,row,column)
            self.deleteShowMesh(deleteData.glMesh)

        else:
            afterData,beforeData,self.OPlist = NumpyArrayToHolePlate.GLViewDataChange(datas,\
                self.holePatternCombobox.currentText(),\
                self.colorlist2,self.OPlist,row,column)
            self.deleteShowMesh(beforeData.glMesh)
            self.addShowMesh(afterData.glMesh)

    def initMenuAndToolbar(self):
        fileOpenAction = QtGui.QAction(QtGui.QIcon('icon/folderopen.png'), 'Open', self)
        fileOpenAction.setShortcut('Ctrl+O')
        fileOpenAction.triggered.connect(self.openSettingFile)
        self.menufiles.addAction(fileOpenAction)
        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(fileOpenAction)

        fileSaveAction = QtGui.QAction(QtGui.QIcon('icon/savefloppy.png'), 'Save', self)
        fileSaveAction.setShortcut('Ctrl+S')
        fileSaveAction.triggered.connect(self.saveSettingFile)
        self.menufiles.addAction(fileSaveAction)
        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(fileSaveAction)

    def saveSettingFile(self):
        datas = self.getTableValue()
        type = self.holePatternCombobox.currentText()

        filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"~/.", ("json file (*.json)"))
        if filepath[0] != "":
            datas = self.getTableValue()
            type = self.holePatternCombobox.currentText()

            with open(filepath[0], 'w') as outfile:
                json.dump({'datas':datas,'type':type},outfile)
                QtWidgets.QMessageBox.information(self, "file",f"設定ファイルの出力が完了しました。\n出力先:{filepath[0]}")


    def openSettingFile(self):
        print("open file")
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"~/.", ("json file (*.json)"))

        if filepath[0] != "":
            with open(filepath[0], 'r') as json_file:
                json_data = json.load(json_file)
                datas = json_data['datas']
                type = json_data['type']
                self.setTableValue(datas)
                self.holePatternCombobox.setCurrentText(type)
                
                datas = self.getTableValue()
                datas = np.array(datas)

                for i in range(self.tableWidget.columnCount()):
                    for j in range(self.tableWidget.rowCount()):
                        if datas[i][j] != 0:
                            addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(datas,\
                                self.holePatternCombobox.currentText(),\
                                self.colorlist2,self.OPlist,j,i)
                            self.addShowMesh(addData.glMesh)

    def deleteShowMesh(self,deleteData):
        self.openGLWidget.removeItem(deleteData)
    
    def addShowMesh(self,addData):
        self.openGLWidget.addItem(addData)

    def deleteAllShowMesh(self):
        for i in range(len(self.OPlist)):
            self.openGLWidget.removeItem(self.OPlist[i].glMesh)

    def addAllShowMesh(self):
        for i in range(len(self.OPlist)):
            self.openGLWidget.addItem(self.OPlist[i].glMesh)
    
    def changeAllOPType(self,type):
        for i in range(len(self.OPlist)):
            self.OPlist[i].changeType(type) 

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid=app_1()
    wid.show()
    sys.exit(app.exec())