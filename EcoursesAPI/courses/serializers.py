from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url

        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class CourseSerializer(ImageSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'image', 'created_date', 'active']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class LessonSerializer(ImageSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'created_date', 'course']


class LessonDetailSerializer(LessonSerializer):
    tags = TagsSerializer(many=True)
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['course'] = instance.course.name
    #     return rep

    # course = serializers.StringRelatedField()

    course = serializers.CharField(source='course.name')
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()

        User = user(**data)
        User.set_password(data["password"])
        User.save()

        return User

    class Meta:
        model = user
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }