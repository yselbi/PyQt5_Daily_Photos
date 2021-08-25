###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : login_template
###############################################################


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(455, 541)
        self.login_window = QtWidgets.QFrame(Form)
        self.login_window.setGeometry(QtCore.QRect(10, 10, 431, 511))
        self.login_window.setStyleSheet("#login_window{\n"
"\n"
"background-image: url(images/login_bg.jpg);\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"#pushButton_login_close{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 59, 42);\n"
"border-radius:4px;\n"
"border: 1px solid  rgb(85, 85, 85);\n"
"}\n"
"\n"
"#pushButton_login_close:hover{\n"
"background-color: rgb(172, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"#lineEdit_user_name, #lineEdit_password{\n"
"border-radius:20px;\n"
"border: 1px solid  rgb(0, 0, 255);\n"
"\n"
"}\n"
"\n"
"#pushButton_signin,#pushButton_register{\n"
"background-image: url(images/btn.png);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:4px;\n"
"}\n"
"\n"
"#pushButton_signin:hover,#pushButton_register:hover{\n"
"border:2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"#pushButton_signin:pressed,#pushButton_register:pressed{\n"
"border:3px solid rgb(0, 176, 176);\n"
"color:rgb(0, 255, 255);\n"
"\n"
"}")
        self.login_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_window.setObjectName("login_window")
        self.pushButton_login_close = QtWidgets.QPushButton(self.login_window)
        self.pushButton_login_close.setGeometry(QtCore.QRect(374, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login_close.setFont(font)
        self.pushButton_login_close.setObjectName("pushButton_login_close")
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.login_window)
        self.lineEdit_user_name.setGeometry(QtCore.QRect(85, 207, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_user_name.setFont(font)
        self.lineEdit_user_name.setStyleSheet("")
        self.lineEdit_user_name.setText("")
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.label = QtWidgets.QLabel(self.login_window)
        self.label.setGeometry(QtCore.QRect(150, 50, 141, 111))
        self.label.setStyleSheet("background-image: url(:/logo/1500x1000.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/1500x1000.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_window)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 267, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_signin = QtWidgets.QPushButton(self.login_window)
        self.pushButton_signin.setGeometry(QtCore.QRect(130, 330, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_signin.setFont(font)
        self.pushButton_signin.setStyleSheet("")
        self.pushButton_signin.setFlat(False)
        self.pushButton_signin.setObjectName("pushButton_signin")
        self.pushButton_register = QtWidgets.QPushButton(self.login_window)
        self.pushButton_register.setGeometry(QtCore.QRect(130, 380, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_register.setFont(font)
        self.pushButton_register.setStyleSheet("")
        self.pushButton_register.setFlat(False)
        self.pushButton_register.setObjectName("pushButton_register")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_login_close.setText(_translate("Form", "X"))
        self.lineEdit_user_name.setPlaceholderText(_translate("Form", " your name"))
        self.lineEdit_password.setPlaceholderText(_translate("Form", " password"))
        self.pushButton_signin.setText(_translate("Form", "Sign In"))
        self.pushButton_register.setText(_translate("Form", "Register"))
