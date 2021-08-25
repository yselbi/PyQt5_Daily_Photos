from register_template import Ui_register_window
import db_connection
###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : register_window
###############################################################


from PyQt5.QtWidgets import QMessageBox

class RegisterForm(Ui_register_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_register.setEnabled(False)

        self.first_pass = ""
        self.second_pass = ""
        # to enable register button
        self.lineEdit_first_name.textChanged.connect(self.enable_register_button)
        self.lineEdit_last_name.textChanged.connect(self.enable_register_button)
        self.lineEdit_username.textChanged.connect(self.enable_register_button)
        self.lineEdit_password.textChanged.connect(self.enable_register_button)
        self.lineEdit_confirm_password.textChanged.connect(self.enable_register_button)

        # to check username
        self.lineEdit_username.textChanged.connect(self.check_username)

        # to check password matching
        self.lineEdit_password.textChanged.connect(self.check_password_matching)
        self.lineEdit_confirm_password.textChanged.connect(self.check_password_matching)

        # register new user
        self.pushButton_register.clicked.connect(self.register_new_user)

    def register_new_user(self):
        create_new_user = f"CREATE USER '{self.lineEdit_username.text()}'@'localhost' IDENTIFIED BY '{self.first_pass}'"
        ans = db_connection.connect_db("admin", create_new_user, "w")
        if ans :
            grant_user = f"GRANT ALL PRIVILEGES ON *.* TO '{self.lineEdit_username.text()}'@'localhost'"
            db_connection.connect_db("admin", grant_user, "w")
            insert_info = f"INSERT INTO users_info VALUES('{self.lineEdit_username.text()}', '{self.lineEdit_first_name.text()}'," \
                          f" '{self.lineEdit_last_name.text()}')"
            db_connection.connect_db("admin", insert_info, "w")
            self.show_message()
            self.close()

    def show_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Successfully Registered")
        msg.show()
        msg.exec_()

    def check_password_matching(self):
        self.first_pass = self.lineEdit_password.text()
        self.second_pass = self.lineEdit_confirm_password.text()
        if self.first_pass == self.second_pass:
            if self.first_pass.__len__() >=6 :
                self.notify_user("password", True, "OK")
            else:
                self.notify_user("password", False, "at least 6 characters")
        else:
            self.notify_user("password", False, "Not Match")



    def check_username(self):
        if self.lineEdit_username.text().__len__() >=5 :
            query = f"SELECT user_name FROM users_info WHERE user_name ='{self.lineEdit_username.text()}'"
            ans = db_connection.connect_db("admin", query, "r")
            if not ans:
                self.notify_user("username",  True, "Available")
            else:
                self.notify_user("username", False, "Not Available")

    def notify_user(self, type="", flag=False, msg=""):
        if type == "username":
            if not flag :
                self.label_is_username_taken.setStyleSheet("color: rgb(255, 0, 0)")
                self.label_is_username_taken.setText(msg)
            else:
                self.label_is_username_taken.setStyleSheet("color: rgb(0, 200, 0)")
                self.label_is_username_taken.setText(msg)
        else:
            if not flag :
                self.label_passowrds_match.setStyleSheet("color: rgb(255, 0, 0)")
                self.label_passowrds_match.setText(msg)
            else:
                self.label_passowrds_match.setStyleSheet("color: rgb(0, 200, 0)")
                self.label_passowrds_match.setText(msg)


    def enable_register_button(self):
       if self.lineEdit_first_name.text().__len__() >=5 and self.lineEdit_last_name.text().__len__() >= 5 \
           and self.lineEdit_username.text().__len__() >=5 and self.lineEdit_password.text().__len__() >= 6 \
               and self.lineEdit_confirm_password.text().__len__() >= 6:
           self.pushButton_register.setEnabled(True)
       else:
           self.pushButton_register.setEnabled(False)