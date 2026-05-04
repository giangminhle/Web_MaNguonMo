from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cấp quyền Admin (is_staff=True) cho một tài khoản bất kỳ'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Tên đăng nhập của user cần cấp quyền')

    def handle(self, *args, **options):
        username = options['username']
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'✅ Thành công! Đã cấp quyền Admin cho tài khoản: {username}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'❌ Lỗi: Không tìm thấy tài khoản nào có tên "{username}".'))