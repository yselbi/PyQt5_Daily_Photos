###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : main
###############################################################


from PyQt5.QtWidgets import QApplication, QMessageBox , QFileDialog
from PyQt5.QtCore import Qt
import sys
import db_connection
from login_window import Ui_Form
from register_window import RegisterForm
from mainwindow import MainWindow
import base64
import os
from PyQt5.QtGui import QPixmap
from change_pw import ChangePW

class LoginWindow(Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.pushButton_login_close.clicked.connect(self.close)

        # to open registering window
        self.register_form = RegisterForm()
        self.pushButton_register.clicked.connect(self.open_registering_form)

        # get username and password
        self.username = ""
        self.password = ""
        self.lineEdit_user_name.textChanged.connect(self.get_username_and_pass)
        self.lineEdit_password.textChanged.connect(self.get_username_and_pass)
        self.pushButton_signin.clicked.connect(self.login)

        # main window
        self.main_window = MainWindow()
        self.photo_title = ""
        self.photo_path = ""
        self.encoded_image = ""
        self.today = ""
        self.db_data = []

        self.main_window.pushButton_select_photo.clicked.connect(self.select_photo)
        self.main_window.lineEdit_title.textChanged.connect(self.set_photo_title)
        self.main_window.dateEdit.dateChanged.connect(self.set_today_date)

        #to save data into db
        self.main_window.pushButton_save.clicked.connect(self.write_into_db)

        #to show photo
        self.main_window.comboBox_saved_photos.currentIndexChanged.connect(self.show_data)


        # change password
        self.change_pass_win = ChangePW()
        self.main_window.pushButton_change_password.clicked.connect(self.show_pass_win)
        self.change_pass_win.lineEdit_current_password.textChanged.connect(self.check_current_pass)

        self.change_pass_win.lineEdit_new_password.textChanged.connect(self.check_new_pass)
        self.change_pass_win.lineEdit_confirm_new_password.textChanged.connect(self.check_new_pass)

        self.change_pass_win.pushButton_change_password.setEnabled(False)

        self.change_pass_win.pushButton_change_password.clicked.connect(self.change_current_pass)

    def show_pass_win(self):
        self.change_pass_win.show()

    def check_current_pass(self):
        if self.change_pass_win.lineEdit_current_password.text().__len__() > 0:
            if self.change_pass_win.lineEdit_current_password.text() != self.password:
                self.change_pass_win.label_current_password.setStyleSheet("color: rgb(255, 0,0)")
                self.change_pass_win.label_current_password.setText("wrong")
            else:
                self.change_pass_win.label_current_password.setStyleSheet("color: rgb(0, 200,0)")
                self.change_pass_win.label_current_password.setText("OK")

    def check_new_pass(self):
        if self.change_pass_win.lineEdit_new_password.text().__len__() >= 6:
            if self.change_pass_win.lineEdit_new_password.text().__len__() > 0 or \
                    self.change_pass_win.lineEdit_confirm_new_password.text().__len__() > 0:
                if self.change_pass_win.lineEdit_new_password.text() != self.change_pass_win.lineEdit_confirm_new_password.text():
                    self.change_pass_win.label_password_match.setStyleSheet("color: rgb(255, 0,0)")
                    self.change_pass_win.label_password_match.setText("wrong")
                else:
                    self.change_pass_win.label_password_match.setStyleSheet("color: rgb(0, 200,0)")
                    self.change_pass_win.label_password_match.setText("OK")
                    self.change_pass_win.pushButton_change_password.setEnabled(True)
        else:
            self.change_pass_win.label_password_match.setStyleSheet("color: rgb(255, 0,0)")
            self.change_pass_win.label_password_match.setText("at least 6 characters ")

    def change_current_pass(self):
        query = f"ALTER USER '{self.username}'@'localhost' IDENTIFIED BY '{self.change_pass_win.lineEdit_confirm_new_password.text()}'"
        ans = db_connection.connect_db("user", query, "w", self.username, self.password)
        if ans :
            self.show_message("your password changed successfully\n please login again", "T")
            self.change_pass_win.close()
        else:
            self.show_message("there is something wrong", "F")


        """ main window """

    def select_photo(self):
        self.photo_path, _ = QFileDialog.getOpenFileName(self, "open file", "./test", "*.jpg;; *.png;; All *.*")
        basename = os.path.basename(self.photo_path)
        self.main_window.label_photo_fullname.setText(basename)
        self.encode_image_mth()

    def encode_image_mth(self):
        with open(self.photo_path, 'rb') as photo:
            img = photo.read()
            self.encoded_image = base64.encodebytes(img)

    def set_photo_title(self):
        self.photo_title = self.main_window.lineEdit_title.text()


    def set_today_date(self):
        self.today = self.main_window.dateEdit.text()


    def write_into_db(self):
        data = (self.photo_title, self.today, self.encoded_image, self.username)
        save_query = "INSERT INTO records (photo_title, saved_date, photo, user_name) VALUES (%s, %s, %s, %s)"
        ans = db_connection.connect_db("user", save_query, "w", self.username, self.password, data)
        if ans :
            self.show_message("your photo saved successfully", "T")
            self.main_window.lineEdit_title.clear()
            self.main_window.label_photo_fullname.clear()
            self.db_data.clear()
            self.read_from_db()



    def read_from_db(self):
        read_query = f"SELECT * FROM records WHERE user_name='{self.username}'"
        data, is_connected = db_connection.connect_db("user", read_query, "r", self.username, self.password)
        self.main_window.comboBox_saved_photos.clear()
        self.main_window.comboBox_saved_photos.addItem("select photo")

        if is_connected:
            for each in data :
                self.main_window.comboBox_saved_photos.addItem(each[1])
                self.db_data.append(each)


    def show_data(self):
        if self.main_window.comboBox_saved_photos.currentIndex() >0 :
            data = self.db_data[self.main_window.comboBox_saved_photos.currentIndex() -1]

            self.main_window.textBrowser_show_info.clear()
            self.main_window.label_photo_display.clear()

            self.main_window.textBrowser_show_info.append(data[0])
            self.main_window.textBrowser_show_info.append(data[1])

            decoded_img = base64.decodebytes(data[2])
            qmap = QPixmap()
            if qmap.loadFromData(decoded_img):
                self.main_window.label_photo_display.setPixmap(qmap)



    """ login part """

    def get_username_and_pass(self):
        self.username = self.lineEdit_user_name.text()
        self.password = self.lineEdit_password.text()

    def login(self):
        try:
            query = f"SELECT * FROM users_info WHERE user_name='{self.username}'"
            data, is_connected = db_connection.connect_db("user", query, "r", self.username, self.password)

            if is_connected:
               self.main_window.label_welcome_msg.setText(f" Welcome {data[0][1]} {data[0][2]}")
               self.main_window.show()
               self.login_window.hide()
               self.read_from_db()


        except:
           self.show_message("invalid username or password\n please try again", "F")

    def show_message(self, msg, choice="F/T"):
        msgbox = QMessageBox()

        if choice == "T":
            msgbox.setWindowTitle("Info")
            msgbox.setIcon(QMessageBox.Information)
        else:
            msgbox.setWindowTitle("Warning")
            msgbox.setIcon(QMessageBox.Critical)
        msgbox.setText(msg)
        msgbox.show()
        msgbox.exec_()

    def open_registering_form(self):
        self.register_form.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    logingform = LoginWindow()
    logingform.show()
    sys.exit(app.exec_())