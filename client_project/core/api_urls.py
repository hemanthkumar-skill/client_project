from django.urls import path
from .views import (
    ClientListCreateView,
    ClientRetrieveUpdateDeleteView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDeleteView,
    ProjectListForLoggedInUserView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),             # List/Create clients
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-detail'),  # Retrieve/Update/Delete a client by ID

    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),           # List/Create projects
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteView.as_view(), name='project-detail'), # Retrieve/Update/Delete a project by ID

    path('user-projects/', ProjectListForLoggedInUserView.as_view(), name='user-projects'),    # List projects for the logged-in user
]
