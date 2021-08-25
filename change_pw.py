###############################################################
#
#  project name :  Daily Photos
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 25.08.2021
#  Note: To be able to use this software you must install MySQL
#         database management system
# File Name : change_pw
###############################################################


from change_pw_template import Ui_ChangePWForm


class ChangePW(Ui_ChangePWForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_change_password.setEnabled(False)



