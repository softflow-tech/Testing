from rest_framework import serializers
from .models import Group, Membership, UserDetails, User
from rest_framework.authtoken.models import Token

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name' ,'members')
        model = Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password','email','first_name','last_name']
        extra_kwargs={'password':{'write_only':True, 'required':True}}
    
    def create(self,validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user', 'birth_date', 'friends')
        model = UserDetails

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'group', 'group_member')
        model = Membership
