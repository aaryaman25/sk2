from django.urls import path
from .api_views import UserProfileView, SkillSearchView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('skills/search/', SkillSearchView.as_view(), name='skill-search'),
]
