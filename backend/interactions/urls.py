from django.urls import path
from .views import CommentListCreateView, CollabRequestCreateView

urlpatterns = [
    path('<int:project_id>/comments/', CommentListCreateView.as_view(), name='comments'),
    path('<int:project_id>/raise-hand/', CollabRequestCreateView.as_view(), name='raise_hand'),
]