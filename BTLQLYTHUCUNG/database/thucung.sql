-- Tạo database mới nếu chưa tồn tại
CREATE DATABASE thucung;
USE thucung;

-- Tạo bảng User
CREATE TABLE [User] (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(255) NOT NULL,  -- Mật khẩu đã hash để bảo mật
    Ho NVARCHAR(50),
    Ten NVARCHAR(50),
    Email NVARCHAR(50) UNIQUE,
    SoDienThoai NVARCHAR(15),
    DiaChi NVARCHAR(100),
    Role NVARCHAR(50) NOT NULL  -- Vai trò của người dùng: 'Nhân viên', 'Quản lý',
);

-- Tạo bảng Nhân viên
CREATE TABLE NhanVien (
    MaNhanVien INT PRIMARY KEY IDENTITY(1,1),
    UserID INT UNIQUE,
    FOREIGN KEY (UserID) REFERENCES [User](UserID)
);

-- Tạo bảng Quản lý
CREATE TABLE QuanLy (
    MaQuanLy INT PRIMARY KEY IDENTITY(1,1),
    UserID INT UNIQUE,
    FOREIGN KEY (UserID) REFERENCES [User](UserID)
);

-- Tạo bảng Khách hàng
CREATE TABLE KhachHang (
    MaKhachHang INT PRIMARY KEY IDENTITY(1,1),
    HoTen NVARCHAR(100) NOT NULL,
    DiaChi NVARCHAR(200),
    DienThoai NVARCHAR(20)
);

-- Tạo bảng Thú cưng
CREATE TABLE ThuCung (
    MaThuCung INT PRIMARY KEY IDENTITY(1,1),
    TenThuCung NVARCHAR(100) NOT NULL,
    Loai NVARCHAR(50),
    Giong NVARCHAR(50),
    Tuoi INT,
    SoLuong INT,  -- Thêm cột số lượng thú cưng
    DonGia DECIMAL(10, 2)  -- Thêm cột đơn giá
);

-- Tạo bảng Đơn hàng
CREATE TABLE DonHang (
    MaDonHang INT PRIMARY KEY IDENTITY(1,1),
    MaKhachHang INT,
    NgayDatHang DATE,
    TongTien DECIMAL(10, 2),
    FOREIGN KEY (MaKhachHang) REFERENCES KhachHang(MaKhachHang)
);

-- Tạo bảng Thanh toán
CREATE TABLE ThanhToan (
    MaThanhToan INT PRIMARY KEY IDENTITY(1,1),
    MaDonHang INT,
    MaThuCung INT,
    NgayThanhToan DATE,
    SoTien DECIMAL(10, 2),
    SoLuong INT,  -- Thêm cột số lượng thú cưng
    DonGia DECIMAL(10, 2),  -- Thêm cột đơn giá
    FOREIGN KEY (MaDonHang) REFERENCES DonHang(MaDonHang),
    FOREIGN KEY (MaThuCung) REFERENCES ThuCung(MaThuCung)
);

-- Tạo bảng Hóa đơn
CREATE TABLE HoaDon (
    MaHoaDon INT PRIMARY KEY IDENTITY(1,1),
    MaDonHang INT,
    NgayPhatHanh DATE,
    NgayThanhToan DATE,
    TongTien DECIMAL(10, 2),
    FOREIGN KEY (MaDonHang) REFERENCES DonHang(MaDonHang)
);

-- Tạo bảng Chi tiết đơn hàng
CREATE TABLE ChiTietDonHang (
    MaChiTietDonHang INT PRIMARY KEY IDENTITY(1,1),
    MaDonHang INT,
    MaThuCung INT,
    SoLuongDonHang INT,
    DonGia DECIMAL(10, 2),
    FOREIGN KEY (MaDonHang) REFERENCES DonHang(MaDonHang),
    FOREIGN KEY (MaThuCung) REFERENCES ThuCung(MaThuCung)
);

-- Tạo bảng Thống kê
CREATE TABLE ThongKe (
    MaThongKe INT PRIMARY KEY IDENTITY(1,1),
    NgayThongKe DATE,
    TongSoDonHang INT,
    TongDoanhThu DECIMAL(15, 2)
);

-- Tạo bảng Login
CREATE TABLE Login (
    LoginID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(255) NOT NULL,  -- Mật khẩu đã hash để bảo mật
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES [User](UserID)
);

