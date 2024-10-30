from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

# View for listing all clients and creating a new client
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # You can modify this if 'created_by' needs to be set explicitly
        serializer.save(created_by=self.request.user)

# View for retrieving, updating, and deleting a client by ID
class ClientRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

# View for listing all projects and creating a new project
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        client_id = self.request.data.get('client_id')
        user_ids = self.request.data.get('users', [])

        # Ensure client_id and user_ids are correctly provided
        if not client_id or not isinstance(user_ids, list):
            raise ValidationError({"detail": "Client ID and user IDs must be provided."})

        client = get_object_or_404(Client, id=client_id)
        users = User.objects.filter(id__in=user_ids)
        serializer.save(created_by=self.request.user, client=client, users=users)

# View for retrieving, updating, and deleting a project by ID
class ProjectRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

# View to list projects assigned to the logged-in user
class ProjectListForLoggedInUserView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.request.user.projects.all()

# Render index.html for the root path
def index(request):
    return render(request, 'core/index.html')


