from PyQt6.QtWidgets import QApplication
import sys
from log import LoginWindow  

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show() 

    sys.exit(app.exec())

