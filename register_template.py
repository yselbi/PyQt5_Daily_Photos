###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : register_template
###############################################################



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_register_window(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(368, 389)
        self.groupBox = QtWidgets.QGroupBox(register_window)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 361))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_first_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(10, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_first_name.setFont(font)
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.lineEdit_last_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(180, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_last_name.setFont(font)
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username.setGeometry(QtCore.QRect(10, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_is_username_taken = QtWidgets.QLabel(self.groupBox)
        self.label_is_username_taken.setGeometry(QtCore.QRect(170, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_is_username_taken.setFont(font)
        self.label_is_username_taken.setText("")
        self.label_is_username_taken.setObjectName("label_is_username_taken")
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_password.setGeometry(QtCore.QRect(10, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_passowrds_match = QtWidgets.QLabel(self.groupBox)
        self.label_passowrds_match.setGeometry(QtCore.QRect(170, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_passowrds_match.setFont(font)
        self.label_passowrds_match.setText("")
        self.label_passowrds_match.setObjectName("label_passowrds_match")
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_confirm_password.setGeometry(QtCore.QRect(10, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_confirm_password.setFont(font)
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.pushButton_register = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_register.setGeometry(QtCore.QRect(100, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_register.setFont(font)
        self.pushButton_register.setObjectName("pushButton_register")

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "Registering Window"))
        self.groupBox.setTitle(_translate("register_window", "Register"))
        self.lineEdit_first_name.setPlaceholderText(_translate("register_window", "first name"))
        self.lineEdit_last_name.setPlaceholderText(_translate("register_window", "last name"))
        self.lineEdit_username.setPlaceholderText(_translate("register_window", "user name"))
        self.lineEdit_password.setPlaceholderText(_translate("register_window", "password"))
        self.lineEdit_confirm_password.setPlaceholderText(_translate("register_window", "confirm password"))
        self.pushButton_register.setText(_translate("register_window", "Register"))



