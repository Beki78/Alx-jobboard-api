from rest_framework import generics, filters, permissions
from .models import Job, Application
from .serializer import JobSerializer, ApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializer import UserRegistrationSerializer


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["employmentType", "experienceLevel", "location"]
    search_fields = ["title", "description"]

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class JobRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["jobId", "userID"]
    search_fields = ["resume"]

    permission_classes = [permissions.IsAuthenticated]


class ApplicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
