# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/git/python/Calculator/calc_log_mod.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 950)
        Dialog.setMinimumSize(QtCore.QSize(550, 950))
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 500, 900))
        self.textBrowser.setMinimumSize(QtCore.QSize(500, 900))
        self.textBrowser.setMaximumSize(QtCore.QSize(500, 900))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Logs"))
