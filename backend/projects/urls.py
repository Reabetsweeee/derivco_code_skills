from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, CelebrationWallView    

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('completed/', CelebrationWallView.as_view(), name='celebration_wall'),
]