-- Thêm các bản ghi vào bảng User
INSERT INTO [User] (Username, PasswordHash, Ho, Ten, Email, SoDienThoai, DiaChi, Role)
VALUES 
    ('employee1', '123', 'Nguyen', 'Van A', 'employee1@example.com', '123456789', '123 ABC Street, City', 'Nhân viên'),
    ('manager1', '123', 'Tran', 'Thi B', 'manager1@example.com', '987654321', '456 XYZ Street, City', 'Quản lý');

-- Thêm nhân viên vào bảng NhanVien (lấy UserID từ bảng User)
INSERT INTO NhanVien (UserID)
VALUES 
    ((SELECT UserID FROM [User] WHERE Username = 'employee1'));

-- Thêm quản lý vào bảng QuanLy (lấy UserID từ bảng User)
INSERT INTO QuanLy (UserID)
VALUES 
    ((SELECT UserID FROM [User] WHERE Username = 'manager1'));

-- Thêm thông tin đăng nhập vào bảng Login (lấy từ bảng User)
INSERT INTO Login (Username, PasswordHash, UserID)
VALUES 
    ('employee1', '123', (SELECT UserID FROM [User] WHERE Username = 'employee1')),
    ('manager1', '123', (SELECT UserID FROM [User] WHERE Username = 'manager1'));

-- Thêm khách hàng vào bảng KhachHang
INSERT INTO KhachHang (HoTen, DiaChi, DienThoai)
VALUES 
    ('Nguyen Thi C', '789 QWE Street, City', '654321987'),
    ('Tran Van D', '987 ZXC Street, City', '321654987');

-- Thêm thú cưng vào bảng ThuCung
INSERT INTO ThuCung (TenThuCung, Loai, Giong, Tuoi, SoLuong, DonGia)
VALUES 
    ('Bobby', 'Chó', 'Labrador', 2, 3, 100.00), 
    ('Mimi', 'Mèo', 'Siamese', 1, 2, 50.00);   

-- Thêm đơn hàng vào bảng DonHang
INSERT INTO DonHang (MaKhachHang, NgayDatHang, TongTien)
VALUES 
    (1, '2024-06-20', 150.50),
    (2, '2024-06-21', 200.25);

-- Thêm một giao dịch thanh toán mới
INSERT INTO ThanhToan (MaDonHang, MaThuCung, NgayThanhToan, SoTien, SoLuong, DonGia)
VALUES (1, 1, '2024-06-23', 500.00, 2, 100.00); -- Thanh toán 500.00 cho 2 con thú cưng với đơn giá là 100.00

-- Thêm thông tin hóa đơn vào bảng HoaDon
INSERT INTO HoaDon (MaDonHang, NgayPhatHanh, NgayThanhToan, TongTien)
VALUES 
    (1, '2024-06-21', '2024-06-21', 150.50),
    (2, '2024-06-22', '2024-06-22', 200.25);

-- Thêm chi tiết đơn hàng vào bảng ChiTietDonHang
INSERT INTO ChiTietDonHang (MaDonHang, MaThuCung, SoLuongDonHang, DonGia)
VALUES 
    (1, 1, 1, 50.00),
    (1, 2, 2, 100.50),
    (2, 2, 1, 200.25);

-- Thêm thông tin thống kê vào bảng ThongKe
INSERT INTO ThongKe (NgayThongKe, TongSoDonHang, TongDoanhThu)
VALUES 
    ('2024-06-22', 2, 350.75);

-- Sửa thông tin trong bảng User (ví dụ: cập nhật thông tin email của user có UserID = 1)
UPDATE [User]
SET Email = 'new_email@example.com'
WHERE UserID = 1;

-- Sửa thông tin trong bảng NhanVien (ví dụ: cập nhật UserID của nhân viên có MaNhanVien = 1)
UPDATE NhanVien
SET UserID = (SELECT UserID FROM [User] WHERE Username = 'new_employee')
WHERE MaNhanVien = 1;

-- Sửa thông tin trong bảng QuanLy (ví dụ: cập nhật UserID của quản lý có MaQuanLy = 1)
UPDATE QuanLy
SET UserID = (SELECT UserID FROM [User] WHERE Username = 'new_manager')
WHERE MaQuanLy = 1;

