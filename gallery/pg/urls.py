from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name = "home"),
    path('upload',views.image_upload,name = "upload"),
    path('upload/images',views.Upload,name = "images upload"),
    path('search',views.search_by_tag,name = "search image"),
    path('view/<int:pk>',views.view_image,name = "view image")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

