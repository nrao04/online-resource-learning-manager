from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Course

# CRUD views

# READ: list all courses
class CourseListView(listView):
    model = Course
    # template to display courses
    template_name = 'courses/course_list.html'

# READ: displaying details of single course
class CourseDetailView(detailView):
    # diplays one course
    model = Course
    template_name = 'courses/course_detail.html'

# CREATE: create a new course entry
class CourseCreateView(createView):
    model = Course
    # fields to include in the form
    fields = ['title', 'description', 'category', 'publication_date']
    # template cor course details
    template_name = 'courses/course_form.html'
    # redirect to course list upon successful creation
    success_url = reverse_lazy('course_list')
    
# UPDATE: update an existing course entry
class CourseUpdateView(updateView):
    model = Course
    fields = ['title', 'description', 'category', 'publication_date']
    # reuse same form template
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

# DELETE: delete an existing course entry    
class CourseDeleteView(deleteView):
    model = Course
    # template to confirm deletion
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')