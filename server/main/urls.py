from django.urls import path
from .views import (
    JobListCreateView,
    JobRetrieveUpdateDestroyView,
    ApplicationListCreateView,
    ApplicationRetrieveUpdateDestroyView,
    UserRegistrationView,
)

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="job-list-create"),
    path("jobs/<int:pk>/", JobRetrieveUpdateDestroyView.as_view(), name="job-detail"),
    path(
        "applications/",
        ApplicationListCreateView.as_view(),
        name="application-list-create",
    ),
    path(
        "applications/<int:pk>/",
        ApplicationRetrieveUpdateDestroyView.as_view(),
        name="application-detail",
    ),
    path("register/", UserRegistrationView.as_view(), name="user-register"),
]
