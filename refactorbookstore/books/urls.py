from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from books import views

# 使用默认根路由
router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
