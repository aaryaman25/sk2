from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from .views import RegisterView, LoginView
from knox import views as knox_views
from django.urls import path, include
from .views import JobViewSet
from users.api_views import UserProfileView, SkillSearchView
from rest_framework.routers import DefaultRouter


urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('skills/search/', SkillSearchView.as_view(), name='skill-search'),
]
