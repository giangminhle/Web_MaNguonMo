# Hướng Dẫn Sử Dụng Website Quản Lý Sân Bóng 333

## Tổng Quan

Website **QuanLySan333** là hệ thống quản lý và đặt sân bóng trực tuyến, cho phép người dùng:
- Tìm kiếm và xem thông tin các địa điểm sân bóng
- Đặt sân trực tuyến
- Tìm đối thi đấu
- Quản lý kho hàng của từng địa điểm
- Đánh giá và nhận xét về sân bóng

## I. Đăng Nhập & Đăng Ký

### 1. Đăng Ký Tài Khoản
- **Truy cập**: `http://127.0.0.1:8000/dang-ky/`
- **Thông tin cần cung cấp**:
  - Tên đăng nhập
  - Email
  - Mật khẩu
  - Xác nhận mật khẩu
- **Lưu ý**: Sau khi đăng ký, cần kiểm tra email để kích hoạt tài khoản

### 2. Đăng Nhập
- **Truy cập**: `http://127.0.0.1:8000/dang-nhap/`
- **Nhập**: Tên đăng nhập và mật khẩu
- **Quên mật khẩu**: Sử dụng link "Quên mật khẩu" để đặt lại qua email

### 3. Các Loại Tài Khoản
- **Superuser**: Quản trị viên toàn hệ thống
- **Staff**: Nhân viên quản lý
- **User thường**: Người dùng thông thường

## II. Chức Năng Chính

### 1. Trang Chủ
- **URL**: `http://127.0.0.1:8000/`
- **Tính năng**:
  - Hiển thị danh sách các địa điểm sân bóng (phân trang 4_item/trang)
  - Tìm kiếm sân theo tên hoặc địa chỉ
  - Hiển thị 5 thông báo mới nhất
  - Xem đánh giá trung bình của từng địa điểm

### 2. Chi Tiết Địa Điểm Sân Bóng
- **URL**: `http://127.0.0.1:8000/dia-diem/<id>/`
- **Thông tin hiển thị**:
  - Tên, địa chỉ, mô tả địa điểm
  - Hình ảnh đại diện và thư viện ảnh
  - Danh sách các sân con thuộc địa điểm
  - Giá thuê và loại sân (5 người, 7 người, 11 người)
  - Đánh giá từ người dùng
  - Tọa độ (vĩ độ, kinh độ)

### 3. Đặt Sân Bóng
- **URL**: `http://127.0.0.1:8000/dat-san/<id>/`
- **Các bước đặt sân**:
  1. Chọn sân con muốn đặt
  2. Chọn ngày đặt
  3. Chọn khung giờ (sáng, chiều, tối)
  4. Nhập số điện thoại liên hệ
  5. Gửi yêu cầu đặt sân
- **Trạng thái đặt sân**:
  - Chờ duyệt
  - Đã duyệt
  - Từ chối

### 4. Lịch Sử Đặt Sân
- **URL**: `http://127.0.0.1:8000/lich-su-dat/`
- **Tính năng**:
  - Xem các lần đặt sân đã thực hiện
  - Hủy đặt sân (nếu chưa được duyệt)
  - Sửa thông tin đặt sân

### 5. Tìm Đối Thi Đấu
- **URL**: `http://127.0.0.1:8000/tim-doi/`
- **Tính năng**:
  - Đăng tin tìm đội đối đầu
  - Xem các tin tìm đội khác
  - Nhận kèo tham gia thi đấu
  - Quản lý các kèo đã đăng

### 6. Quản Lý Hồ Sơ Cá Nhân
- **URL**: `http://127.0.0.1:8000/ho-so/`
- **Các chức năng**:
  - Xem thông tin cá nhân
  - Cập nhật hồ sơ
  - Đổi mật khẩu
  - Xem lịch sử hoạt động

## III. Chức Năng Quản Trị (Superuser/Staff)

### 1. Quản Lý Địa Điểm
- **Thêm địa điểm mới**: `http://127.0.0.1:8000/them-dia-diem/`
- **Sửa địa điểm**: `http://127.0.0.1:8000/sua-dia-diem/<id>/`
- **Xóa địa điểm**: `http://127.0.0.1:8000/xoa-dia-diem/<id>/`

