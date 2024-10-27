from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Job
from .serializers import JobSerializer

# Import login from Django auth
from django.contrib.auth import login

class JobFilter(filters.FilterSet):
    business_title = filters.CharFilter(field_name='business_title', lookup_expr='icontains')
    work_location = filters.CharFilter(field_name='work_location', lookup_expr='icontains')
    salary_range_from = filters.NumberFilter(field_name='salary_range_from', lookup_expr='gte')
    salary_range_to = filters.NumberFilter(field_name='salary_range_to', lookup_expr='lte')

    class Meta:
        model = Job
        fields = ['business_title', 'work_location', 'salary_range_from', 'salary_range_to']

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = JobFilter  # Add the filter class here

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(KnoxLoginView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = AuthTokenSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Use the login function from django.contrib.auth
        login(request, user)
        return super(LoginView, self).post(request, format=None)
