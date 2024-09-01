from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.v1 import school, classroom, teacher, student

router = DefaultRouter()
router.register('school', school.SchoolViewSet, basename = 'school')
router.register('classroom', classroom.ClassroomViewSet, basename = 'classroom')
router.register('teacher', teacher.TeacherViewSet, basename = 'teacher')
router.register('student', student.StudentViewSet, basename = 'student')

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
