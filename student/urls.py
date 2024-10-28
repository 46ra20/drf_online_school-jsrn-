from .views import ReviewView,CourseEnrolView,AllReviewView,FavoriteCourseView,MyStudentsViews,PaymentMethodIntegration
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('review',ReviewView,basename='user_review')
# router.register('enrol',CourseEnrolView,basename='course_view')

urlpatterns = [
    # path('',include(router.urls)),
    path('review/all/',AllReviewView.as_view({'get':'list'})),
    path('review/<course_id>/',ReviewView.as_view({'get':'list'})),
    path('review_create/',ReviewView.as_view({'post':'create'})),
    path('enrol/<enrol_by>/',CourseEnrolView.as_view({'get':'list'})),
    path('enrol_create/',CourseEnrolView.as_view({'post':'create'})),
    path('enrol_unenroled/<id>/',CourseEnrolView.as_view({'delete':'destroy'})),
    path('favorite_course/',FavoriteCourseView.as_view({'get':'list'})),
    path('my_student/<userId>/',MyStudentsViews.as_view({'get':'list'})),
    path('payment_method/',PaymentMethodIntegration)
]
