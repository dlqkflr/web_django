from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), #@app.route의 해당하는 부분
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('introduce/<str:name>/<int:age>', views.introduce),
    path('multiple/<int:num1>/<int:num2>', views.multiple),
    path('dtl/', views.dtl),
    path('birth/', views.birth),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto_throw/', views.lotto_throw),
    path('lotto_catch/', views.lotto_catch),
    path('article_new/', views.article_new),
    path('article_create/', views.article_create),
    path('static_example/', views.static_example),
    ]
