from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import UserListView, GroupListView, MembershipListView, UserDetailsListView

router = routers.DefaultRouter()
router.register('users',UserListView)
router.register('userdetails',UserDetailsListView)
router.register('groups',GroupListView)
router.register('memberships',MembershipListView)


urlpatterns= [
    path('',include(router.urls)),
    # path('users/',UserListView.as_view(), name= 'users'),
    # path('users/<int:pk>/',UserDetailsView.as_view(), name = 'user_details'),

    # path('groups/',GroupListView.as_view(), name= 'groups'),
    # path('groups/<int:pk>/',GroupDetailsView.as_view(), name = 'group_details'),

    # path('memberships/',MembershipListView.as_view(), name= 'memberships'),
    # path('memberships/<int:pk>/',MembershipDetailsView.as_view(), name = 'membership_details'),
]