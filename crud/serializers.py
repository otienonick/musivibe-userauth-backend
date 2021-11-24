from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for our user objects.
    
    """
    class Meta:
        model = User
        fields =['id','username','email','password','avatar',]

        # hide password
        extra_kwargs = {
            'password':{'write_only' : True}
        }
        
        # hash user's password
    def create(self, validated_data):
        password = validated_data.pop('password',None) 
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) 
        instance.save()
        return instance

# class ProfileSerializer(serializers.ModelSerializer):
#     """
#     A serializer for our user profile objects
    
#     """
#     class Meta:
#         model = Profile
#         fields =['avatar','followers','following']
