from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, StudentViewSet

router = DefaultRouter()
router.register('classes', ClassViewSet, basename='class')
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls
