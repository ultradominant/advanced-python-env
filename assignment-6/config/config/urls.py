from django.contrib import admin
from django.urls import path
from blog.views import posts_api, post_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", post_list),
    path("api/posts/", posts_api),
]

from django.contrib import admin
from django.urls import path, include
from blog.views import post_list   # добавь

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('', post_list, name='home'),  # главная страница
]
