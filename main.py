#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap

from uis.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
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

    def open_file(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(self, "Project Data", "",
                                                               "Image files(*.png *.jpg *.jpeg *.bmp)")
        if all(self.file_path):
            print(self.file_path[0])
            self.load_image(self.file_path[0])
        else:
            QtWidgets.QMessageBox().critical(self, "Error", "File was not opened or does not exist.",
                                             QtWidgets.QMessageBox().Ok)

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.ui.label.setPixmap(pixmap.scaled(781, 501))

    def save_image(self):
        if self.file_path:
            print(self.file_path)
            options = QtWidgets.QFileDialog.Options()
            # options |= QtWidgets.QFileDialog.DontUseNativeDialog
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFileName", "./src",
                                                                 "Image files(*.png)",
                                                                 options=options)
            if file_name:
                try:
                    from PIL import Image
                    open_file_from_pil = Image.open(f"{self.file_path[0]}")
                    open_file_from_pil_copy = open_file_from_pil.resize((16, 16))
                    open_file_from_pil_copy.save(f"./src/{file_name}_16x16.png")
                except Exception as _error:
                    QtWidgets.QMessageBox().critical(self, "Error", f"{_error}",
                                                     QtWidgets.QMessageBox().Ok)
        else:
            QtWidgets.QMessageBox().critical(self, "Error", "File was not opened or does not exist.",
                                             QtWidgets.QMessageBox().Ok)

    def about_app(self):
        _text_about = r"""This app built with PyQt5. This application can resize the image to the size of the *.png icon.
Icons taken from https://www.flaticon.com/
        """
        QtWidgets.QMessageBox().about(self, "About this application", _text_about)

    def app_help(self):
        _text_help = r"""To convert an image to an icon size, you need to open this image, and then save this image.
When you saving image, don't to set the file extension, it will always be *.png.
By default, images are saved in the ./src folder, don't delete it.
"""
        QtWidgets.QMessageBox().about(self, "About this application", _text_help)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
