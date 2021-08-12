#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap

from uis.main_window import Ui_MainWindow
from uis.check_box_window import Ui_CheckBoxWindow


CHECK_BOX_DICT = {"16x16": 1, "32x32": 0, "64x64": 0, "128x128": 0, "192x192": 0}


def null_check_box_dict():
    for key, value in CHECK_BOX_DICT.items():
        CHECK_BOX_DICT[key] = 0


class MainWindow(QtWidgets.QMainWindow):
    """ Main Window """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.file_path = ""

    def init_ui(self):
        self.setWindowTitle("Convert image to icon")
        self.setWindowIcon(QtGui.QIcon("./icons/app_icon.png"))
        self.menu_bar()

    def menu_bar(self):
        # menu file
        self.ui.actionExit.setStatusTip("Close the application")
        self.ui.actionExit.triggered.connect(QtWidgets.qApp.quit)

        self.ui.actionOpen_file.setStatusTip("Open file to Tab_1")
        self.ui.actionOpen_file.triggered.connect(self.open_file)

        self.ui.actionSave_file.setStatusTip("Save your compressed files")
        self.ui.actionSave_file.triggered.connect(self.save_image)

        # menu help
        self.ui.actionAbout.setStatusTip("About this app")
        self.ui.actionAbout.triggered.connect(self.about_app)

        self.ui.actionHelp.setStatusTip("About this app")
        self.ui.actionHelp.triggered.connect(self.app_help)

        self.ui.actionIcon_size.triggered.connect(self.icon_size)

    @staticmethod
    def icon_size():
        check_box_widget = CheckBoxWindow()
        check_box_widget.show()

    def open_file(self):
        _file_path = self.file_path
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(self, "Project Data", "",
                                                               "Image files(*.png *.jpg *.jpeg *.bmp)")
        if all(self.file_path):
            print(self.file_path[0])
            self.load_image(self.file_path[0])
        else:
            self.file_path = _file_path
            QtWidgets.QMessageBox().critical(self, "Error", "File was not opened or does not exist.",
                                             QtWidgets.QMessageBox().Ok)

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.ui.label.setPixmap(pixmap.scaled(781, 501))

    def save_image(self):
        _file_path = self.file_path
        if self.file_path:
            print(self.file_path)
            options = QtWidgets.QFileDialog.Options()
            # options |= QtWidgets.QFileDialog.DontUseNativeDialog
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFileName", "",
                                                                 "Image files(*.png)",
                                                                 options=options)
            if file_name:
                try:
                    from PIL import Image
                    for key, value in CHECK_BOX_DICT.items():
                        if CHECK_BOX_DICT[key] == 1:
                            open_file_from_pil = Image.open(f"{self.file_path[0]}")
                            icon_size = key.split("x")
                            icon_size = int(icon_size[0]), int(icon_size[1])
                            open_file_from_pil_copy = open_file_from_pil.resize(icon_size)
                            open_file_from_pil_copy.save(f"{file_name}_{icon_size}.png")
                except Exception as _error:
                    QtWidgets.QMessageBox().critical(self, "Error", f"{_error}",
                                                     QtWidgets.QMessageBox().Ok)
            else:
                QtWidgets.QMessageBox().critical(self, "Error", "Error while saving file, canceled.",
                                                 QtWidgets.QMessageBox().Ok)
        else:
            self.file_path = _file_path
            QtWidgets.QMessageBox().critical(self, "Error", "File was not opened or does not exist.",
                                             QtWidgets.QMessageBox().Ok)

    def about_app(self):
        _text_about = r"""This app built with PyQt5. This application can resize the image to the *.png icon.
Icons taken from https://www.flaticon.com/
        """
        QtWidgets.QMessageBox().about(self, "About this application", _text_about)

    def app_help(self):
        _text_help = r"""To convert an image to an icon size, you need to open this image, and then save this image.
When you saving image, don't to set the file extension, it will always be *.png.
"""
        QtWidgets.QMessageBox().about(self, "About this application", _text_help)


class CheckBoxWindow(QtWidgets.QWidget):
    """ Check Box Window """
    def __init__(self):
        super(CheckBoxWindow, self).__init__()
        self.ui = Ui_CheckBoxWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.nothing_selected_text = "Nothing selected"
        self.selected_values_text = ""

    def init_ui(self):
        self.setWindowTitle("Choose size of icon")
        self.ui.label_text_for_user = "Select sized that you need:"

        self.ui.check_16x16.stateChanged.connect(lambda: self.selected_value(self.ui.check_16x16))
        self.ui.check_32x32.stateChanged.connect(lambda: self.selected_value(self.ui.check_32x32))
        self.ui.check_64x64.stateChanged.connect(lambda: self.selected_value(self.ui.check_64x64))
        self.ui.check_128x128.stateChanged.connect(lambda: self.selected_value(self.ui.check_128x128))
        self.ui.check_192x192.stateChanged.connect(lambda: self.selected_value(self.ui.check_192x192))

    def selected_value(self, btn):
        if self.selected_values_text:
            _str = self.selected_values_text
            selected_values = _str.split(" ,")
            self.selected_values_text = ""
            for value in selected_values:
                if btn.text() != value:
                    if self.selected_values_text == "":
                        self.selected_values_text = value
                    else:
                        self.selected_values_text += " ," + value
            if btn.isChecked():
                if self.selected_values_text == "":
                    self.selected_values_text = btn.text()
                else:
                    self.selected_values_text += " ," + btn.text()
        else:
            if btn.isChecked():
                if self.selected_values_text == "":
                    self.selected_values_text = btn.text()
                else:
                    self.selected_values_text += " ," + btn.text()
        if self.selected_values_text == "":
            self.ui.label_selected_values.setText('You have selected \n' + self.nothing_selected_text)
            CHECK_BOX_DICT["16x16"] = 1
        else:
            self.ui.label_selected_values.setText('You have selected \n' + self.selected_values_text)
            selected_values_text_list = self.selected_values_text.split(" ,")
            null_check_box_dict()
            for key in range(len(selected_values_text_list)):
                if CHECK_BOX_DICT[selected_values_text_list[key]] == 0:
                    CHECK_BOX_DICT[selected_values_text_list[key]] = 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
