from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from rest_framework import serializers

from pdfconverter.models import File, Fileupload

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('password', 'username', 'first_name', 'last_name', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ["url", "name"]

class FileSerializer(serializers.ModelSerializer):
  class Meta:
    model = File
    fields = ('file1', 'file2', 'remark', 'timestamp')

class FileuploadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fileupload
    fields = ['file']

