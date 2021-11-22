from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#general urls
app_name = 'shop'
urlpatterns = [    
    path('product/', views.ProductListView.as_view(), name='product'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('<slug>/', views.ProductDetailView.as_view(), name='detail'),
]
if not settings.DEBUG:    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)