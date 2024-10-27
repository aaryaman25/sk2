from rest_framework import serializers
from .models import UserProfile, Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, required=False)  # Include the skills field

    class Meta:
        model = UserProfile
        fields = ['user', 'linkedin_url', 'resume', 'skills']  # Include other fields if needed

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skills', None)  # Extract skills data if present
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.resume = validated_data.get('resume', instance.resume)
        instance.save()

        if skills_data is not None:
            # Update skills using the set method
            instance.skills.set(skills_data)

        return instance
