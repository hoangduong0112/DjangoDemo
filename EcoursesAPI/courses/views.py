import parser

from rest_framework import viewsets, generics, status, parsers
from rest_framework.response import Response

from .models import *
from .serializers import CategorySerializer, CourseSerializer, LessonSerializer, LessonDetailSerializer, UserSerializer
from .paginators import CoursesPaginator
from rest_framework.decorators import action


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = CoursesPaginator

    def get_queryset(self):
        qr = self.queryset
        q = self.request.query_params.get('q')
        if self.action.__eq__('list'):
            qr = qr.filter(name__icontains=q)
        cate = self.request.query_params.get('category_id')
        if cate:
            qr = qr.filter(category_id=cate)
        return qr

    @action(methods=['get'], detail=True, url_path='lessons')
    def get_lesson(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)
        q = request.query_params.get('q')

        if q:
            lessons = lessons.filter(subject__icontains=q)

        return Response(LessonSerializer(lessons, many=True).data,
                        status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related('tags').filter(active=True)
    serializer_class = LessonDetailSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = user.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]