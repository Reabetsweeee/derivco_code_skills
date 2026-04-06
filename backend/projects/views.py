from rest_framework import generics , permissions
from .models import Project
from .serializers import ProjectSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CelebrationWallView(generics.ListAPIView):
    queryset = Project.objects.filter(status='completed')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

def get_queryset(self):
    return Project.objects.filter(status='completed')