### 2. Quản Lý Sân Con
- **Thêm sân con**: `http://127.0.0.1:8000/them-san-con/`
- **Sửa thông tin sân**: `http://127.0.0.1:8000/sua-san/<id>/`

### 3. Quản Lý Đơn Đặt Sân
- **URL**: `http://127.0.0.1:8000/quan-ly-don/`
- **Tính năng**:
  - Xem tất cả các đơn đặt sân
  - Duyệt/Từ chối đơn
  - Sửa thông tin đơn

### 4. Quản Lý Thành Viên
- **URL**: `http://127.0.0.1:8000/quan-ly-thanh-vien/`
- **Tính năng**:
  - Xem danh sách thành viên
  - Sửa thông tin thành viên
  - Xóa thành viên

### 5. Quản Lý Kho Hàng
- **URL**: `http://127.0.0.1:8000/ds-san-pham/`
- **Tính năng**:
  - Xem danh sách sản phẩm
  - Thêm/Sửa/Xóa sản phẩm
  - Nhập/Xuất Excel
  - Quản lý tồn kho

### 6. Quản Lý Thông Báo
- **URL**: `http://127.0.0.1:8000/quan-ly-thong-bao/`
- **Tính năng**:
  - Đăng thông báo mới
  - Ghim thông báo quan trọng
  - Sửa/Xóa thông báo

### 7. Quản Lý Giới Thiệu
- **URL**: `http://127.0.0.1:8000/gioi-thieu/`
- **URL quản lý**: `http://127.0.0.1:8000/sua-gioi-thieu/`

## IV. Bản Đồ Sân Bóng
- **URL**: `http://127.0.0.1:8000/ban-do/`
- **Tính năng**:
  - Hiển thị tất cả địa điểm sân bóng trên bản đồ
  - Tìm kiếm theo vị trí
  - Xem thông tin chi tiết khi click vào địa điểm

## V. REST API (Dành cho nhà phát triển)

### 1. Truy Cập API Documentation
- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`

### 2. Xác Thực JWT
- **Endpoint**: `POST /api/token/`
- **Body**: 
  ```json
  {
    "username": "ten_dang_nhap",
    "password": "mat_khau"
  }
  ```
- **Response**: 
  ```json
  {
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token"
  }
  ```

### 3. Các Endpoint Chính
- **Users**: `/api/users/` - Quản lý người dùng
- **Địa điểm**: `/api/dia-diem/` - Quản lý địa điểm sân bóng
- **Sân bóng**: `/api/san-bong/` - Quản lý sân con

### 4. Sử Dụng Token
Khi gọi các API cần xác thực, thêm header:
```
Authorization: Bearer <access_token>
```

## VI. Lưu Ý Quan Trọng

### 1. Bảo Mật
- Không chia sẻ tài khoản cho người khác
- Sử dụng mật khẩu mạnh
- Đăng xuất sau khi sử dụng xong

### 2. Quy Tắc Đặt Sân
- Đặt sân trước ít nhất 2 giờ
- Hủy đặt sân trước 1 giờ so với thời gian bắt đầu
- Tuân thủ quy định của từng địa điểm

### 3. Đánh Giá
- Đánh giá trung thực về chất lượng sân
- Không spam hoặc bình luận không phù hợp

### 4. Hỗ Trợ
- Liên hệ admin qua email hoặc thông báo trên hệ thống
- Báo lỗi ngay khi phát hiện

## VII. Mobile & Responsive

Website được thiết kế responsive, tương thích với:
- Desktop (1920x1080 và cao hơn)
- Tablet (768px - 1024px)
- Mobile (360px - 768px)

## VIII. Cấu Hình Hệ Thống

### Yêu Cầu Tối Thiểu
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+
- **Internet**: Kết nối ổn định
- **JavaScript**: Bật JavaScript để sử dụng đầy đủ tính năng

### Tối Ưu Hiệu Suất
- Cache hình ảnh trong 30 ngày
- Compress CSS/JS
- Lazy load cho hình ảnh lớn

---

**Phát triển bởi**: QuanLySan333 Team  
**Công nghệ**: Django + Django REST Framework + PostgreSQL  
**Liên hệ**: admin@quanlysan333.com  

*Last updated: 2026*
