from django import forms
from django.contrib.auth.models import User
from .models import DiaDiem, SanBong, DatSan, SanPham, ThongTinGioiThieu, ThongBao, TimDoi
from datetime import date

class DiaDiemForm(forms.ModelForm):
    class Meta:
        model = DiaDiem
        fields = '__all__'
        widgets = {
            'ten_dia_diem': forms.TextInput(attrs={'class': 'form-control'}),
            'dia_chi': forms.TextInput(attrs={'class': 'form-control'}),
            'vi_do': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtLat', 'readonly': 'readonly'}),
            'kinh_do': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtLng', 'readonly': 'readonly'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CapNhatHoSoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class SanBongForm(forms.ModelForm):
    class Meta:
        model = SanBong
        fields = '__all__'
        widgets = {
            'ten_san': forms.TextInput(attrs={'class': 'form-control'}),
            'loai_san': forms.Select(attrs={'class': 'form-control'}),
            'gia_tien': forms.NumberInput(attrs={'class': 'form-control'}),
            'dia_diem': forms.Select(attrs={'class': 'form-control'}),
        }

class DatSanForm(forms.ModelForm):
    class Meta:
        model = DatSan
        fields = ['ho_ten', 'sdt', 'ngay_dat', 'gio_bat_dau', 'thoi_luong']
        widgets = {
            'ho_ten': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'sdt': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'ngay_dat': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'gio_bat_dau': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': 'required'}),
            'thoi_luong': forms.Select(choices=[(60, '60 phút (1 tiếng)'), (90, '90 phút (1.5 tiếng)'), (120, '120 phút (2 tiếng)')], attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="Tên đăng nhập", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(forms.ModelForm):
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label="Xác nhận mật khẩu", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Tên đăng nhập',
            'email': 'Email',
            'first_name': 'Tên',
            'last_name': 'Họ',
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            self.add_error('confirm_password', "Mật khẩu xác nhận không khớp!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit: user.save()
        return user

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = '__all__'
        widgets = {
            'ten_sp': forms.TextInput(attrs={'class': 'form-control'}),
            'gia': forms.NumberInput(attrs={'class': 'form-control'}),
            'so_luong': forms.NumberInput(attrs={'class': 'form-control'}),
            'dia_diem': forms.Select(attrs={'class': 'form-control'}),
            'hinh_anh': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SuaDonForm(forms.ModelForm):
    class Meta:
        model = DatSan
        fields = ['ho_ten', 'sdt', 'ngay_dat', 'gio_bat_dau', 'thoi_luong', 'trang_thai']
        widgets = {
            'ho_ten': forms.TextInput(attrs={'class': 'form-control'}),
            'sdt': forms.TextInput(attrs={'class': 'form-control'}),
            'ngay_dat': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gio_bat_dau': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'thoi_luong': forms.NumberInput(attrs={'class': 'form-control'}),
            'trang_thai': forms.Select(attrs={'class': 'form-control'}),
        }

class SuaThanhVienForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class GioiThieuForm(forms.ModelForm):
    class Meta:
        model = ThongTinGioiThieu
        fields = '__all__'
        widgets = {
            'tieu_de_hero': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta_hero': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'hinh_anh_hero': forms.FileInput(attrs={'class': 'form-control'}),
            'tam_nhin_su_menh': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'noi_dung_chinh': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'hinh_anh_chinh': forms.FileInput(attrs={'class': 'form-control'}),
            'feature_1_title': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_1_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_2_title': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_2_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_3_title': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_3_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_4_title': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_4_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ThongBaoForm(forms.ModelForm):
    class Meta:
        model = ThongBao
        fields = ['tieu_de', 'noi_dung', 'is_pin']
        labels = {
            'tieu_de': 'Tiêu đề thông báo',
            'noi_dung': 'Nội dung chi tiết',
            'is_pin': 'Ghim lên đầu trang'
        }
        widgets = {
            'tieu_de': forms.TextInput(attrs={'class': 'form-control'}),
            'noi_dung': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_pin': forms.CheckboxInput(attrs={'class': 'form-check-input ms-2'})
        }

class SuaKeoForm(forms.ModelForm):
    class Meta:
        model = TimDoi
        fields = ['san_bong', 'ngay_da', 'gio_bat_dau', 'thoi_luong', 'trinh_do', 'sdt_lien_he', 'ghi_chu']
        labels = {
            'san_bong': 'Sân bóng', 'ngay_da': 'Ngày đá', 'gio_bat_dau': 'Giờ bắt đầu', 
            'thoi_luong': 'Thời gian đá (phút)', 'trinh_do': 'Trình độ', 
            'sdt_lien_he': 'SĐT Liên hệ', 'ghi_chu': 'Lời nhắn'
        }
        widgets = {
            'san_bong': forms.Select(attrs={'class': 'form-control'}),
            'ngay_da': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gio_bat_dau': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'thoi_luong': forms.NumberInput(attrs={'class': 'form-control'}),
            'trinh_do': forms.TextInput(attrs={'class': 'form-control'}),
            'sdt_lien_he': forms.TextInput(attrs={'class': 'form-control'}),
            'ghi_chu': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class TimDoiForm(forms.ModelForm):
    class Meta:
        model = TimDoi
        fields = ['san_bong', 'ngay_da', 'gio_bat_dau', 'thoi_luong', 'trinh_do', 'sdt_lien_he', 'ghi_chu']
        labels = {
            'san_bong': 'Chọn sân bóng',
            'ngay_da': 'Ngày đá',
            'gio_bat_dau': 'Giờ bắt đầu',
            'thoi_luong': 'Thời gian đá (phút)',
            'trinh_do': 'Trình độ đội bạn',
            'sdt_lien_he': 'Số điện thoại liên hệ',
            'ghi_chu': 'Lời nhắn nhủ'
        }
        widgets = {
            'san_bong': forms.Select(attrs={'class': 'form-select bg-light'}),
            'ngay_da': forms.DateInput(attrs={'class': 'form-control bg-light', 'type': 'date'}),
            'gio_bat_dau': forms.TimeInput(attrs={'class': 'form-control bg-light', 'type': 'time'}),
            'thoi_luong': forms.Select(choices=[(60, '60 phút'), (90, '90 phút'), (120, '120 phút')], attrs={'class': 'form-select bg-light'}),
            'trinh_do': forms.Select(choices=[
                ('Giao lưu mồ hôi', 'Giao lưu mồ hôi / Mới chơi'),
                ('Trung bình yếu', 'Trung bình yếu (Đội văn phòng)'),
                ('Trung bình', 'Trung bình (Đá thường xuyên)'),
                ('Trung bình khá', 'Trung bình khá (Có chiến thuật)'),
                ('Khá cứng', 'Khá cứng (Phủi phong trào)')
            ], attrs={'class': 'form-select bg-light'}),
            'sdt_lien_he': forms.TextInput(attrs={'class': 'form-control bg-light', 'placeholder': 'SĐT để đối thủ liên lạc...'}),
            'ghi_chu': forms.Textarea(attrs={'class': 'form-control bg-light', 'rows': 2, 'placeholder': 'Giao lưu vui vẻ, cưa đôi tiền sân...'}),
        }

class KhachSuaDonForm(forms.ModelForm):
    class Meta:
        model = DatSan
        fields = ['ho_ten', 'sdt']
        labels = {
            'ho_ten': 'Họ tên người đặt',
            'sdt': 'Số điện thoại liên hệ'
        }
        widgets = {
            'ho_ten': forms.TextInput(attrs={'class': 'form-control'}),
            'sdt': forms.TextInput(attrs={'class': 'form-control'}),
        }