from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.uic import loadUi
import sys
import pyodbc
from main import MainWindow  

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("dangnhap.ui", self)
        self.dangnhap_2.clicked.connect(self.login)
        self.dangxuat.clicked.connect(self.close)
        self.main_window = None  

    def login(self):
        username = self.tk.text()
        password = self.mk.text()
        server = 'QUANGMINH'  
        database = 'thucung'  
        db_username = 'sa'  
        db_password = 'sa'  
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={db_username};PWD={db_password}'

        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [User] WHERE username = ? AND PasswordHash = ?", (username, password))
            result = cursor.fetchone()
            if result:
                print("Đăng nhập thành công!")
                self.show_main_window()  # Hiển thị cửa sổ chính sau khi đăng nhập thành công
            else:
                print("Thông tin đăng nhập không đúng!")
                QMessageBox.warning(self, "Lỗi", "Thông tin đăng nhập không đúng!")

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Lỗi kết nối: {e}")
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {e}")

    def show_main_window(self):
        if self.main_window is None:
            self.main_window = MainWindow()  # Tạo ra cửa sổ chính (MainWindow)
        self.main_window.show()
        self.close()  # Đóng cửa sổ đăng nhập sau khi hiển thị cửa sổ chính

