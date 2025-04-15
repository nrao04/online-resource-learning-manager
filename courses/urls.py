from django.urls import path
from . import views

urlpatterns = [
    # display list of all courses
    path('', views.CourseListView.as_view(), name ='course_list'),
    
    # display detailed view of a specific course (using its primary key)
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name ='course_detail'),
    
    # form to create a new course
    path('course/new/', views.CourseCreateView.as_view(), name ='course_create'),
    
    # form to update an existing course
    path('course/<int:pk>/edit/', views.CourseUpdateView.as_view(), name ='course_update'),
    
    # confirmation page to delete a course
    path('course/<int:pk>/delete/', views.CourseDeleteView.as_view(), name ='course_delete'),
]