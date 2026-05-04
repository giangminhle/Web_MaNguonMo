# Danh sách Endpoint (Web + REST API)

> Nguồn: `CoreRoot/urls.py` và `quanlysan/urls.py`.

## 1) Web endpoints (Django templates)

- `GET /` — Trang chủ
- `GET /dia-diem/<pk>/` — Chi tiết địa điểm
- `POST /dia-diem/<pk>/` — (Admin) cập nhật địa điểm + upload ảnh
- `GET /xoa-anh/<pk>/` — (Superuser) xóa ảnh cụm sân
- `GET /thong-tin-cum-san/<pk>/` — Thông tin cụm sân
- `GET /ban-do/` — Bản đồ
- `GET /tim-doi/` — Trang tìm đối
- `POST /tim-doi/` — Tạo kèo tìm đối
- `GET /nhan-keo/<pk>/` — Nhận kèo (đi tới đặt sân)

### Đặt sân

- `GET /dat-san/<pk>/` — Form đặt sân
- `POST /dat-san/<pk>/` — Tạo đơn đặt sân + dịch vụ kèm theo
- `GET /lich-su/` — Lịch sử đặt sân (user)

### Auth (web)

- `GET /login/` — Đăng nhập
- `POST /login/` — Xử lý đăng nhập
- `GET /signup/` — Đăng ký
- `POST /signup/` — Xử lý đăng ký (gửi email kích hoạt)
- `GET /kich-hoat/<uidb64>/<token>/` — Kích hoạt tài khoản qua email
- `GET /logout/` — Đăng xuất
- `GET /ho-so/` — Hồ sơ cá nhân
- `GET /ho-so/cap-nhat/` — Cập nhật hồ sơ
- `POST /ho-so/cap-nhat/` — Lưu cập nhật hồ sơ
- `GET /doi-mat-khau/` — Đổi mật khẩu
- `POST /doi-mat-khau/` — Lưu đổi mật khẩu

### Quên mật khẩu (Django built-in views)

- `GET /quen-mat-khau/` — Nhập email
- `POST /quen-mat-khau/` — Gửi email reset
- `GET /quen-mat-khau/xac-nhan/` — Thông báo đã gửi email
- `GET /dat-lai-mat-khau/<uidb64>/<token>/` — Form đặt lại mật khẩu
- `POST /dat-lai-mat-khau/<uidb64>/<token>/` — Lưu mật khẩu mới
- `GET /dat-lai-mat-khau/thanh-cong/` — Hoàn tất

### Quản lý đơn đặt (staff)

- `GET /quan-ly-don/`
- `GET /sua-don/<pk>/`
- `POST /sua-don/<pk>/`
- `GET /duyet-don/<pk>/<trang_thai>/` — Duyệt/Từ chối

### Kho/Sản phẩm (staff)

- `GET /ds-san-pham/`
- `POST /ds-san-pham/` — Thêm sản phẩm
- `GET /sua-san-pham/<pk>/`
- `POST /sua-san-pham/<pk>/`
- `GET /xoa-san-pham/<pk>/`
- `GET /ds-san-pham/xuat-excel/`
- `POST /ds-san-pham/nhap-excel/`
- `POST /ds-san-pham/xac-nhan-excel/`

### Quản lý địa điểm/sân con (superuser)

- `GET /them-dia-diem/`
- `POST /them-dia-diem/`
- `GET /sua-dia-diem/<pk>/`
- `POST /sua-dia-diem/<pk>/`
- `GET /xoa-dia-diem/<pk>/`
- `GET /them-san-con/`
- `POST /them-san-con/`
- `GET /sua-san/<pk>/`
- `POST /sua-san/<pk>/`

### Thông báo + Thành viên (superuser)

- `GET /quan-ly-thong-bao/`
- `POST /quan-ly-thong-bao/`
- `GET /xoa-thong-bao/<pk>/`
- `GET /quan-ly-thanh-vien/`
- `GET /sua-thanh-vien/<pk>/`
- `POST /sua-thanh-vien/<pk>/`
- `GET /xoa-thanh-vien/<pk>/`

### Trang giới thiệu

- `GET /gioi-thieu/`
- `GET /gioi-thieu/sua/` (staff)
- `POST /gioi-thieu/sua/` (staff)

## 2) REST API endpoints (DRF)

> Router đặt ở: `path("api/", include(router.urls))`

- `GET /api/users/` — list users (JWT)
- `POST /api/users/` — create user (JWT)
- `GET /api/users/<id>/` — retrieve (JWT)
- `PUT/PATCH /api/users/<id>/` — update (JWT)
- `DELETE /api/users/<id>/` — delete (JWT)

- `GET /api/dia-diem/` — CRUD địa điểm (JWT)
- `GET /api/dia-diem/<id>/` — CRUD địa điểm (JWT)

- `GET /api/san-bong/` — CRUD sân bóng (JWT)
- `GET /api/san-bong/<id>/` — CRUD sân bóng (JWT)

## 3) JWT endpoints

- `POST /api/token/` — lấy access/refresh token (SimpleJWT)

## 4) API docs

- `GET /swagger/` — Swagger UI

## 5) Admin

- `GET /admin/`

