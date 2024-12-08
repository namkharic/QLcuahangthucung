from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
import sys
import pyodbc
def fetch_data(table_name):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=QUANGMINH;'
        'DATABASE=thucung;'
        'UID=sa;'
        'PWD=sa'
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    conn.close()
    return columns, rows

def insert_data(table_name, columns, values):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=QUANGMINH;'
        'DATABASE=thucung;'
        'UID=sa;'
        'PWD=sa'
    )
    cursor = conn.cursor()
    placeholders = ','.join('?' * len(values))
    sql = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def update_data(table_name, column_values, condition):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=QUANGMINH;'
        'DATABASE=thucung;'
        'UID=sa;'
        'PWD=sa'
    )
    cursor = conn.cursor()
    set_clause = ','.join(f"{column} = ?" for column in column_values.keys())
    sql = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    cursor.execute(sql, list(column_values.values()))
    conn.commit()
    conn.close()

def delete_data(table_name, condition):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=QUANGMINH;'
        'DATABASE=thucung;'
        'UID=sa;'
        'PWD=sa'
    )
    cursor = conn.cursor()
    sql = f"DELETE FROM {table_name} WHERE {condition}"
    cursor.execute(sql)
    conn.commit()
    conn.close()

# Lớp MainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Home.ui', self)

        # Thiết lập thông tin bảng và kết nối sự kiện
        self.tables = {
            0: {'name': 'ThongKe', 'btnAdd': self.them1, 'btnUpdate': self.sua1, 'btnDelete': self.xoa1, 'line_edits': [self.ntk, self.tdh, self.tdt], 'tableWidget': self.doanhthu},
            1: {'name': '[User]', 'btnAdd': self.add, 'btnUpdate': self.edit, 'btnDelete': self.delete1, 'line_edits': [ self.name, self.pw, self.ho, self.ten, self.email, self.sdt, self.dc, self.cv], 'tableWidget': self.tabuser},
            2: {'name': 'KhachHang', 'btnAdd': self.add2, 'btnUpdate': self.edit2, 'btnDelete': self.delete2, 'line_edits': [ self.ht, self.dchi, self.sdthoai], 'tableWidget': self.tabkhachhang},
            3: {'name': 'ThuCung', 'btnAdd': self.add3, 'btnUpdate': self.edit3, 'btnDelete': self.delete3, 'line_edits': [self.ttc, self.loai, self.giong,self.tuoi, self.sl, self.gia], 'tableWidget': self.tabthucung},
            4: {'name': 'DonHang', 'btnAdd': self.add4, 'btnUpdate': self.edit4, 'btnDelete': self.delete4, 'line_edits': [self.mkh2, self.ndh, self.tt], 'tableWidget': self.tabdonhang},
            5: {'name': 'ThanhToan', 'btnAdd': self.add_2, 'btnUpdate': self.edit_2, 'btnDelete': self.delete_2, 'line_edits': [self.mdh1, self.mtc2, self.ntt, self.st,self.sl1,self.dongia], 'tableWidget': self.thanhtoan},
            6: {'name': 'HoaDon', 'btnAdd': self.themhd, 'btnUpdate': self.suahd, 'btnDelete': self.xoahd, 'line_edits': [self.mdh,self.nph,self.nttoan,self.ttien], 'tableWidget': self.hoadon},
        }
        self.tabWidget.currentChanged.connect(self.update_table)
        for tab_info in self.tables.values():
            tab_info['btnAdd'].clicked.connect(self.add_record)
            tab_info['btnUpdate'].clicked.connect(self.update_record)
            tab_info['btnDelete'].clicked.connect(self.delete_record)

        # Kết nối sự kiện khi bấm vào dòng trong bảng để hiển thị dữ liệu lên các QLineEdit
        for tab_info in self.tables.values():
            table_widget = tab_info.get('tableWidget')
            if table_widget:
                table_widget.cellClicked.connect(self.display_selected_record)
        #tạo nút đăng xuất        
        self.thoat1.clicked.connect(self.logout)  
        # Khởi tạo bảng dữ liệu ban đầu
        self.update_table(0)

    # Phương thức cập nhật bảng dữ liệu khi thay đổi tab
    def update_table(self, index):
        table_info = self.tables.get(index)
        if table_info:
            table_name = table_info['name']
            columns, data = fetch_data(table_name)
            current_tab_widget = self.tabWidget.widget(index)
            table_widget = current_tab_widget.findChild(QtWidgets.QTableWidget)
            if table_widget:
                table_widget.setRowCount(len(data))
                table_widget.setColumnCount(len(columns))
                table_widget.setHorizontalHeaderLabels(columns)
                for row_idx, row_data in enumerate(data):
                    for col_idx, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        table_widget.setItem(row_idx, col_idx, item)

    # Phương thức hiển thị dữ liệu từ dòng được chọn lên các QLineEdit
    def display_selected_record(self, row, col):
        index = self.tabWidget.currentIndex()
        table_info = self.tables.get(index)
        if table_info:
            table_name = table_info['name']
            current_tab_widget = self.tabWidget.widget(index)
            table_widget = current_tab_widget.findChild(QtWidgets.QTableWidget)
            if table_widget:
                line_edits = table_info.get('line_edits', [])
                for i, line_edit in enumerate(line_edits):
                    line_edit.setText(table_widget.item(row, i + 1).text())

    # Phương thức thêm bản ghi mới
    def add_record(self):
        index = self.tabWidget.currentIndex()
        table_info = self.tables.get(index)
        if table_info:
            table_name = table_info['name']
            line_edits = table_info.get('line_edits', [])
            columns, _ = fetch_data(table_name)
            columns = columns[1:]  # Loại bỏ cột IDENTITY (cột tự tăng)
            values = [lineEdit.text() for lineEdit in line_edits]
            try:
                insert_data(table_name, columns, values)
                self.update_table(index)
            except pyodbc.Error as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể thêm dữ liệu: {e}")

    # Phương thức cập nhật bản ghi
    def update_record(self):
        index = self.tabWidget.currentIndex()
        table_info = self.tables.get(index)
        if table_info:
            table_name = table_info['name']
            line_edits = table_info.get('line_edits', [])
            columns, _ = fetch_data(table_name)
            columns = columns[1:]  
            values = [lineEdit.text() for lineEdit in line_edits]
            table_widget = table_info.get('tableWidget')
            selected_rows = table_widget.selectedItems()
            if selected_rows:
                row = selected_rows[0].row()
                primary_key_column = table_widget.horizontalHeaderItem(0).text()
                primary_key_value = table_widget.item(row, 0).text()
                condition = f"{primary_key_column} = '{primary_key_value}'"
                column_values = dict(zip(columns, values))
                try:
                    update_data(table_name, column_values, condition)
                    self.update_table(index)
                except pyodbc.Error as e:
                    QMessageBox.critical(self, "Lỗi", f"Không thể cập nhật dữ liệu: {e}")

    # Phương thức xóa bản ghi
    def delete_record(self):
        index = self.tabWidget.currentIndex()
        table_info = self.tables.get(index)
        if table_info:
            table_name = table_info['name']
            table_widget = table_info.get('tableWidget')
            selected_rows = table_widget.selectedItems()
            if selected_rows:
                row = selected_rows[0].row()
                primary_key_column = table_widget.horizontalHeaderItem(0).text()
                primary_key_value = table_widget.item(row, 0).text()
                condition = f"{primary_key_column} = '{primary_key_value}'"
                try:
                    delete_data(table_name, condition)
                    self.update_table(index)
                except pyodbc.Error as e:
                    QMessageBox.critical(self, "Lỗi", f"Không thể xóa dữ liệu: {e}")
     # Phương thức đăng xuất
    def logout(self):
        self.close()  
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
