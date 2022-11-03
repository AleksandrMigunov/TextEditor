# Copyright (C) 2022 Aleksandr Migunov

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
  
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Text_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Text_1.setObjectName("label_Text_1")
        self.gridLayout.addWidget(self.label_Text_1, 0, 0, 1, 1)
        self.label_Text_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Text_2.setObjectName("label_Text_2")
        self.gridLayout.addWidget(self.label_Text_2, 0, 1, 1, 1)
        self.textEdit_Text_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Text_1.setObjectName("textEdit_Text_1")
        self.gridLayout.addWidget(self.textEdit_Text_1, 2, 0, 1, 1)
        self.textEdit_Text_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Text_2.setObjectName("textEdit_Text_2")
        self.gridLayout.addWidget(self.textEdit_Text_2, 2, 1, 1, 1)
        self.textEdit_Text_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Text_3.setObjectName("textEdit_Text_3")
        self.gridLayout.addWidget(self.textEdit_Text_3, 2, 2, 1, 1)
        self.label_Text_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_Text_3.setObjectName("label_Text_3")
        self.gridLayout.addWidget(self.label_Text_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuUndo = QtWidgets.QMenu(self.menuEdit)
        self.menuUndo.setObjectName("menuUndo")
        self.menuRedo = QtWidgets.QMenu(self.menuEdit)
        self.menuRedo.setObjectName("menuRedo")
        self.menuCut = QtWidgets.QMenu(self.menuEdit)
        self.menuCut.setObjectName("menuCut")
        self.menuCopy = QtWidgets.QMenu(self.menuEdit)
        self.menuCopy.setObjectName("menuCopy")
        self.menuPaste = QtWidgets.QMenu(self.menuEdit)
        self.menuPaste.setObjectName("menuPaste")
        self.menuFind = QtWidgets.QMenu(self.menuEdit)
        self.menuFind.setObjectName("menuFind")
        self.menuSelect_All = QtWidgets.QMenu(self.menuEdit)
        self.menuSelect_All.setObjectName("menuSelect_All")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuFont = QtWidgets.QMenu(self.menuTools)
        self.menuFont.setObjectName("menuFont")
        self.menuColor = QtWidgets.QMenu(self.menuTools)
        self.menuColor.setObjectName("menuColor")
        self.menuHighlight = QtWidgets.QMenu(self.menuTools)
        self.menuHighlight.setObjectName("menuHighlight")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuZoom_In = QtWidgets.QMenu(self.menuView)
        self.menuZoom_In.setObjectName("menuZoom_In")
        self.menuZoom_Out = QtWidgets.QMenu(self.menuView)
        self.menuZoom_Out.setObjectName("menuZoom_Out")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionNew_Text_1.setObjectName("actionNew_Text_1")
        self.actionNew_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_Text_2.setObjectName("actionNew_Text_2")
        self.actionOpen_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionOpen_Text_1.setObjectName("actionOpen_Text_1")
        self.actionOpen_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_Text_2.setObjectName("actionOpen_Text_2")
        self.actionSave_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionSave_Text_1.setObjectName("actionSave_Text_1")
        self.actionSave_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_Text_2.setObjectName("actionSave_Text_2")
        self.actionUndo_in_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionUndo_in_Text_1.setObjectName("actionUndo_in_Text_1")
        self.actionUndo_in_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionUndo_in_Text_2.setObjectName("actionUndo_in_Text_2")
        self.actionRedo_in_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionRedo_in_Text_1.setObjectName("actionRedo_in_Text_1")
        self.actionRedo_in_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionRedo_in_Text_2.setObjectName("actionRedo_in_Text_2")
        self.actionCut_from_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionCut_from_Text_1.setObjectName("actionCut_from_Text_1")
        self.actionCut_from_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionCut_from_Text_2.setObjectName("actionCut_from_Text_2")
        self.actionCopy_from_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionCopy_from_Text_1.setObjectName("actionCopy_from_Text_1")
        self.actionCopy_from_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionCopy_from_Text_2.setObjectName("actionCopy_from_Text_2")
        self.actionPaste_into_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionPaste_into_Text_1.setObjectName("actionPaste_into_Text_1")
        self.actionPaste_into_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionPaste_into_Text_2.setObjectName("actionPaste_into_Text_2")
        self.actionFind_in_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionFind_in_Text_1.setObjectName("actionFind_in_Text_1")
        self.actionFind_in_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionFind_in_Text_2.setObjectName("actionFind_in_Text_2")
        self.actionFont_of_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionFont_of_Text_1.setObjectName("actionFont_of_Text_1")
        self.actionFont_of_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionFont_of_Text_2.setObjectName("actionFont_of_Text_2")
        self.actionColor_of_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionColor_of_Text_1.setObjectName("actionColor_of_Text_1")
        self.actionColor_of_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionColor_of_Text_2.setObjectName("actionColor_of_Text_2")
        self.actionHighlight_in_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionHighlight_in_Text_1.setObjectName("actionHighlight_in_Text_1")
        self.actionHighlight_in_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionHighlight_in_Text_2.setObjectName("actionHighlight_in_Text_2")
        self.actionZoom_In_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionZoom_In_Text_1.setObjectName("actionZoom_In_Text_1")
        self.actionZoom_In_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionZoom_In_Text_2.setObjectName("actionZoom_In_Text_2")
        self.actionZoom_Out_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out_Text_1.setObjectName("actionZoom_Out_Text_1")
        self.actionZoom_Out_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out_Text_2.setObjectName("actionZoom_Out_Text_2")
        self.actionSelect_All_in_Text_1 = QtWidgets.QAction(MainWindow)
        self.actionSelect_All_in_Text_1.setObjectName("actionSelect_All_in_Text_1")
        self.actionSelect_All_in_Text_2 = QtWidgets.QAction(MainWindow)
        self.actionSelect_All_in_Text_2.setObjectName("actionSelect_All_in_Text_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionNew_Text_3.setObjectName("actionNew_Text_3")
        self.actionOpen_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionOpen_Text_3.setObjectName("actionOpen_Text_3")
        self.actionSave_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionSave_Text_3.setObjectName("actionSave_Text_3")
        self.actionUndo_in_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionUndo_in_Text_3.setObjectName("actionUndo_in_Text_3")
        self.actionRedo_in_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionRedo_in_Text_3.setObjectName("actionRedo_in_Text_3")
        self.actionCut_from_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionCut_from_Text_3.setObjectName("actionCut_from_Text_3")
        self.actionCopy_from_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionCopy_from_Text_3.setObjectName("actionCopy_from_Text_3")
        self.actionPaste_into_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionPaste_into_Text_3.setObjectName("actionPaste_into_Text_3")
        self.actionSelect_All_in_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionSelect_All_in_Text_3.setObjectName("actionSelect_All_in_Text_3")
        self.actionZoom_In_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionZoom_In_Text_3.setObjectName("actionZoom_In_Text_3")
        self.actionZoom_Out_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out_Text_3.setObjectName("actionZoom_Out_Text_3")
        self.actionFont_of_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionFont_of_Text_3.setObjectName("actionFont_of_Text_3")
        self.actionColor_of_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionColor_of_Text_3.setObjectName("actionColor_of_Text_3")
        self.actionHighlight_in_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionHighlight_in_Text_3.setObjectName("actionHighlight_in_Text_3")
        self.actionFind_in_Text_3 = QtWidgets.QAction(MainWindow)
        self.actionFind_in_Text_3.setObjectName("actionFind_in_Text_3")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menuNew.addAction(self.actionNew_Text_1)
        self.menuNew.addAction(self.actionNew_Text_2)
        self.menuNew.addAction(self.actionNew_Text_3)
        self.menuOpen.addAction(self.actionOpen_Text_1)
        self.menuOpen.addAction(self.actionOpen_Text_2)
        self.menuOpen.addAction(self.actionOpen_Text_3)
        self.menuSave.addAction(self.actionSave_Text_1)
        self.menuSave.addAction(self.actionSave_Text_2)
        self.menuSave.addAction(self.actionSave_Text_3)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuUndo.addAction(self.actionUndo_in_Text_1)
        self.menuUndo.addAction(self.actionUndo_in_Text_2)
        self.menuUndo.addAction(self.actionUndo_in_Text_3)
        self.menuRedo.addAction(self.actionRedo_in_Text_1)
        self.menuRedo.addAction(self.actionRedo_in_Text_2)
        self.menuRedo.addAction(self.actionRedo_in_Text_3)
        self.menuCut.addAction(self.actionCut_from_Text_1)
        self.menuCut.addAction(self.actionCut_from_Text_2)
        self.menuCut.addAction(self.actionCut_from_Text_3)
        self.menuCopy.addAction(self.actionCopy_from_Text_1)
        self.menuCopy.addAction(self.actionCopy_from_Text_2)
        self.menuCopy.addAction(self.actionCopy_from_Text_3)
        self.menuPaste.addAction(self.actionPaste_into_Text_1)
        self.menuPaste.addAction(self.actionPaste_into_Text_2)
        self.menuPaste.addAction(self.actionPaste_into_Text_3)
        self.menuFind.addAction(self.actionFind_in_Text_1)
        self.menuFind.addAction(self.actionFind_in_Text_2)
        self.menuFind.addAction(self.actionFind_in_Text_3)
        self.menuSelect_All.addAction(self.actionSelect_All_in_Text_1)
        self.menuSelect_All.addAction(self.actionSelect_All_in_Text_2)
        self.menuSelect_All.addAction(self.actionSelect_All_in_Text_3)
        self.menuEdit.addAction(self.menuUndo.menuAction())
        self.menuEdit.addAction(self.menuRedo.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuCut.menuAction())
        self.menuEdit.addAction(self.menuCopy.menuAction())
        self.menuEdit.addAction(self.menuPaste.menuAction())
        self.menuEdit.addAction(self.menuSelect_All.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuFind.menuAction())
        self.menuFont.addAction(self.actionFont_of_Text_1)
        self.menuFont.addAction(self.actionFont_of_Text_2)
        self.menuFont.addAction(self.actionFont_of_Text_3)
        self.menuColor.addAction(self.actionColor_of_Text_1)
        self.menuColor.addAction(self.actionColor_of_Text_2)
        self.menuColor.addAction(self.actionColor_of_Text_3)
        self.menuHighlight.addAction(self.actionHighlight_in_Text_1)
        self.menuHighlight.addAction(self.actionHighlight_in_Text_2)
        self.menuHighlight.addAction(self.actionHighlight_in_Text_3)
        self.menuTools.addAction(self.menuFont.menuAction())
        self.menuTools.addAction(self.menuColor.menuAction())
        self.menuTools.addAction(self.menuHighlight.menuAction())
        self.menuZoom_In.addAction(self.actionZoom_In_Text_1)
        self.menuZoom_In.addAction(self.actionZoom_In_Text_2)
        self.menuZoom_In.addAction(self.actionZoom_In_Text_3)
        self.menuZoom_Out.addAction(self.actionZoom_Out_Text_1)
        self.menuZoom_Out.addAction(self.actionZoom_Out_Text_2)
        self.menuZoom_Out.addAction(self.actionZoom_Out_Text_3)
        self.menuView.addAction(self.menuZoom_In.menuAction())
        self.menuView.addAction(self.menuZoom_Out.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ThreeTextEditor in Python with PySide"))
        self.label_Text_1.setText(_translate("MainWindow", "<b>Text 1</b>"))
        self.label_Text_2.setText(_translate("MainWindow", "<b>Text 2</b>"))
        self.label_Text_3.setText(_translate("MainWindow", "<b>Text 3</b>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuUndo.setTitle(_translate("MainWindow", "Undo"))
        self.menuRedo.setTitle(_translate("MainWindow", "Redo"))
        self.menuCut.setTitle(_translate("MainWindow", "Cut"))
        self.menuCopy.setTitle(_translate("MainWindow", "Copy"))
        self.menuPaste.setTitle(_translate("MainWindow", "Paste"))
        self.menuFind.setTitle(_translate("MainWindow", "Find"))
        self.menuSelect_All.setTitle(_translate("MainWindow", "Select All"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuFont.setTitle(_translate("MainWindow", "Font"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuHighlight.setTitle(_translate("MainWindow", "Highlight"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuZoom_In.setTitle(_translate("MainWindow", "Zoom In"))
        self.menuZoom_Out.setTitle(_translate("MainWindow", "Zoom Out"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_Text_1.setText(_translate("MainWindow", "New Text 1"))
        self.actionNew_Text_2.setText(_translate("MainWindow", "New Text 2"))
        self.actionOpen_Text_1.setText(_translate("MainWindow", "Open Text 1"))
        self.actionOpen_Text_2.setText(_translate("MainWindow", "Open Text 2"))
        self.actionSave_Text_1.setText(_translate("MainWindow", "Save Text 1"))
        self.actionSave_Text_2.setText(_translate("MainWindow", "Save Text 2"))
        self.actionUndo_in_Text_1.setText(_translate("MainWindow", "Undo in Text 1"))
        self.actionUndo_in_Text_2.setText(_translate("MainWindow", "Undo in Text 2"))
        self.actionRedo_in_Text_1.setText(_translate("MainWindow", "Redo in Text 1"))
        self.actionRedo_in_Text_2.setText(_translate("MainWindow", "Redo in Text 2"))
        self.actionCut_from_Text_1.setText(_translate("MainWindow", "Cut from Text 1"))
        self.actionCut_from_Text_2.setText(_translate("MainWindow", "Cut from Text 2"))
        self.actionCopy_from_Text_1.setText(_translate("MainWindow", "Copy from Text 1"))
        self.actionCopy_from_Text_2.setText(_translate("MainWindow", "Copy from Text 2"))
        self.actionPaste_into_Text_1.setText(_translate("MainWindow", "Paste into Text 1"))
        self.actionPaste_into_Text_2.setText(_translate("MainWindow", "Paste into Text 2"))
        self.actionFind_in_Text_1.setText(_translate("MainWindow", "Find in Text 1"))
        self.actionFind_in_Text_2.setText(_translate("MainWindow", "Find in Text 2"))
        self.actionFont_of_Text_1.setText(_translate("MainWindow", "Font of Text 1"))
        self.actionFont_of_Text_2.setText(_translate("MainWindow", "Font of Text 2"))
        self.actionColor_of_Text_1.setText(_translate("MainWindow", "Color of Text 1"))
        self.actionColor_of_Text_2.setText(_translate("MainWindow", "Color of Text 2"))
        self.actionHighlight_in_Text_1.setText(_translate("MainWindow", "Highlight in Text 1"))
        self.actionHighlight_in_Text_2.setText(_translate("MainWindow", "Highlight in Text 2"))
        self.actionZoom_In_Text_1.setText(_translate("MainWindow", "Zoom In Text 1"))
        self.actionZoom_In_Text_2.setText(_translate("MainWindow", "Zoom In Text 2"))
        self.actionZoom_Out_Text_1.setText(_translate("MainWindow", "Zoom Out Text 1"))
        self.actionZoom_Out_Text_2.setText(_translate("MainWindow", "Zoom Out Text 2"))
        self.actionSelect_All_in_Text_1.setText(_translate("MainWindow", "Select All in Text 1"))
        self.actionSelect_All_in_Text_2.setText(_translate("MainWindow", "Select All in Text 2"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionNew_Text_3.setText(_translate("MainWindow", "New Text 3"))
        self.actionOpen_Text_3.setText(_translate("MainWindow", "Open Text 3"))
        self.actionSave_Text_3.setText(_translate("MainWindow", "Save Text 3"))
        self.actionUndo_in_Text_3.setText(_translate("MainWindow", "Undo in Text 3"))
        self.actionRedo_in_Text_3.setText(_translate("MainWindow", "Redo in Text 3"))
        self.actionCut_from_Text_3.setText(_translate("MainWindow", "Cut from Text 3"))
        self.actionCopy_from_Text_3.setText(_translate("MainWindow", "Copy from Text 3"))
        self.actionPaste_into_Text_3.setText(_translate("MainWindow", "Paste into Text 3"))
        self.actionSelect_All_in_Text_3.setText(_translate("MainWindow", "Select All in Text 3"))
        self.actionZoom_In_Text_3.setText(_translate("MainWindow", "Zoom In Text 3"))
        self.actionZoom_Out_Text_3.setText(_translate("MainWindow", "Zoom Out Text 3"))
        self.actionFont_of_Text_3.setText(_translate("MainWindow", "Font of Text 3"))
        self.actionColor_of_Text_3.setText(_translate("MainWindow", "Color of Text 3"))
        self.actionHighlight_in_Text_3.setText(_translate("MainWindow", "Highlight in Text 3"))
        self.actionFind_in_Text_3.setText(_translate("MainWindow", "Find in Text 3"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
