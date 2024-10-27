from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Skill
from .serializer import UserProfileSerializer, SkillSerializer

# API View for User Profile
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

# API View for Skill Search
class SkillSearchView(generics.ListAPIView):
    serializer_class = SkillSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return Skill.objects.filter(name__icontains=query)
        return Skill.objects.all()
