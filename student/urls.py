from .views import ReviewView,CourseEnrolView,AllReviewView,FavoriteCourseView,MyStudentsViews,PaymentMethodIntegration,Payment_Success,Payment_fail,Payment_cancel
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
    path('payment_method/<userId>/<courseId>/',PaymentMethodIntegration),
    path('payment_success/<userId>/<courseId>/<transaction_id>/',Payment_Success),
    path('payment_fail/<courseId>/',Payment_fail),
    path('payment_cancel/<courseId>/',Payment_cancel)
]
