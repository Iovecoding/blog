#进行users 子应用的视图路由
from django.urls import path
from users.views import RegisterView
urlpatterns = [
    #path 第一个参数：路由
    #path第二个参数：视图函数名
    #namespace 为该path设置一个别名，防止冲突
    path('register/', RegisterView.as_view(), name = 'register'),

]