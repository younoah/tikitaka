from django.contrib import admin
from django.urls import path
import tika.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tika.views.home, name = 'home'),
    path('product/', tika.views.product, name = 'product'),
    path('list/', tika.views.list, name = 'list'),
    path('order/', tika.views.order, name = 'order'),
    path('order/create', tika.views.create, name = 'create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
