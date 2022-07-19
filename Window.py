# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.selector_tab = QtWidgets.QWidget()
        self.selector_tab.setObjectName("selector_tab")
        self.label = QtWidgets.QLabel(self.selector_tab)
        self.label.setGeometry(QtCore.QRect(10, 27, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.selector_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 131, 18))
        self.label_2.setObjectName("label_2")
        self.serverRemove = QtWidgets.QPushButton(self.selector_tab)
        self.serverRemove.setGeometry(QtCore.QRect(310, 400, 91, 31))
        self.serverRemove.setObjectName("serverRemove")
        self.serverAdd = QtWidgets.QPushButton(self.selector_tab)
        self.serverAdd.setGeometry(QtCore.QRect(220, 400, 91, 31))
        self.serverAdd.setObjectName("serverAdd")
        self.serverInput = QtWidgets.QLineEdit(self.selector_tab)
        self.serverInput.setGeometry(QtCore.QRect(10, 400, 211, 31))
        self.serverInput.setObjectName("serverInput")
        self.wlsToggle = QtWidgets.QCheckBox(self.selector_tab)
        self.wlsToggle.setGeometry(QtCore.QRect(10, 430, 391, 24))
        self.wlsToggle.setObjectName("wlsToggle")
        self.wrlList = QtWidgets.QListWidget(self.selector_tab)
        self.wrlList.setGeometry(QtCore.QRect(410, 50, 361, 351))
        self.wrlList.setObjectName("wrlList")
        self.label_3 = QtWidgets.QLabel(self.selector_tab)
        self.label_3.setGeometry(QtCore.QRect(410, 30, 151, 21))
        self.label_3.setObjectName("label_3")
        self.selectAll = QtWidgets.QPushButton(self.selector_tab)
        self.selectAll.setGeometry(QtCore.QRect(410, 400, 181, 31))
        self.selectAll.setObjectName("selectAll")
        self.deselectAll = QtWidgets.QPushButton(self.selector_tab)
        self.deselectAll.setGeometry(QtCore.QRect(590, 400, 181, 31))
        self.deselectAll.setObjectName("deselectAll")
        self.indexList = QtWidgets.QTreeWidget(self.selector_tab)
        self.indexList.setGeometry(QtCore.QRect(10, 50, 391, 171))
        self.indexList.setObjectName("indexList")
        self.indexList.headerItem().setTextAlignment(1, QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userList = QtWidgets.QTreeWidget(self.selector_tab)
        self.userList.setGeometry(QtCore.QRect(10, 240, 391, 161))
        self.userList.setObjectName("userList")
        self.userList.headerItem().setTextAlignment(1, QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.applyButton = QtWidgets.QPushButton(self.selector_tab)
        self.applyButton.setGeometry(QtCore.QRect(590, 440, 181, 31))
        self.applyButton.setObjectName("applyButton")
        self.tabWidget.addTab(self.selector_tab, "")
        self.options_tab = QtWidgets.QWidget()
        self.options_tab.setObjectName("options_tab")
        self.wrlFolder = QtWidgets.QLineEdit(self.options_tab)
        self.wrlFolder.setGeometry(QtCore.QRect(10, 40, 741, 21))
        self.wrlFolder.setObjectName("wrlFolder")
        self.label_4 = QtWidgets.QLabel(self.options_tab)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 761, 17))
        self.label_4.setObjectName("label_4")
        self.browseWrlFolder = QtWidgets.QToolButton(self.options_tab)
        self.browseWrlFolder.setGeometry(QtCore.QRect(750, 40, 24, 21))
        self.browseWrlFolder.setObjectName("browseWrlFolder")
        self.label_5 = QtWidgets.QLabel(self.options_tab)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 771, 17))
        self.label_5.setObjectName("label_5")
        self.indexUrl = QtWidgets.QLineEdit(self.options_tab)
        self.indexUrl.setGeometry(QtCore.QRect(10, 90, 761, 25))
        self.indexUrl.setObjectName("indexUrl")
        self.saveButton = QtWidgets.QPushButton(self.options_tab)
        self.saveButton.setGeometry(QtCore.QRect(660, 120, 111, 31))
        self.saveButton.setObjectName("saveButton")
        self.tabWidget.addTab(self.options_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_worlds_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_worlds_folder.setObjectName("actionOpen_worlds_folder")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KISS"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Menu for setting the server you would like to connect to</p></body></html>"))
        self.selector_tab.setAccessibleName(_translate("MainWindow", "Server Selector"))
        self.label.setText(_translate("MainWindow", "Server Index"))
        self.label_2.setText(_translate("MainWindow", "User added servers"))
        self.serverRemove.setText(_translate("MainWindow", "Remove"))
        self.serverAdd.setText(_translate("MainWindow", "Add"))
        self.wlsToggle.setText(_translate("MainWindow", "Server uses WLS"))
        self.label_3.setText(_translate("MainWindow", ".wrl files to update"))
        self.selectAll.setText(_translate("MainWindow", "Select All"))
        self.deselectAll.setText(_translate("MainWindow", "Deselect All"))
        self.indexList.headerItem().setText(0, _translate("MainWindow", "Server Address & Port"))
        self.indexList.headerItem().setText(1, _translate("MainWindow", "WLS Required"))
        self.userList.headerItem().setText(0, _translate("MainWindow", "Server Address & Port"))
        self.userList.headerItem().setText(1, _translate("MainWindow", "WLS Required"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selector_tab), _translate("MainWindow", "Server Selector"))
        self.wrlFolder.setText(_translate("MainWindow", "C:\\Sony\\Community Place Browser\\world"))
        self.label_4.setText(_translate("MainWindow", "worlds Folder (Contains .wrl files)"))
        self.browseWrlFolder.setText(_translate("MainWindow", "..."))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>The Server Index is a centralised index managed by kodicraft4#6685 </p><p>which aims to make discovery of Sapari servers easier.</p><p>You may use another index if you\'d like.</p><p>DM Kodi if you want your server added!</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Server Index URL (?)"))
        self.indexUrl.setText(_translate("MainWindow", "https://sapari.kdcf.me"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.options_tab), _translate("MainWindow", "Options"))
        self.actionOpen_worlds_folder.setText(_translate("MainWindow", "Open worlds folder..."))
