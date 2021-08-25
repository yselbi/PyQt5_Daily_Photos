###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : mainwindow_template
###############################################################



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_input_fields = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_input_fields.setGeometry(QtCore.QRect(20, 70, 351, 391))
        self.groupBox_input_fields.setObjectName("groupBox_input_fields")
        self.lineEdit_title = QtWidgets.QLineEdit(self.groupBox_input_fields)
        self.lineEdit_title.setGeometry(QtCore.QRect(20, 40, 151, 31))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.lineEdit_title.setPlaceholderText("photo title")
        self.pushButton_select_photo = QtWidgets.QPushButton(self.groupBox_input_fields)
        self.pushButton_select_photo.setGeometry(QtCore.QRect(220, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_select_photo.setFont(font)
        self.pushButton_select_photo.setObjectName("pushButton_select_photo")
        self.label_photo_fullname = QtWidgets.QLabel(self.groupBox_input_fields)
        self.label_photo_fullname.setGeometry(QtCore.QRect(20, 90, 191, 16))
        self.label_photo_fullname.setObjectName("label_photo_fullname")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_input_fields)
        self.dateEdit.setGeometry(QtCore.QRect(20, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_input_fields)
        self.pushButton_save.setGeometry(QtCore.QRect(60, 230, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_welcome_msg = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome_msg.setGeometry(QtCore.QRect(20, 10, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_welcome_msg.setFont(font)
        self.label_welcome_msg.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_welcome_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_welcome_msg.setObjectName("label_welcome_msg")
        self.groupBox_saved_data = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_saved_data.setGeometry(QtCore.QRect(380, 70, 371, 391))
        self.groupBox_saved_data.setObjectName("groupBox_saved_data")
        self.label_photo_display = QtWidgets.QLabel(self.groupBox_saved_data)
        self.label_photo_display.setGeometry(QtCore.QRect(40, 170, 321, 201))
        self.label_photo_display.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_photo_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_photo_display.setText("")
        self.label_photo_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_photo_display.setObjectName("label_photo_display")
        self.comboBox_saved_photos = QtWidgets.QComboBox(self.groupBox_saved_data)
        self.comboBox_saved_photos.setGeometry(QtCore.QRect(120, 30, 241, 31))
        self.comboBox_saved_photos.setObjectName("comboBox_saved_photos")
        self.textBrowser_show_info = QtWidgets.QTextBrowser(self.groupBox_saved_data)
        self.textBrowser_show_info.setGeometry(QtCore.QRect(40, 70, 321, 91))
        self.textBrowser_show_info.setObjectName("textBrowser_show_info")
        self.pushButton_change_password = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change_password.setGeometry(QtCore.QRect(600, 12, 151, 41))
        self.pushButton_change_password.setObjectName("pushButton_change_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Daily Photos"))
        self.groupBox_input_fields.setTitle(_translate("MainWindow", "input fields"))
        self.pushButton_select_photo.setText(_translate("MainWindow", "Select a photo ..."))
        self.label_photo_fullname.setText(_translate("MainWindow", "-"))
        self.pushButton_save.setText(_translate("MainWindow", "Save into database"))
        self.label_welcome_msg.setText(_translate("MainWindow", "Welcome ..."))
        self.groupBox_saved_data.setTitle(_translate("MainWindow", "Saved Data"))
        self.pushButton_change_password.setText(_translate("MainWindow", "Change Password"))

