# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QWidget, qApp
from PyQt5.QtGui import QTextDocument, QTextCursor


class Writer(QWidget):

    def __init__(self):
        super().__init__()

        # set up the text editor
        self.text = QTextEdit()

        # set up the clear button
        self.clr_btn = QPushButton('Clear')
        # self.save_btn = QPushButton('Save')
        # self.opn_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        # set up h box layouts for button and text box
        hb1 = QHBoxLayout()
        hb1.addStretch()
        hb1.addWidget(self.clr_btn)
        # hb1.addWidget(self.save_btn)
        # hb1.addWidget(self.opn_btn)
        hb1.addStretch()

        # set up slots for the buttons
        self.clr_btn.clicked.connect(self.text.clear)
        # self.save_btn.clicked.connect(self.save)
        # self.opn_btn.clicked.connect(self.open)

        # set up a main v box layout
        vb = QVBoxLayout()
        vb.addWidget(self.text)
        vb.addLayout(hb1)

        # set up window
        self.setLayout(vb)
        self.setWindowTitle('Text Editor')
        self.show()

    def save(self):
        try:
            file_name = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
            with open(file_name[0], 'w') as file:
                text = self.text.toPlainText()
                file.write(text)
        except FileNotFoundError:
            pass

    def open(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
            with open(file_name[0], 'r') as file:
                self.text.setText(file.read())
        except FileNotFoundError:
            pass


class Ui_Editor(object):
    def setupUi(self, Editor):
        # set up window
        Editor.setObjectName("Editor")
        Editor.resize(800, 600)
        # center widget
        self.form_widget = Writer()
        self.form_widget.clr_btn.deleteLater()
        Editor.setCentralWidget(self.form_widget)
        self.form_widget.setObjectName("Central Widget")

        # text area
        self.form_widget.setGeometry(QtCore.QRect(0, 0, 801, 558))
        self.form_widget.setObjectName("Text Area")

        # status bar
        self.statusbar = QtWidgets.QStatusBar(Editor)
        self.statusbar.setObjectName("statusbar")
        Editor.setStatusBar(self.statusbar)

        # set up menu bar
        self.menubar = QtWidgets.QMenuBar(Editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        Editor.setMenuBar(self.menubar)

        # set up root menus
        # file menu
        self.menuFile = QtWidgets.QMenu(self.menubar)  # file menu
        self.menuFile.setObjectName("menuFile")
        self.menubar.addAction(self.menuFile.menuAction())
        # edit menu
        self.menuEdit = QtWidgets.QMenu(self.menubar)  # edit menu
        self.menuEdit.setObjectName("menuEdit")
        self.menuFind_Replace = QtWidgets.QMenu(self.menuEdit)  # find/replace menu
        self.menubar.addAction(self.menuEdit.menuAction())
        # window menu
        self.menuFind_Replace.setObjectName("menuFind_Replace")
        self.menuWindow = QtWidgets.QMenu(self.menubar)  # window menu
        self.menuWindow.setObjectName("menuWindow")
        self.menubar.addAction(self.menuWindow.menuAction())

        # set up actions
        # file actions
        self.actionNew = QtWidgets.QAction(Editor)  # new action
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.actionNew.triggered.connect(lambda: self.onClick("new"))
        self.actionOpen = QtWidgets.QAction(Editor)  # open action
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(lambda: self.onClick("open"))
        self.actionSave = QtWidgets.QAction(Editor)  # save action
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.actionSave.triggered.connect(lambda: self.onClick("save"))
        self.actionQuit = QtWidgets.QAction(Editor)  # quit action
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(lambda: self.onClick("quit"))

        # edit actions
        self.actionCopy = QtWidgets.QAction(Editor)  # copy action
        self.actionCopy.setObjectName("actionCopy")
        self.menuEdit.addAction(self.actionCopy)
        self.actionCopy.triggered.connect(lambda: self.onClick("copy"))
        self.actionPaste = QtWidgets.QAction(Editor)  # paste action
        self.actionPaste.setObjectName("actionPaste")
        self.menuEdit.addAction(self.actionPaste)
        self.actionPaste.triggered.connect(lambda: self.onClick("paste"))
        self.actionUndo = QtWidgets.QAction(Editor)  # undo action
        self.actionUndo.setObjectName("actionUndo")
        self.menuEdit.addAction(self.actionUndo)
        self.actionUndo.triggered.connect(lambda: self.onClick("undo"))
        self.actionRedo = QtWidgets.QAction(Editor)  # redo action
        self.actionRedo.setObjectName("actionRedo")
        self.menuEdit.addAction(self.actionRedo)
        self.actionRedo.triggered.connect(lambda: self.onClick("redo"))
        # find replace sub menu
        self.menuEdit.addAction(self.menuFind_Replace.menuAction())
        self.actionFind = QtWidgets.QAction(Editor)  # find action
        self.actionFind.setObjectName("actionFind")
        self.menuFind_Replace.addAction(self.actionFind)
        self.actionFind.triggered.connect(lambda: self.onClick("find"))
        self.actionReplace = QtWidgets.QAction(Editor)  # replace action
        self.actionReplace.setObjectName("actionReplace")
        self.menuFind_Replace.addAction(self.actionReplace)
        self.actionReplace.triggered.connect(lambda: self.onClick("replace"))

        # window actions
        self.actionMinimize = QtWidgets.QAction(Editor)  # minimize action
        self.actionMinimize.setObjectName("actionMinimize")
        self.menuWindow.addAction(self.actionMinimize)
        self.actionMinimize.triggered.connect(lambda: self.onClick("minimize"))
        self.actionFull_Screen = QtWidgets.QAction(Editor)  # full screen action
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.menuWindow.addAction(self.actionFull_Screen)
        self.actionFull_Screen.triggered.connect(lambda: self.onClick("fullscreen"))

        # re-translate to main window form
        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        # set window title
        Editor.setWindowTitle(_translate("Editor", "Editor"))

        # set menu titles
        self.menuFile.setTitle(_translate("Editor", "File"))
        self.menuEdit.setTitle(_translate("Editor", "Edit"))
        self.menuFind_Replace.setTitle(_translate("Editor", "Find/Replace"))
        self.menuWindow.setTitle(_translate("Editor", "Window"))

        # set action names
        # file actions
        self.actionNew.setText(_translate("Editor", "New"))  # new action
        self.actionNew.setStatusTip(_translate("Editor", "Create New File"))
        self.actionNew.setShortcut(_translate("Editor", "Ctrl+N"))
        self.actionOpen.setText(_translate("Editor", "Open"))  # open action
        self.actionOpen.setStatusTip(_translate("Editor", "Open File"))
        self.actionOpen.setShortcut(_translate("Editor", "Ctrl+O"))
        self.actionSave.setText(_translate("Editor", "Save"))  #  save action
        self.actionSave.setStatusTip(_translate("Editor", "Save File"))
        self.actionSave.setShortcut(_translate("Editor", "Ctrl+S"))
        self.actionQuit.setText(_translate("Editor", "Quit"))  # quit action
        self.actionQuit.setStatusTip(_translate("Editor", "Quit Window"))
        self.actionQuit.setShortcut(_translate("Editor", "Ctrl+W"))
        # edit actions
        self.actionCopy.setText(_translate("Editor", "Copy"))  # copy actions
        self.actionCopy.setStatusTip(_translate("Editor", "Copy to Clipboard"))
        self.actionCopy.setShortcut(_translate("Editor", "Ctrl+C"))
        self.actionPaste.setText(_translate("Editor", "Paste"))  # paste action
        self.actionPaste.setStatusTip(_translate("Editor", "Paste to File"))
        self.actionPaste.setShortcut(_translate("Editor", "Ctrl+V"))
        self.actionUndo.setText(_translate("Editor", "Undo"))  # undo action
        self.actionUndo.setStatusTip(_translate("Editor", "Undo Last Action"))
        self.actionUndo.setShortcut(_translate("Editor", "Ctrl+Z"))
        self.actionRedo.setText(_translate("Editor", "Redo"))  # redo action
        self.actionRedo.setShortcut(_translate("Editor", "Ctrl+Y"))
        self.actionRedo.setStatusTip(_translate("Editor", "Redo Action"))
        self.actionFind.setText(_translate("Editor", "Find"))  # find action
        self.actionFind.setStatusTip(_translate("Editor", "Find in File"))
        self.actionFind.setShortcut(_translate("Editor", "Ctrl+F"))
        self.actionReplace.setText(_translate("Editor", "Replace"))  # replace action
        self.actionReplace.setStatusTip(_translate("Editor", "Replace Highlighted Item"))
        self.actionReplace.setShortcut(_translate("Editor", "Ctrl+H"))
        # window actions
        self.actionMinimize.setText(_translate("Editor", "Minimize"))  # minimize action
        self.actionMinimize.setShortcut(_translate("Editor", "Ctrl+M"))
        self.actionMinimize.setStatusTip(_translate("Editor", "Minimize Window"))
        self.actionFull_Screen.setText(_translate("Editor", "Full Screen"))  # full screen action
        self.actionFull_Screen.setStatusTip(_translate("Editor", "Enter Full Screen"))

    def onClick(self, action):
        if action == "new":
            self.form_widget.text.clear()
        elif action == "open":
            self.form_widget.open()
        elif action == "save":
            self.form_widget.save()
        elif action == "quit":
            qApp.quit()
        elif action == "copy":
            self.form_widget.text.copy()
        elif action == "paste":
            self.form_widget.text.paste()
        elif action == "redo":
            self.form_widget.text.undo()
        elif action == "undo":
            self.form_widget.text.redo()
        elif action == "find":
            # dialogue layout
            self.find_dialogue = QtWidgets.QDialog()
            self.find_dialogue.setWindowTitle("Find")
            self.find_dialogue.setGeometry(400, 400, 200, 50)
            # widgets
            h1 = QtWidgets.QHBoxLayout()
            l1 = QtWidgets.QLineEdit()
            start = QTextCursor.MoveOperation
            b1 = QtWidgets.QPushButton('Find')
            b1.clicked.connect(lambda: self.dialogue(l1.text()))
            h1.addWidget(l1)
            h1.addWidget(b1)
            # execution
            self.find_dialogue.setLayout(h1)
            self.find_dialogue.exec_()
        elif action == "replace":
            pass
        elif action == "minimize":
            Editor.showMinimized()
        elif action == "fullscreen":
            Editor.showFullScreen()

    def dialogue(self, text):
        check = False
        while not check:
            check = self.form_widget.text.find(text)
        self.find_dialogue.deleteLater()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QMainWindow()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())
