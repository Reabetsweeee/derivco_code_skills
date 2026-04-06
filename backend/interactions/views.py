from rest_framework import generics, permissions
from .models import Comment, CollabRequest
from .serializers import CommentSerializer, CollabRequestSerializer
from projects.models import Project


class CommentListCreateView(generics.ListCreateAPIView):
    """Anyone can read comments. Must be logged in to post."""
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(project_id=self.kwargs['project_id'])

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_id'])
        serializer.save(author=self.request.user, project=project)


class CollabRequestCreateView(generics.CreateAPIView):
    """Logged in users can raise their hand to join a project."""
    serializer_class = CollabRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_id'])
        serializer.save(requester=self.request.user, project=project)