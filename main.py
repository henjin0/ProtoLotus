import sys,os
from PyQt6 import QtCore,QtGui, QtWidgets #, QtOpenGLWidgets
import pyqtgraph.opengl as gl
from ui_files import mainwindow
from HolePlateMaker import NumpyArrayToHolePlate

import numpy as np
from stl import mesh

import json

def resourcePath(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)

class app_1(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self):

        self.colorlist = [QtGui.QColor(70,70,70),\
                QtGui.QColor(96,240,168),\
                QtGui.QColor(240,168,96),\
                QtGui.QColor(168,96,240),\
                QtGui.QColor(240,96,96),\
                QtGui.QColor(96,240,240),\
                QtGui.QColor(240,240,96),\
                QtGui.QColor(96,96,240),\
                QtGui.QColor(0,255,0),\
                ]
        self.colorlist2 = [(255/255,255/255,255/255,1),\
                (96/(255*1.5),240/(255*1.5),168/(255*1.5),1),\
                (240/(255*1.5),168/(255*1.5),96/(255*1.5),1),\
                (168/(255*1.5),96/(255*1.5),240/(255*1.5),1),\
                (240/(255*1.5),96/(255*1.5),96/(255*1.5),1),\
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

        self.holePatternCombobox.setCurrentIndex(0)
        self.holePatternCombobox.currentIndexChanged.connect(self.changeIndexHolePatternCombobox)

        self.maxXScaleComboBox.setCurrentIndex(0)
        self.maxXScaleComboBox.currentIndexChanged.connect(self.changeIndexMaxXScaleComboBox)

        self.maxYScaleComboBox.setCurrentIndex(0)
        self.maxYScaleComboBox.currentIndexChanged.connect(self.changeIndexMaxYScaleComboBox)

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

    def changeIndexHolePatternCombobox(self,index):
        self.deleteAllShowMesh()
        self.changeAllOPType(self.holePatternCombobox.currentText())
        self.addAllShowMesh()
    
    def changeIndexMaxXScaleComboBox(self,index):
        tempDatas = self.getTableValue()
        tempDatas = np.array(tempDatas)
        columnTemp,rowTemp = np.where(tempDatas != 0)

        if(columnTemp.any()):
            if(np.max(columnTemp) >= int(self.maxXScaleComboBox.currentText())):
                QtWidgets.QMessageBox.information(self, "警告",f"指定した行数よりもモデルが大きいようです。モデルの大きさを調節して再度指定してください。")
                self.maxXScaleComboBox.setCurrentText(f"{self.tableWidget.columnCount()}")
                return

        self.deleteAllShowMesh()
        self.OPlist = []

        self.tableWidget.setColumnCount(int(self.maxXScaleComboBox.currentText()))
        self.initTableValue()
        
        datas = self.getTableValue()
        datas = np.array(datas)

        column,row = np.where(datas != 0)

        for i in range(len(column)):
                addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(datas,\
                    self.holePatternCombobox.currentText(),\
                    self.colorlist2,self.OPlist,row[i],column[i])
                self.addShowMesh(addData.glMesh)
        

    def changeIndexMaxYScaleComboBox(self,index):
        tempDatas = self.getTableValue()
        tempDatas = np.array(tempDatas)
        columnTemp,rowTemp = np.where(tempDatas != 0)

        if(rowTemp.any()):
            if(np.max(rowTemp)) >= int(self.maxYScaleComboBox.currentText()):
                QtWidgets.QMessageBox.information(self, "警告",f"指定した列数よりもモデルが大きいようです。モデルの大きさを調節して再度指定してください。")
                self.maxYScaleComboBox.setCurrentText(f"{self.tableWidget.rowCount()}")
                return
            
        self.deleteAllShowMesh()
        self.OPlist = []

        self.tableWidget.setRowCount(int(self.maxYScaleComboBox.currentText()))
        self.initTableValue()
        
        datas = self.getTableValue()
        datas = np.array(datas)
        column,row = np.where(datas != 0)

        for i in range(len(column)):
            addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(datas,\
                self.holePatternCombobox.currentText(),\
                self.colorlist2,self.OPlist,row[i],column[i])
            self.addShowMesh(addData.glMesh)

    def initTableValue(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                if not (self.tableWidget.item(j,i)):
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

            if int(self.tableWidget.item(row,column).text(),10) >= 3:
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

         # note: 1になった瞬間＝数字のローテーション始まってモデルを新しく追加するとき。
        if int(self.tableWidget.item(row,column).text(),10)==1:
            addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(datas,\
                self.holePatternCombobox.currentText(),\
                self.colorlist2,self.OPlist,row,column)
            self.addShowMesh(addData.glMesh)

        # note: 0になった瞬間＝数字のローテーションが一周してモデルを消さなくてはいけなくなったとき。
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
        
        self.tableWidget.clearSelection()

    def initMenuAndToolbar(self):
        fileOpenAction = QtGui.QAction(QtGui.QIcon(resourcePath('icon/folderopen.png')), 'Open', self)
        fileOpenAction.setShortcut('Ctrl+O')
        fileOpenAction.triggered.connect(self.openSettingFile)
        self.menufiles.addAction(fileOpenAction)
        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(fileOpenAction)

        fileSaveAction = QtGui.QAction(QtGui.QIcon(resourcePath('icon/savefloppy.png')), 'Save', self)
        fileSaveAction.setShortcut('Ctrl+S')
        fileSaveAction.triggered.connect(self.saveSettingFile)
        self.menufiles.addAction(fileSaveAction)
        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(fileSaveAction)

        button0Action = QtGui.QAction(QtGui.QIcon(resourcePath('icon/0.png')), 'fill 0 for all selected cells', self)
        button0Action.setShortcut('Ctrl+0')
        button1Action = QtGui.QAction(QtGui.QIcon(resourcePath('icon/1.png')), 'fill 1 for all selected cells', self)
        button1Action.setShortcut('Ctrl+1')
        button2Action = QtGui.QAction(QtGui.QIcon(resourcePath('icon/2.png')), 'fill 2 for all selected cells', self)
        button2Action.setShortcut('Ctrl+2')
        button3Action = QtGui.QAction(QtGui.QIcon(resourcePath('icon/3.png')), 'fill 3 for all selected cells', self)
        button3Action.setShortcut('Ctrl+3')

        apply0ModelAction = lambda :self.applyModelAction(0)
        button0Action.triggered.connect(apply0ModelAction)
        self.menufiles.addAction(button0Action)
        self.toolbar = self.addToolBar('fill 0 for all selected cells')
        self.toolbar.addAction(button0Action)

        apply1ModelAction = lambda :self.applyModelAction(1)
        button1Action.triggered.connect(apply1ModelAction)
        self.menufiles.addAction(button1Action)
        self.toolbar = self.addToolBar('fill 1 for all selected cells')
        self.toolbar.addAction(button1Action)

        apply2ModelAction = lambda :self.applyModelAction(2)
        button2Action.triggered.connect(apply2ModelAction)
        self.menufiles.addAction(button2Action)
        self.toolbar = self.addToolBar('fill 2 for all selected cells')
        self.toolbar.addAction(button2Action)

        apply3ModelAction = lambda :self.applyModelAction(3)
        button3Action.triggered.connect(apply3ModelAction)
        self.menufiles.addAction(button3Action)
        self.toolbar = self.addToolBar('fill 3 for all selected cells')
        self.toolbar.addAction(button3Action)

    def applyModelAction(self,cellNumber):
        items = self.tableWidget.selectedItems()
        
        if(items==[]):
            return

        temp_tableWidgetDatas = self.getTableValue()
        temp_tableWidgetDatas = np.array(temp_tableWidgetDatas)

        row = []
        column = []
        tempData = []
        for item in sorted(items):
            row.append(item.row())
            column.append(item.column())
            tempData.append(int(item.text(),10))
            setItem = QtWidgets.QTableWidgetItem(f"{cellNumber}")
            setItem.setBackground(self.colorlist[cellNumber])
            self.tableWidget.setItem(item.row(),item.column(),setItem)
        
        tableWidgetDatas = self.getTableValue()
        tableWidgetDatas = np.array(tableWidgetDatas)

        self.tableWidget.clearSelection()

        if(cellNumber == 0):
            for i in range(len(row)):
                if(tempData[i] != 0):
                    deleteData,self.OPlist = NumpyArrayToHolePlate.GLViewDataPop(tableWidgetDatas,\
                        self.holePatternCombobox.currentText(),\
                        self.colorlist2,self.OPlist,row[i],column[i])
                    self.deleteShowMesh(deleteData.glMesh)
            
            return
                
        for i in range(len(row)):
            if(tempData[i]==0):
                addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(tableWidgetDatas,\
                    self.holePatternCombobox.currentText(),\
                    self.colorlist2,self.OPlist, row[i], column[i])
                self.addShowMesh(addData.glMesh)
            else:
                afterData,beforeData,self.OPlist = NumpyArrayToHolePlate.GLViewDataChange(tableWidgetDatas,\
                self.holePatternCombobox.currentText(),\
                self.colorlist2,self.OPlist, row[i], column[i])
                self.deleteShowMesh(beforeData.glMesh)
                self.addShowMesh(afterData.glMesh)

    def saveSettingFile(self):
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"~/.", ("json file (*.json)"))
        if filepath[0] != "":
            tableWidgetDatas = self.getTableValue()
            holePatternComboboxValue = self.holePatternCombobox.currentText()
            maxXScaleComboBoxValue = self.maxXScaleComboBox.currentText()
            maxYScaleComboBoxValue = self.maxYScaleComboBox.currentText()

            with open(filepath[0], 'w') as outfile:
                dumpData = {\
                    'tableWidgetDatas': tableWidgetDatas,\
                    'holePatternComboboxValue': holePatternComboboxValue,\
                    'maxXScaleComboBoxValue': maxXScaleComboBoxValue,\
                    'maxYScaleComboBoxValue': maxYScaleComboBoxValue\
                    }
                json.dump(dumpData,outfile)
                QtWidgets.QMessageBox.information(self, "file",f"設定ファイルの出力が完了しました。\n出力先:{filepath[0]}")


    def openSettingFile(self):
        print("open file")
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"~/.", ("json file (*.json)"))

        if filepath[0] != "":
            with open(filepath[0], 'r') as json_file:
                self.deleteAllShowMesh()
                self.OPlist.clear()

                json_data = json.load(json_file)

                # 旧フォーマット
                if "type" in json_data:
                    tableWidgetDatas = json_data['datas']
                    tableWidgetDatas = np.array(tableWidgetDatas)
                    holePatternComboboxValue = json_data['type']
                    maxXScaleComboBoxValue = "10"
                    maxYScaleComboBoxValue = "10"

                # 現行フォーマット
                else:
                    tableWidgetDatas = json_data['tableWidgetDatas']
                    tableWidgetDatas = np.array(tableWidgetDatas)
                    holePatternComboboxValue = json_data['holePatternComboboxValue']
                    maxXScaleComboBoxValue = json_data['maxXScaleComboBoxValue']
                    maxYScaleComboBoxValue = json_data['maxYScaleComboBoxValue']

                self.maxXScaleComboBox.setCurrentText(maxXScaleComboBoxValue)
                self.maxYScaleComboBox.setCurrentText(maxYScaleComboBoxValue)
                self.tableWidget.setColumnCount(int(self.maxXScaleComboBox.currentText()))
                self.tableWidget.setRowCount(int(self.maxYScaleComboBox.currentText()))


                self.setTableValue(tableWidgetDatas.T)
                self.holePatternCombobox.setCurrentText(holePatternComboboxValue)
                
                datas = self.getTableValue()
                datas = np.array(datas)

                column,row = np.where(datas != 0)

                for i in range(len(column)):
                    addData, self.OPlist = NumpyArrayToHolePlate.GLViewDataPush(datas,\
                        self.holePatternCombobox.currentText(),\
                        self.colorlist2,self.OPlist,row[i],column[i])
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