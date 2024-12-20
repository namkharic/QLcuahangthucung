from PyQt6 import QtCore, QtGui, QtWidgets
import hinh 

class Ui_formlogin(object):
    def setupUi(self, formlogin):
        formlogin.setObjectName("formlogin")
        formlogin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=formlogin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 731, 541))
        self.widget.setStyleSheet("background-image: url(:/pic/hinhanh/dangnhap.jpg);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(230, 40, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(160, 140, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(160, 190, 71, 16))
        self.label_3.setObjectName("label_3")
        self.dangnhap_2 = QtWidgets.QPushButton(parent=self.widget)
        self.dangnhap_2.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.dangnhap_2.setObjectName("dangnhap_2")
        self.dangxuat = QtWidgets.QPushButton(parent=self.widget)
        self.dangxuat.setGeometry(QtCore.QRect(440, 300, 93, 28))
        self.dangxuat.setObjectName("dangxuat")
        self.tk = QtWidgets.QLineEdit(parent=self.widget)
        self.tk.setGeometry(QtCore.QRect(270, 140, 181, 22))
        self.tk.setObjectName("tk")
        self.mk = QtWidgets.QLineEdit(parent=self.widget)
        self.mk.setGeometry(QtCore.QRect(270, 190, 181, 22))
        self.mk.setObjectName("mk")
        formlogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=formlogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        formlogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=formlogin)
        self.statusbar.setObjectName("statusbar")
        formlogin.setStatusBar(self.statusbar)

        self.retranslateUi(formlogin)
        QtCore.QMetaObject.connectSlotsByName(formlogin)

    def retranslateUi(self, formlogin):
        _translate = QtCore.QCoreApplication.translate
        formlogin.setWindowTitle(_translate("formlogin", "MainWindow"))
        self.label.setText(_translate("formlogin", "Đăng nhập vào ứng dụng"))
        self.label_2.setText(_translate("formlogin", "Tài Khoản: "))
        self.label_3.setText(_translate("formlogin", "Mật Khẩu: "))
        self.dangnhap_2.setText(_translate("formlogin", "Đăng Nhập"))
        self.dangxuat.setText(_translate("formlogin", "Đăng Xuất"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_formlogin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
