# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AverageDaysInTestUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 360)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AverageDaysTest_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.AverageDaysTest_lbl.setFont(font)
        self.AverageDaysTest_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AverageDaysTest_lbl.setObjectName("AverageDaysTest_lbl")
        self.verticalLayout.addWidget(self.AverageDaysTest_lbl)
        self.AverageDaysInTest_int = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AverageDaysInTest_int.setFont(font)
        self.AverageDaysInTest_int.setAlignment(QtCore.Qt.AlignCenter)
        self.AverageDaysInTest_int.setObjectName("AverageDaysInTest_int")
        self.verticalLayout.addWidget(self.AverageDaysInTest_int)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LastReportedAverage_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.LastReportedAverage_lbl.setFont(font)
        self.LastReportedAverage_lbl.setScaledContents(False)
        self.LastReportedAverage_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.LastReportedAverage_lbl.setWordWrap(False)
        self.LastReportedAverage_lbl.setObjectName("LastReportedAverage_lbl")
        self.verticalLayout_2.addWidget(self.LastReportedAverage_lbl)
        self.LastReportedAverage_int = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LastReportedAverage_int.setFont(font)
        self.LastReportedAverage_int.setAlignment(QtCore.Qt.AlignCenter)
        self.LastReportedAverage_int.setObjectName("LastReportedAverage_int")
        self.verticalLayout_2.addWidget(self.LastReportedAverage_int)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AverageDelta_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AverageDelta_lbl.setFont(font)
        self.AverageDelta_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AverageDelta_lbl.setObjectName("AverageDelta_lbl")
        self.verticalLayout_3.addWidget(self.AverageDelta_lbl)
        self.AverageDelta_int = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AverageDelta_int.setFont(font)
        self.AverageDelta_int.setAlignment(QtCore.Qt.AlignCenter)
        self.AverageDelta_int.setObjectName("AverageDelta_int")
        self.verticalLayout_3.addWidget(self.AverageDelta_int)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.UpdateNumber_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UpdateNumber_btn.setObjectName("UpdateNumber_btn")
        self.verticalLayout.addWidget(self.UpdateNumber_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Average Test Card Tracker"))
        self.AverageDaysTest_lbl.setText(_translate("Form", "Average Days Card has spent in Test"))
        self.AverageDaysInTest_int.setText(_translate("Form", "TextLabel"))
        self.LastReportedAverage_lbl.setText(_translate("Form", "Last Reported Average"))
        self.LastReportedAverage_int.setText(_translate("Form", "0"))
        self.AverageDelta_lbl.setText(_translate("Form", "Average Delta"))
        self.AverageDelta_int.setText(_translate("Form", "0"))
        self.UpdateNumber_btn.setText(_translate("Form", "Update Average"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

