from rest_framework import serializers, generics, permissions
from .models import Comment,CollabRequest
from projects.models import Project 

classCommentListCreateView(generics.ListCreateAPIView):
"""anyone can read comments but MUST BE LOGGED IN TO POST"""
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

    def get_queryset(self):
        return Comment.objects.filter(project_id=self.kwargs['project_id']).order_by('-created_at') 
def perform_create(self, serializer):
        project = generics.get_object_or_404(Project, id=self.kwargs['project_id'])
        serializer.save(author=self.request.user, project=project)

class CollabRequestListCreateView(generics.ListCreateAPIView):  
     """logged in users can raise their hand to collaborate on a project, but only project owner can see the collab requests"""
     serializer_class = CollabRequestSerializer
     permission_classes = [permissions.IsAuthenticated] 

    def perform_create(self, serializer):
        project = generics.get_object_or_404(Project, id=self.kwargs['project_id'])
        serializer.save(requester=self.request.user, project=project)