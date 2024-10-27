# users/management/commands/add_skills.py

from django.core.management.base import BaseCommand
from api.models import Skill

class Command(BaseCommand):
    help = 'Add a list of skills to the database'

    def handle(self, *args, **kwargs):
        skills_list = [
            'Python',
            'Java',
            'JavaScript',
            'C++',
            'Django',
            'Flask',
            'React',
            'Node.js',
            'HTML',
            'CSS',
            'SQL',
            'Machine Learning',
            'Data Analysis',
            'Project Management',
            'Teamwork',
            'Communication',
            # Add more skills as needed
        ]

        # Initialize a counter for added skills
        added_skills_count = 0

        for skill_name in skills_list:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            if created:  # Check if a new skill was created
                added_skills_count += 1
                self.stdout.write(self.style.SUCCESS(f'Skill "{skill_name}" added.'))
            else:
                self.stdout.write(self.style.WARNING(f'Skill "{skill_name}" already exists.'))

        # Output the total number of added skills
        self.stdout.write(self.style.SUCCESS(f'Total skills added: {added_skills_count}'))
