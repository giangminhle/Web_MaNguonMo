# QuanLySan333 (Hệ Thống Quản Lý Sân Bóng)

![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Website quản lý & đặt sân bóng hoàn chỉnh với **Django** + **REST API** + **JWT** + **Swagger**. Hệ thống cho phép người dùng tìm kiếm, đặt sân, tìm đối thi đấu và quản lý toàn bộ hoạt động liên quan đến sân bóng.

## ✨ Tính Năng Nổi Bật

### 🏆 Dành cho người dùng
- **Tìm kiếm & khám phá** địa điểm sân bóng theo vị trí, tên, địa chỉ
- **Đặt sân trực tuyến** với hệ thống xác nhận tự động
- **Tìm đối thi đấu** - đăng kèo và nhận kèo trận đấu
- **Đánh giá & nhận xét** về chất lượng sân bóng
- **Lịch sử đặt sân** và quản lý đơn hàng
- **Bản đồ tương tác** hiển thị tất cả địa điểm

### 🛠️ Dành cho quản trị viên
- **Quản lý địa điểm** - Thêm/sửa/xóa địa điểm sân bóng
- **Quản lý sân con** - Cập nhật thông tin giá, loại sân (5/7/11 người)
- **Quản lý kho hàng** - Theo dõi sản phẩm, tồn kho, nhập/xuất Excel
- **Quản lý thành viên** - Phân quyền và quản lý người dùng
- **Quản lý thông báo** - Đăng thông báo, ghim tin quan trọng
- **Quản lý đơn đặt sân** - Duyệt/hủy/sửa các yêu cầu đặt sân

### 🚀 Công nghệ API
- **RESTful API** đầy đủ với Django REST Framework
- **Xác thực JWT** an toàn và hiệu quả
- **Swagger/OpenAPI** documentation tự động
- **CRUD operations** cho tất cả entities
- **Permission system** phân quyền chi tiết

## 🛠️ Công Nghệ Sử Dụng

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend Framework** | Django | 4.2+ |
| **REST API** | Django REST Framework | 3.14+ |
| **Authentication** | SimpleJWT | 5.2+ |
| **API Documentation** | drf-yasg (Swagger) | 1.21+ |
| **Database** | PostgreSQL | 13+ |
| **Frontend** | Django Templates + Bootstrap | - |
| **Image Processing** | Pillow | - |
| **Excel Processing** | openpyxl | - |

## 📋 Cấu Trúc Dự Án

```
QuanLySan333/
├── CoreRoot/                 # Cấu hình Django chính
│   ├── settings.py          # Cấu hình ứng dụng
│   ├── urls.py              # URL routing chính
│   └── wsgi.py              # WSGI config
├── quanlysan/               # App chính
│   ├── models.py            # Models: DiaDiem, SanBong, DatSan...
│   ├── views.py             # Views logic
│   ├── urls.py              # URL routing cho app
│   ├── forms.py             # Django forms
│   ├── serializers.py       # DRF serializers
│   └── templates/           # HTML templates
├── media/                   # Media files (images, uploads)
├── docs/                    # API documentation
└── requirements.txt         # Python dependencies
```

## 🚀 Cài Đặt & Chạy Dự Án

### 1️⃣ Kiểm Tra Python Version

**Windows:**
```powershell
py --version
# Yêu cầu: Python 3.8 trở lên
```

**Linux/WSL:**
```bash
python3 --version
# Yêu cầu: Python 3.8 trở lên
```

### 2️⃣ Clone Repository
```bash
git clone <repository-url>
cd QuanLySan333
```

### 3️⃣ Tạo Môi Trường Python

**Windows (khuyến nghị):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/WSL:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4️⃣ Cài Đặt Các Thư Viện

#### Django Core Framework
**Windows:**
```powershell
pip install Django==6.0.3
pip install asgiref==3.11.1
pip install sqlparse==0.5.5
pip install tzdata==2025.2
```

**Linux/WSL:**
```bash
pip3 install Django==6.0.3
pip3 install asgiref==3.11.1
pip3 install sqlparse==0.5.5
pip3 install tzdata==2025.2
```

#### Django REST Framework
**Windows:**
```powershell
pip install djangorestframework==3.17.1
pip install djangorestframework-simplejwt==5.5.1
pip install PyJWT==2.12.1
```

**Linux/WSL:**
```bash
pip3 install djangorestframework==3.17.1
pip3 install djangorestframework-simplejwt==5.5.1
pip3 install PyJWT==2.12.1
```

#### API Documentation
**Windows:**
```powershell
pip install drf-yasg==1.21.15
pip install uritemplate==4.2.0
pip install inflection==0.5.1
pip install PyYAML==6.0.3
```

**Linux/WSL:**
```bash
pip3 install drf-yasg==1.21.15
pip3 install uritemplate==4.2.0
pip3 install inflection==0.5.1
pip3 install PyYAML==6.0.3
```

#### Database & Media Processing
**Windows:**
```powershell
pip install psycopg2-binary==2.9.11
pip install pillow==11.3.0
pip install openpyxl==3.1.5
```

**Linux/WSL:**
```bash
pip3 install psycopg2-binary==2.9.11
pip3 install pillow==11.3.0
pip3 install openpyxl==3.1.5
```

#### Cài Đặt Nhanh (Tất Cả Cùng Lúc)
```bash
# Windows
pip install Django==6.0.3 asgiref==3.11.1 sqlparse==0.5.5 tzdata==2025.2 djangorestframework==3.17.1 djangorestframework-simplejwt==5.5.1 PyJWT==2.12.1 drf-yasg==1.21.15 uritemplate==4.2.0 inflection==0.5.1 PyYAML==6.0.3 psycopg2-binary==2.9.11 pillow==11.3.0 openpyxl==3.1.5

# Linux/WSL
pip3 install Django==6.0.3 asgiref==3.11.1 sqlparse==0.5.5 tzdata==2025.2 djangorestframework==3.17.1 djangorestframework-simplejwt==5.5.1 PyJWT==2.12.1 drf-yasg==1.21.15 uritemplate==4.2.0 inflection==0.5.1 PyYAML==6.0.3 psycopg2-binary==2.9.11 pillow==11.3.0 openpyxl==3.1.5
```

#### Hoặc Sử Dụng Requirements.txt
```bash
# Windows
pip install -r requirements.txt

# Linux/WSL
pip3 install -r requirements.txt
```

### 5️⃣ Cấu Hình PostgreSQL

Trong `CoreRoot/settings.py` dự án đang sử dụng:
- **Database**: `quanlysan_db`
- **User**: `postgres`
- **Host**: `localhost`
- **Port**: `5432`

**Tạo database:**
```sql
CREATE DATABASE quanlysan_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE quanlysan_db TO postgres;
```

### 6️⃣ Database Migration
**Windows:**
```powershell
py manage.py makemigrations
py manage.py migrate
```

**Linux/WSL:**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 7️⃣ Tạo Superuser
**Windows:**
```powershell
py manage.py createsuperuser
```

**Linux/WSL:**
```bash
python3 manage.py createsuperuser
```

### 8️⃣ Chạy Server
**Windows:**
```powershell
py manage.py runserver
```

**Linux/WSL:**
```bash
python3 manage.py runserver
```

**Truy cập ứng dụng:** `http://127.0.0.1:8000/`

## 👥 Hệ Thống Phân Quyền

| Vai trò | Quyền | Chức năng |
|---------|-------|-----------|
| **Superuser** | Toàn quyền  | Quản lý hệ thống, CRUD địa điểm/sân, quản lý thành viên, thông báo |
| **Staff** | Quyền hạn chế | Quản lý kho hàng, sản phẩm, giới thiệu (tuỳ view được cấp) |
| **User thường** | Người dùng | Đặt sân, đánh giá, tìm đối, xem thông tin |


## 🌐 URL Structure

### User Interface
- `/` - Trang chủ
- `/dia-diem/<id>/` - Chi tiết địa điểm
- `/dat-san/<id>/` - Đặt sân
- `/tim-doi/` - Tìm đối thi đấu
- `/lich-su-dat/` - Lịch sử đặt sân
- `/ban-do/` - Bản đồ địa điểm

### Authentication
- `/dang-nhap/` - Đăng nhập
- `/dang-ky/` - Đăng ký
- `/dang-xuat/` - Đăng xuất
- `/ho-so/` - Hồ sơ cá nhân
- `/cap-nhat-ho-so/` - Cập nhật hồ sơ

### Admin Panel
- `/quan-ly-don/` - Quản lý đơn đặt sân
- `/quan-ly-thanh-vien/` - Quản lý thành viên
- `/quan-ly-thong-bao/` - Quản lý thông báo
- `/ds-san-pham/` - Quản lý kho hàng

## 🎯 Models Chính

### DiaDiem (Địa điểm)
```python
class DiaDiem(models.Model):
    ten_dia_diem = models.CharField(max_length=255)
    dia_chi = models.CharField(max_length=255)
    vi_do = models.FloatField(null=True, blank=True)
    kinh_do = models.FloatField(null=True, blank=True)
    hinh_anh_dai_dien = models.ImageField(...)
    mo_ta = models.TextField(blank=True, null=True)
```

### SanBong (Sân con)
```python
class SanBong(models.Model):
    LOAI_SAN_CHOICES = ((5, 'Sân 5 người'), (7, 'Sân 7 người'), (11, 'Sân 11 người'))
    dia_diem = models.ForeignKey(DiaDiem, ...)
    ten_san = models.CharField(max_length=50)
    loai_san = models.IntegerField(choices=LOAI_SAN_CHOICES)
    gia_tien = models.DecimalField(max_digits=10, decimal_places=0)
```

### DatSan (Đặt sân)
```python
class DatSan(models.Model):
    TRANG_THAI = (('CHO_DUYET', 'Chờ duyệt'), ('DA_DUYET', 'Đã duyệt'), ('TU_CHOI', 'Từ chối'))
    nguoi_dat = models.ForeignKey(User, ...)
    san_bong = models.ForeignKey(SanBong, ...)
    ngay_dat = models.DateField()
    khoang_gio = models.CharField(max_length=50)
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI)
```

## 🎨 Features Chi Tiết

### 📍 Tìm Kiếm & Lọc
- Tìm kiếm theo tên địa điểm, địa chỉ
- Lọc theo loại sân (5/7/11 người)
- Tìm kiếm theo khoảng cách (tính toán tọa độ GPS)
- Phân trang danh sách kết quả

### 💰 Quản Lý Giá & Đặt Sân
- Giá thuê theo khung giờ (sáng, chiều, tối)
- Hệ thống xác nhận tự động
- Lịch sử đặt sân chi tiết
- Hủy/sửa đặt sân (tuỳ điều kiện)

### ⭐ Đánh Giá & Phản Hồi
- Hệ thống đánh giá 5 sao
- Bình luận chi tiết
- Tính điểm trung bình tự động
- Hình ảnh đính kèm

### 🤝 Tìm Đối Thi Đấu
- Đăng tin tìm đội đối đầu
- Lọc theo khu vực, thời gian
- Hệ thống nhận/hủy kèo
- Lịch sử các trận đấu

## 🔧 Development

### Environment Variables
Tạo file `.env` trong thư mục gốc:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=quanlysan_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### Testing
```bash
py manage.py test
```

### Collect Static Files
```bash
py manage.py collectstatic
```

## 🚀 Deployment

### Production Settings
```python
# CoreRoot/settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
STATIC_ROOT = '/var/www/html/static/'
MEDIA_ROOT = '/var/www/html/media/'
```

### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Linux Server (WSL/VPS)
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3-pip python3-venv postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

## 📊 Database Schema

### Relationships
- `DiaDiem` 1→N `SanBong`
- `DiaDiem` 1→N `DatSan` (thông qua `SanBong`)
- `User` 1→N `DatSan`
- `DiaDiem` 1→N `DanhGia`
- `DiaDiem` 1→N `SanPham`

### Indexes
- Tự động tạo indexes cho foreign keys
- Index cho trường tìm kiếm (ten_dia_diem, dia_chi)
- Index cho trường ngày tháng (ngay_dat)


## 🤝 Support

- **Email**: admin@quanlysan333.com
- **Documentation**: `/docs/`
- **API Docs**: `/swagger/`
- **Issues**: GitHub Issues

## 📈 Roadmap

- [ ] Mobile App (React Native)
- [ ] Payment Integration (Momo, VNPay)
- [ ] Real-time Notifications (WebSocket)
- [ ] Advanced Analytics Dashboard
- [ ] Multi-language Support
- [ ] Cloud Storage Integration

---

**Phát triển bởi**: CNTT1 Team  
**Last updated**: May 2026

