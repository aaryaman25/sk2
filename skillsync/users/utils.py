# users/utils.py
from api.models import Skill

def add_skills_to_profile(profile, skills_to_add):
    for skill_name in skills_to_add:
        try:
            # Retrieve the Skill instance by name
            skill = Skill.objects.get(name=skill_name)
            print(f"Retrieved skill: {skill}")  # Confirm the skill is retrieved
            profile.skills.add(skill)  # Add the skill to the profile
            print(f"Added skill: {skill.name}")
        except Skill.DoesNotExist:
            print(f"Skill with name '{skill_name}' does not exist.")

# users/utils.py
def clear_skills_from_profile(profile):
    profile.skills.clear()  # This removes all skills associated with the profile
    print("All skills have been removed from the profile.")
