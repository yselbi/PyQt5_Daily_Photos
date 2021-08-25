###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : login_window
###############################################################

from PyQt5.QtCore import  Qt
from login_template import Ui_Form

class Login(Ui_Form):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
