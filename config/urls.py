from django.contrib import admin
from django.urls import path

admin.site.site_header = 'YggCore ERP'
admin.site.site_title = 'YggCore'
admin.site.index_title = 'Painel administrativo'

urlpatterns = [
    path('admin/', admin.site.urls),
]
