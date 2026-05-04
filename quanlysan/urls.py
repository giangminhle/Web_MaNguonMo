from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
schema_view = get_schema_view(
   openapi.Info(title="Sân Bóng 333 API", default_version='v1'),
   public=True, permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'dia-diem', views.DiaDiemViewSet)
router.register(r'san-bong', views.SanBongViewSet)

urlpatterns = [
    path('', views.trang_chu, name='home'),
    path('dia-diem/<int:pk>/', views.chi_tiet_dia_diem, name='chi_tiet_dia_diem'),
    path('xoa-anh/<int:pk>/', views.xoa_anh_cum_san, name='xoa_anh_cum_san'),
    path('thong-tin-cum-san/<int:pk>/', views.thong_tin_cum_san, name='thong_tin_cum_san'),
    path('ban-do/', views.ban_do_lon, name='ban_do_lon'),
    
    path('dang-nhap/', views.dang_nhap, name='login'),
    path('dang-ky/', views.dang_ky, name='signup'),
    path('dang-xuat/', views.dang_xuat, name='logout'),
    path('ho-so/', views.ho_so_ca_nhan, name='ho_so'),
    path('cap-nhat-ho-so/', views.cap_nhat_ho_so, name='cap_nhat_ho_so'),
    path('doi-mat-khau/', views.doi_mat_khau, name='doi_mat_khau'),
    
    path('quen-mat-khau/', auth_views.PasswordResetView.as_view(
        template_name='quanlysan/quen_mat_khau.html', 
        email_template_name='quanlysan/email_quen_mat_khau.html', # Giữ làm bản dự phòng text
        html_email_template_name='quanlysan/email_quen_mat_khau.html' # <--- BỔ SUNG THAM SỐ NÀY
    ), name='password_reset'),    
    path('quen-mat-khau/gui-xong/', auth_views.PasswordResetDoneView.as_view(template_name='quanlysan/thong_bao_email.html', extra_context={'title': 'Đã gửi email', 'message': 'Vui lòng kiểm tra hộp thư của bạn.'}), name='password_reset_done'),
    path('dat-lai-mat-khau/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='quanlysan/dat_lai_mat_khau.html'), name='password_reset_confirm'),
    path('dat-lai-mat-khau/hoan-tat/', auth_views.PasswordResetCompleteView.as_view(template_name='quanlysan/thong_bao_email.html', extra_context={'title': 'Thành công', 'message': 'Mật khẩu đã được đổi. Vui lòng đăng nhập lại.', 'is_success': True}), name='password_reset_complete'),
    path('kich-hoat/<uidb64>/<token>/', views.kich_hoat_tai_khoan, name='kich_hoat_tai_khoan'),
    
    path('dat-san/<int:pk>/', views.dat_san, name='dat_san'),
    path('lich-su-dat/', views.lich_su_dat, name='lich_su_dat'),
    
    path('khach-huy-don/<int:pk>/', views.khach_huy_don, name='khach_huy_don'),
    path('khach-sua-don/<int:pk>/', views.khach_sua_don, name='khach_sua_don'),

    path('tim-doi/', views.trang_tim_doi, name='trang_tim_doi'),
    path('nhan-keo/<int:pk>/', views.nhan_keo, name='nhan_keo'),
    
    path('sua-keo/<int:pk>/', views.sua_keo, name='sua_keo'),
    path('huy-keo/<int:pk>/', views.huy_keo, name='huy_keo'),

    path('ds-san-pham/', views.ds_san_pham, name='ds_san_pham'),
    path('ds-san-pham/xuat-excel/', views.xuat_excel_san_pham, name='xuat_excel_san_pham'),
    path('ds-san-pham/nhap-excel/', views.nhap_excel_san_pham, name='nhap_excel_san_pham'),
    path('ds-san-pham/xac-nhan-excel/', views.xac_nhan_excel, name='xac_nhan_excel'),
    
    path('sua-san-pham/<int:pk>/', views.sua_san_pham, name='sua_san_pham'),
    path('xoa-san-pham/<int:pk>/', views.xoa_san_pham, name='xoa_san_pham'),
    path('them-dia-diem/', views.them_dia_diem, name='them_dia_diem'),
    path('sua-dia-diem/<int:pk>/', views.sua_dia_diem, name='sua_dia_diem'),
    path('xoa-dia-diem/<int:pk>/', views.xoa_dia_diem, name='xoa_dia_diem'),
    path('them-san-con/', views.them_san_con, name='them_san_con'),
    path('sua-san/<int:pk>/', views.sua_san, name='sua_san'),
    path('quan-ly-don/', views.quan_ly_don, name='quan_ly_don'),
    path('sua-don/<int:pk>/', views.sua_don, name='sua_don'),
    path('duyet-don/<int:pk>/<str:trang_thai>/', views.duyet_don, name='duyet_don'),
    
    path('quan-ly-thanh-vien/', views.quan_ly_thanh_vien, name='quan_ly_thanh_vien'),
    path('sua-thanh-vien/<int:pk>/', views.sua_thanh_vien, name='sua_thanh_vien'),
    path('xoa-thanh-vien/<int:pk>/', views.xoa_thanh_vien, name='xoa_thanh_vien'),
    
    path('quan-ly-thong-bao/', views.quan_ly_thong_bao, name='quan_ly_thong_bao'),
    path('sua-thong-bao/<int:pk>/', views.sua_thong_bao, name='sua_thong_bao'),
    path('xoa-thong-bao/<int:pk>/', views.xoa_thong_bao, name='xoa_thong_bao'),
    
    path('gioi-thieu/', views.gioi_thieu, name='gioi_thieu'),
    path('sua-gioi-thieu/', views.sua_gioi_thieu, name='sua_gioi_thieu'),
    
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]