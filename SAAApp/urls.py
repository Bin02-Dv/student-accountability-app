from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('conva/', views.conva, name='conva'),
    path('fetch_conversation_data/', views.fetch_conversation_data, name='fetch_conversation_data'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('create-goal/', views.create_goal, name='create_goal'),
    path('update-goal/<int:id>', views.update_goal, name='update_goal'),
    path('track-progress/', views.track_progress, name='track_progress'),
    path('student-progress/', views.track_progress_2, name='student_progress'),
    path('delete/<int:id>', views.goal_delete, name='delete'),
]