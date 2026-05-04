from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DiaDiem, SanBong

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

class DiaDiemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaDiem
        fields = '__all__'

class SanBongSerializer(serializers.ModelSerializer):
    ten_dia_diem = serializers.CharField(source='dia_diem.ten_dia_diem', read_only=True)
    
    class Meta:
        model = SanBong
        fields = ['id', 'ten_san', 'loai_san', 'gia_tien', 'dia_diem', 'ten_dia_diem']