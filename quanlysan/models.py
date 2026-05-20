from django.db import models
from django.contrib.auth.models import User

class DanhMucSan(models.Model):
    ten_danh_muc = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True, null=True)
    def __str__(self): return self.ten_danh_muc

class DiaDiem(models.Model):
    ten_dia_diem = models.CharField(max_length=255)
    dia_chi = models.CharField(max_length=255)
    vi_do = models.FloatField(null=True, blank=True)
    kinh_do = models.FloatField(null=True, blank=True)
    hinh_anh_dai_dien = models.ImageField(upload_to='dia_diem/', null=True, blank=True)
    mo_ta = models.TextField(blank=True, null=True)

    @property
    def trung_binh_sao(self):
        reviews = self.ds_danh_gia.all()
        if reviews.exists():
            tb = sum(r.so_sao for r in reviews) / reviews.count()
            return round(tb, 1)
        return 5.0

    def __str__(self): return self.ten_dia_diem

class HinhAnhDiaDiem(models.Model):
    dia_diem = models.ForeignKey(DiaDiem, related_name='ds_hinh_anh', on_delete=models.CASCADE)
    hinh_anh = models.ImageField(upload_to='dia_diem_gallery/')
    ngay_tao = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Ảnh của {self.dia_diem.ten_dia_diem}"

class SanBong(models.Model):
    LOAI_SAN_CHOICES = ((5, 'Sân 5 người'), (7, 'Sân 7 người'), (11, 'Sân 11 người'))
    dia_diem = models.ForeignKey(DiaDiem, on_delete=models.CASCADE, related_name='ds_san_con')
    danh_muc = models.ForeignKey(DanhMucSan, on_delete=models.SET_NULL, null=True, blank=True)
    ten_san = models.CharField(max_length=50)
    loai_san = models.IntegerField(choices=LOAI_SAN_CHOICES, default=5)
    gia_tien = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self): return f"{self.dia_diem.ten_dia_diem} - {self.ten_san}"

class SanPham(models.Model):
    dia_diem = models.ForeignKey(DiaDiem, on_delete=models.CASCADE, related_name='kho_hang')
    ten_sp = models.CharField(max_length=100)
    gia = models.DecimalField(max_digits=10, decimal_places=0)
    so_luong = models.IntegerField(default=0)
    hinh_anh = models.ImageField(upload_to='san_pham/', null=True, blank=True)

class DatSan(models.Model):
    TRANG_THAI = (('CHO_DUYET', 'Chờ duyệt'), ('DA_DUYET', 'Đã duyệt'), ('TU_CHOI', 'Từ chối'))
    san = models.ForeignKey(SanBong, on_delete=models.CASCADE)
    khach_hang = models.ForeignKey(User, on_delete=models.CASCADE)
    ho_ten = models.CharField(max_length=100)
    sdt = models.CharField(max_length=15)
    ngay_dat = models.DateField()
    gio_bat_dau = models.TimeField()
    thoi_luong = models.IntegerField()
    tong_tien = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    tien_coc = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI, default='CHO_DUYET')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ghi_chu = models.TextField(blank=True, null=True, verbose_name="Ghi chú")
    def __str__(self): return f"{self.ho_ten} - {self.san.ten_san}"

class ChiTietDichVu(models.Model):
    don_dat = models.ForeignKey(DatSan, on_delete=models.CASCADE, related_name='chi_tiet_dv')
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField()

class TimDoi(models.Model):
    TRANG_THAI = (('DANG_TIM', 'Đang tìm đối'), ('DA_CAP', 'Đã cáp kèo'))
    nguoi_dang = models.ForeignKey(User, on_delete=models.CASCADE, related_name='keo_tao')
    doi_thu = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='keo_nhan')
    san_bong = models.ForeignKey(SanBong, on_delete=models.CASCADE)
    ngay_da = models.DateField(null=True, blank=True)
    gio_bat_dau = models.TimeField(null=True, blank=True)
    thoi_luong = models.IntegerField(default=60)
    trinh_do = models.CharField(max_length=50, choices=(('YEU', 'Yếu'), ('TB', 'Trung bình'), ('KHA', 'Khá/Mạnh')))
    sdt_lien_he = models.CharField(max_length=15)
    ghi_chu = models.TextField(blank=True, null=True)
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI, default='DANG_TIM')
    ngay_dang = models.DateTimeField(auto_now_add=True)

class ThongBao(models.Model):
    tieu_de = models.CharField(max_length=255)
    noi_dung = models.TextField()
    ngay_dang = models.DateTimeField(auto_now_add=True)
    is_pin = models.BooleanField(default=False)

class DanhGia(models.Model):
    dia_diem = models.ForeignKey(DiaDiem, on_delete=models.CASCADE, related_name='ds_danh_gia')
    khach_hang = models.ForeignKey(User, on_delete=models.CASCADE)
    so_sao = models.IntegerField(default=5)
    binh_luan = models.TextField()
    ngay_tao = models.DateTimeField(auto_now_add=True)

class ThongTinGioiThieu(models.Model):
    tieu_de_hero = models.CharField(max_length=255, default="Về Chúng Tôi", verbose_name="Tiêu đề chính")
    mo_ta_hero = models.TextField(default="Nền tảng đặt sân bóng đá tiện lợi...", verbose_name="Mô tả ngắn (Hero)")
    hinh_anh_hero = models.ImageField(upload_to='gioi_thieu/', null=True, blank=True, verbose_name="Ảnh bìa trang (Hero Background)")
    
    tam_nhin_su_menh = models.TextField(verbose_name="Tầm nhìn & Sứ mệnh", blank=True, null=True)
    noi_dung_chinh = models.TextField(verbose_name="Nội dung chi tiết", blank=True, null=True)
    hinh_anh_chinh = models.ImageField(upload_to='gioi_thieu/', null=True, blank=True, verbose_name="Ảnh minh họa nội dung")
    
    feature_1_title = models.CharField(max_length=100, default="Nhanh chóng")
    feature_1_desc = models.CharField(max_length=255, default="Đặt sân 24/7 chỉ với 30 giây.")
    feature_2_title = models.CharField(max_length=100, default="Cáp kèo dễ dàng")
    feature_2_desc = models.CharField(max_length=255, default="Hệ thống tìm đối thủ thông minh.")
    feature_3_title = models.CharField(max_length=100, default="Uy tín 100%")
    feature_3_desc = models.CharField(max_length=255, default="Cam kết giữ sân, không lo bị hủy.")
    feature_4_title = models.CharField(max_length=100, default="Hỗ trợ tận tình")
    feature_4_desc = models.CharField(max_length=255, default="Chăm sóc khách hàng liên tục.")

    def __str__(self): return "Cấu hình trang Giới thiệu"