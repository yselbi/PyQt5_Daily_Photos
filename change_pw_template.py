###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : change_pw_template
###############################################################



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_ChangePWForm( QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, ChangePWForm):
        ChangePWForm.setObjectName("ChangePWForm")
        ChangePWForm.resize(345, 279)
        self.lineEdit_current_password = QtWidgets.QLineEdit(ChangePWForm)
        self.lineEdit_current_password.setGeometry(QtCore.QRect(30, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_current_password.setFont(font)
        self.lineEdit_current_password.setText("")
        self.lineEdit_current_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_current_password.setObjectName("lineEdit_current_password")
        self.lineEdit_new_password = QtWidgets.QLineEdit(ChangePWForm)
        self.lineEdit_new_password.setGeometry(QtCore.QRect(30, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_new_password.setFont(font)
        self.lineEdit_new_password.setText("")
        self.lineEdit_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")
        self.lineEdit_confirm_new_password = QtWidgets.QLineEdit(ChangePWForm)
        self.lineEdit_confirm_new_password.setGeometry(QtCore.QRect(30, 140, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_confirm_new_password.setFont(font)
        self.lineEdit_confirm_new_password.setText("")
        self.lineEdit_confirm_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_new_password.setObjectName("lineEdit_confirm_new_password")
        self.pushButton_change_password = QtWidgets.QPushButton(ChangePWForm)
        self.pushButton_change_password.setGeometry(QtCore.QRect(60, 200, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_change_password.setFont(font)
        self.pushButton_change_password.setObjectName("pushButton_change_password")
        self.label_current_password = QtWidgets.QLabel(ChangePWForm)
        self.label_current_password.setGeometry(QtCore.QRect(200, 40, 121, 31))
        self.label_current_password.setText("")
        self.label_current_password.setObjectName("label_current_password")
        self.label_password_match = QtWidgets.QLabel(ChangePWForm)
        self.label_password_match.setGeometry(QtCore.QRect(200, 140, 121, 31))
        self.label_password_match.setText("")
        self.label_password_match.setObjectName("label_password_match")

        self.retranslateUi(ChangePWForm)
        QtCore.QMetaObject.connectSlotsByName(ChangePWForm)

    def retranslateUi(self, ChangePWForm):
        _translate = QtCore.QCoreApplication.translate
        ChangePWForm.setWindowTitle(_translate("ChangePWForm", "Change password "))
        self.lineEdit_current_password.setPlaceholderText(_translate("ChangePWForm", "current password"))
        self.lineEdit_new_password.setPlaceholderText(_translate("ChangePWForm", "new password"))
        self.lineEdit_confirm_new_password.setPlaceholderText(_translate("ChangePWForm", "confirm password"))
        self.pushButton_change_password.setText(_translate("ChangePWForm", "Submit"))


