import sys
from PyQt6 import QtCore,QtGui, QtWidgets #, QtOpenGLWidgets
import pyqtgraph.opengl as gl
from ui_files import mainui
from HolePlateMaker import NumpyArrayToHolePlate

import numpy as np
from stl import mesh

class app_1(QtWidgets.QDialog, mainui.Ui_Dialog):
    def __init__(self):
        super(app_1,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_push_b1)
        self.tableWidget.cellClicked.connect(self.on_clickcell)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

        self.initTableValue()
        axis = gl.GLGridItem()
        axis.setSpacing(x=1,y=1,z=1)
        self.openGLWidget.addItem(axis)

        self.lastDir = None
        self.droppedFilename = None
        self.currentSTL = None

        self.colorlist = [QtGui.QColor(255,255,255),\
                QtGui.QColor(96,240,168),\
                QtGui.QColor(240,168,96),\
                QtGui.QColor(240,96,96),\
                QtGui.QColor(168,96,240),\
                QtGui.QColor(96,240,240),\
                QtGui.QColor(240,240,96),\
                QtGui.QColor(96,96,240),\
                QtGui.QColor(0,255,0),\
                ]

    def initTableValue(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(j,i,QtWidgets.QTableWidgetItem("0"))

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
            
            print(f"{int(self.tableWidget.item(row,column).text(),10) + 1}")
            self.tableWidget.setItem(row,column,newItem)
        else:
            self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem("0"))
        
        self.tableWidget.item(row,column).setBackground(self.colorlist[int(self.tableWidget.item(row,column).text(),10)])

        datas = self.getTableValue()
        self.curMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(np.array(datas),'4.8mm')
        self.showMesh()

        print(datas)

    @QtCore.pyqtSlot()
    def on_push_b1(self):
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"~/.", ("STL file (*.stl)"))
        self.curMesh.save(filepath[0])
        

    def showMesh(self):
        viewCurMesh = self.curMesh
        # note: 重心を揃える
        volume, cog, inertia = viewCurMesh.get_mass_properties()
        viewCurMesh.translate(-cog)
        
        shape = viewCurMesh.points.shape
        points = viewCurMesh.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)
        meshdata = gl.MeshData(vertexes=points, faces=faces)
        mesh = gl.GLMeshItem(meshdata=meshdata, smooth=True,\
            drawFaces=True, drawEdges=False, edgeColor=(0, 0, 0, 1))
        mesh.scale(0.1,0.1,0.1)
        if self.currentSTL:
            self.openGLWidget.removeItem(self.currentSTL)
        self.openGLWidget.addItem(mesh)
        self.currentSTL = mesh


    def showSTL(self,filename):
        if self.currentSTL:
            self.openGLWidget.removeItem(self.currentSTL)
        
        points, faces = self.loadSTL(filename)
        meshdata = gl.MeshData(vertexes=points, faces=faces)
        mesh = gl.GLMeshItem(meshdata=meshdata, smooth=True,\
            drawFaces=False, drawEdges=True, edgeColor=(0, 1, 0, 1))
        self.openGLWidget.addItem(mesh)

        self.currentSTL = mesh

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