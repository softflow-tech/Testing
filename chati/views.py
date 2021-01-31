from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from .serializer import UserSerializer, GroupSerializer, MembershipSerializer, UserdetailSerializer
from .models import Group, Membership,Userdetail

# class UserListView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserdetailListView(ModelViewSet):
    queryset = Userdetail.objects.all()
    serializer_class = UserdetailSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes =[IsAuthenticated, ]

class GroupListView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes =[IsAuthenticated, ]

class MembershipListView(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes =[IsAuthenticated, ]

# class UserDetailsView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes =[IsAuthenticated, ]

# class GroupDetailsView(ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes =[IsAuthenticated, ]

# class MembershipDetailsView(ModelViewSet):
#     queryset = Membership.objects.all()
#     serializer_class = MembershipSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes =[IsAuthenticated, ]
