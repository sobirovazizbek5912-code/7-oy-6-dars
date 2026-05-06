from django.contrib import admin
from .models import Category, Elon,Author,Publisher,Comment


admin.site.site_header="Bugungi kun yangliklari"
admin.site.site_title='Yangliklar'
admin.site.login_template='admin/login.html'
admin.site.logout_template='admin/logout.html'


admin.site.register(Category)
admin.site.register(Elon)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Comment)
