# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_box_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckBoxWindow(object):
    def setupUi(self, CheckBoxWindow):
        CheckBoxWindow.setObjectName("CheckBoxWindow")
        CheckBoxWindow.resize(350, 250)
        self.label_text_for_user = QtWidgets.QLabel(CheckBoxWindow)
        self.label_text_for_user.setGeometry(QtCore.QRect(7, 5, 341, 31))
        self.label_text_for_user.setObjectName("label_text_for_user")
        self.label_selected_values = QtWidgets.QLabel(CheckBoxWindow)
        self.label_selected_values.setGeometry(QtCore.QRect(7, 200, 341, 31))
        self.label_selected_values.setObjectName("label_selected_values")
        self.layoutWidget = QtWidgets.QWidget(CheckBoxWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_16x16 = QtWidgets.QCheckBox(self.layoutWidget)
        self.check_16x16.setObjectName("check_16x16")
        self.verticalLayout.addWidget(self.check_16x16)
        self.check_32x32 = QtWidgets.QCheckBox(self.layoutWidget)
        self.check_32x32.setObjectName("check_32x32")
        self.verticalLayout.addWidget(self.check_32x32)
        self.check_64x64 = QtWidgets.QCheckBox(self.layoutWidget)
        self.check_64x64.setObjectName("check_64x64")
        self.verticalLayout.addWidget(self.check_64x64)
        self.check_128x128 = QtWidgets.QCheckBox(self.layoutWidget)
        self.check_128x128.setObjectName("check_128x128")
        self.verticalLayout.addWidget(self.check_128x128)
        self.check_192x192 = QtWidgets.QCheckBox(self.layoutWidget)
        self.check_192x192.setObjectName("check_192x192")
        self.verticalLayout.addWidget(self.check_192x192)

        self.retranslateUi(CheckBoxWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckBoxWindow)

    def retranslateUi(self, CheckBoxWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckBoxWindow.setWindowTitle(_translate("CheckBoxWindow", "Form"))
        self.label_text_for_user.setText(_translate("CheckBoxWindow", "Select sizes that you need:"))
        self.label_selected_values.setText(_translate("CheckBoxWindow", "Nothing selected"))
        self.check_16x16.setText(_translate("CheckBoxWindow", "16x16"))
        self.check_32x32.setText(_translate("CheckBoxWindow", "32x32"))
        self.check_64x64.setText(_translate("CheckBoxWindow", "64x64"))
        self.check_128x128.setText(_translate("CheckBoxWindow", "128x128"))
        self.check_192x192.setText(_translate("CheckBoxWindow", "192x192"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckBoxWindow = QtWidgets.QWidget()
    ui = Ui_CheckBoxWindow()
    ui.setupUi(CheckBoxWindow)
    CheckBoxWindow.show()
    sys.exit(app.exec_())
