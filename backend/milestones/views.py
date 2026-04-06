from rest_framework import generics, permissions
from .models import Milestone   
from .serializers import MilestoneSerializer    
from projects.models import Project

class MilestoneListCreateView(generics.ListCreateAPIView):
    """List all milestones for a project or create a new milestone"""
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Milestone.objects.filter(project_id=self.kwargs['project_id']).order_by('due_date')

    def perform_create(self, serializer):
        project = generics.get_object_or_404(Project, id=self.kwargs['project_id'])
        serializer.save(project=project)

class MilestoneUpdateView(generics.UpdateAPIView):
    """Update milestone details or status"""
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]