-- Sửa thông tin trong bảng KhachHang (ví dụ: cập nhật địa chỉ của khách hàng có MaKhachHang = 1)
UPDATE KhachHang
SET DiaChi = '789 New Address, City'
WHERE MaKhachHang = 1;

-- Sửa thông tin trong bảng ThuCung (ví dụ: cập nhật số lượng thú cưng của thú cưng có MaThuCung = 1)
UPDATE ThuCung
SET SoLuong = 1  -- Số lượng thú cưng tương ứng với dữ liệu của bạn
WHERE MaThuCung = 1;

-- Sửa thông tin trong bảng DonHang (ví dụ: cập nhật ngày đặt hàng của đơn hàng có MaDonHang = 1)
UPDATE DonHang
SET NgayDatHang = '2024-06-25'
WHERE MaDonHang = 1;

-- Sửa thông tin trong bảng ThanhToan (cập nhật đơn giá từ bảng ThuCung)
UPDATE ThanhToan
SET DonGia = ThuCung.DonGia
FROM ThanhToan
JOIN ThuCung ON ThanhToan.MaThuCung = ThuCung.MaThuCung;

-- Sửa thông tin trong bảng HoaDon (ví dụ: cập nhật tổng tiền của hóa đơn có MaHoaDon = 1)
UPDATE HoaDon
SET TongTien = 250.00
WHERE MaHoaDon = 1;

-- Sửa thông tin trong bảng ChiTietDonHang (ví dụ: cập nhật số lượng và đơn giá của chi tiết đơn hàng có MaChiTietDonHang = 1)
UPDATE ChiTietDonHang
SET SoLuongDonHang = 3, DonGia = 70.00
WHERE MaChiTietDonHang = 1;

-- Sửa thông tin trong bảng ThongKe (ví dụ: cập nhật tổng số đơn hàng của thống kê có MaThongKe = 1)
UPDATE ThongKe
SET TongSoDonHang = 3
WHERE MaThongKe = 1;

-- Xóa user có UserID = 1
DELETE FROM [User]
WHERE UserID = 1;

-- Xóa nhân viên có MaNhanVien = 1
DELETE FROM NhanVien
WHERE MaNhanVien = 1;

-- Xóa quản lý có MaQuanLy = 1
DELETE FROM QuanLy
WHERE MaQuanLy = 1;

-- Xóa khách hàng có MaKhachHang = 1
DELETE FROM KhachHang
WHERE MaKhachHang = 1;

-- Xóa thú cưng có MaThuCung = 1
DELETE FROM ThuCung
WHERE MaThuCung = 1;

-- Xóa đơn hàng có MaDonHang = 1
DELETE FROM DonHang
WHERE MaDonHang = 1;

-- Xóa thanh toán có MaThanhToan = 1
DELETE FROM ThanhToan
WHERE MaThanhToan = 1;

-- Xóa hóa đơn có MaHoaDon = 1
DELETE FROM HoaDon
WHERE MaHoaDon = 1;

-- Xóa chi tiết đơn hàng có MaChiTietDonHang = 1
DELETE FROM ChiTietDonHang
WHERE MaChiTietDonHang = 1;

-- Xóa thông kê có MaThongKe = 1
DELETE FROM ThongKe
WHERE MaThongKe = 1;

-- Truy vấn thông tin từ bảng User
SELECT *
FROM [User];

-- Truy vấn thông tin từ bảng NhanVien
SELECT *
FROM NhanVien;

-- Truy vấn thông tin từ bảng QuanLy
SELECT *
FROM QuanLy;

-- Truy vấn thông tin từ bảng KhachHang
SELECT *
FROM KhachHang;

-- Truy vấn thông tin từ bảng ThuCung
SELECT *
FROM ThuCung;

-- Truy vấn thông tin từ bảng DonHang
SELECT *
FROM DonHang;

-- Truy vấn thông tin từ bảng ThanhToan
SELECT *
FROM ThanhToan;

-- Truy vấn thông tin từ bảng HoaDon
SELECT *
FROM HoaDon;

-- Truy vấn thông tin từ bảng ChiTietDonHang
SELECT *
FROM ChiTietDonHang;

-- Truy vấn thông tin từ bảng ThongKe
SELECT *
FROM ThongKe;
-- Tính tổng thanh toán cho đơn hàng có MaDonHang = 1
