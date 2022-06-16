import sys
from PyQt6 import QtCore,QtGui, QtWidgets #, QtOpenGLWidgets
import pyqtgraph.opengl as gl
from ui_files import mainui
from HolePlateMaker import NumpyArrayToHolePlate

import numpy as np
from stl import mesh

class app_1(QtWidgets.QDialog, mainui.Ui_Dialog):
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

        self.initTableValue()
        axis = gl.GLGridItem()
        axis.setSpacing(x=1,y=1,z=1)
        self.openGLWidget.addItem(axis)

        self.holePatternCombobox.addItems(['3mm', '4.8mm'])
        self.holePatternCombobox.setCurrentIndex(0)
        self.holePatternCombobox.currentIndexChanged.connect(self.changeIndex)

        self.lastDir = None
        self.droppedFilename = None
        self.currentSTL = None
        self.glAllMesh = None
        self.bufGLAllMesh = None


    def changeIndex(self,index):
        datas = self.getTableValue()
        self.curMesh, self.glAllMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(np.array(datas),self.holePatternCombobox.currentText(),self.colorlist2)
        self.showGLAllMesh()


    def initTableValue(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(j,i,QtWidgets.QTableWidgetItem("0"))
                self.tableWidget.item(j,i).setBackground(\
                    self.colorlist[0])


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
        self.curMesh, self.glAllMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(np.array(datas),self.holePatternCombobox.currentText(),self.colorlist2)
        self.showGLAllMesh()

        #print(datas)

    @QtCore.pyqtSlot()
    def on_push_b1(self):
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"~/.", ("STL file (*.stl)"))
        self.curMesh.save(filepath[0])
        
    def showGLAllMesh(self):
        if self.bufGLAllMesh:
            for i in range(len(self.bufGLAllMesh)):
                self.openGLWidget.removeItem(self.bufGLAllMesh[i])

        for i in range(len(self.glAllMesh)):
            self.openGLWidget.addItem(self.glAllMesh[i])
        
        self.bufGLAllMesh = self.glAllMesh

    def loadSTL(self, filename):
        m = mesh.Mesh.from_file(filename)
        shape = m.points.shape
        points = m.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)
        return points, faces

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid=app_1()
    wid.show()
    sys.exit(app.exec())