from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import UserListView, GroupListView, MembershipListView, UserdetailListView

router = routers.DefaultRouter()
router.register('users',UserListView)
router.register('userdetails',UserdetailListView)
router.register('groups',GroupListView)
router.register('memberships',MembershipListView)

urlpatterns= [
    path('',include(router.urls)),
]