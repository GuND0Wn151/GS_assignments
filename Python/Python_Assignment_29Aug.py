rom PyQt6 import QtWidgets,uic
import sys
username_main='mac'
password_main='password'
def gotoRegister():
    register.show()
    login.close()

def validate():
    global username_main,password_main
    username=login.username.text()
    password=login.password.text()
    if username==username_main and password==password_main:
        login.status.setText("Logged In")
    else:
        login.status.setText("")
    
def register_user():
    global username_main,password_main
    register.rstatus.setText("Done")
    username_main=register.rusername.text()
    password_main=register.rpass.text()

def gotoLogin():
    login.show()
    register.close()

demo = QtWidgets.QApplication([])
    
login = uic.loadUi("/Users/kguptha/Desktop/login.ui")
register=uic.loadUi("/Users/kguptha/Desktop/register.ui")

login.show()

login.registe.clicked.connect(gotoRegister)
login.loginbtn.clicked.connect(validate)
register.rregister.clicked.connect(register_user)
register.rlogin.clicked.connect(gotoLogin)
sys.exit(demo.exec())
