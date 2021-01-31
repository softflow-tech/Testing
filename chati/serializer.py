from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Group, Membership, Userdetail
from rest_framework.authtoken.models import Token

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name' ,'members')
        model = Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs={'password':{'write_only':True, 'required':True}}
    
    def create(self,validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user

class UserdetailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_id', 'email', 'first_name','last_name')
        model = Userdetail

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'group', 'group_member')
        model = Membership
