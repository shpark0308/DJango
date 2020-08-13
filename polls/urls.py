from django.urls import path
from . import views
# 최상위 URLconf에서 polls.urls 모듈을 연결하기

urlpatterns = [
    path('',views.index,name='index'), # View 내부로 이동하기
]