
from django.urls import path
from video_content import views
from django.conf.urls.static import static
from django.conf import settings

app_name= 'video_content'

urlpatterns = [
    path('video_stream', views.video_stream, name='video_stream')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
