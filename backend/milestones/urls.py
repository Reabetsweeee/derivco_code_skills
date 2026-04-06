from django.urls import path
from .views import MilestoneListCreateView, MilestoneUpdateView 

urlpatterns = [
path ('<int:project_id>/milestones/', MilestoneListCreateView.as_view(), name='milestone'),
path('milestone/<int:pk>/', MilestoneUpdateView.as_view(), name='milestone-update'),
]