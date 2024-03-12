from django.urls import path
from www.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
