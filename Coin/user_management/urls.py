from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('token',UserView)

urlpatterns = [
   path('',include(router.urls)),
   path('link/<int:pk>/<str:username>/', TokenView.as_view(), name = 'click_link'),

]