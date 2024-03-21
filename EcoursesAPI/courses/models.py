from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
class user(AbstractUser):
    avatar = CloudinaryField(null=True)


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(BaseModel):
    name = models.CharField(max_length=50)
    description = RichTextField(null=True)
    image = CloudinaryField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    subject = models.CharField(max_length=50)
    content = RichTextField(null=True)
    image = CloudinaryField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.subject

class Interaction(BaseModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(BaseModel):
    pass