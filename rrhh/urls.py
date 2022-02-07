from django.urls import path
from rrhh import views
from django.conf import settings
from django.conf.urls.static import static

#general urls
app_name = 'rrhh'
urlpatterns = [
    path('recruitment/', views.RecruitmentView.as_view(), name='recruitment'),
    path('jobDescription/', views.JobDescriptionView.as_view(), name='jobDescription'),
    path('approveRequest/', views.ApproveRequestView.as_view(), name='approveRequest'),
]
if not settings.DEBUG:    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)