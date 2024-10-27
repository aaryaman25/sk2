import csv
from django.core.management.base import BaseCommand
from api.models import Job
from datetime import datetime

class Command(BaseCommand):
    help = 'Load job data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert string date to proper date format
                    posting_date = None
                    closing_date = None
                    if row['posting_date']:
                        posting_date = datetime.strptime(row['posting_date'], '%Y-%m-%d').date()
                    if row['closing_date']:
                        closing_date = datetime.strptime(row['closing_date'], '%Y-%m-%d').date()

                    # Check if the job already exists, skip if it does
                    if not Job.objects.filter(job_id=row['job_id']).exists():
                        Job.objects.create(
                            job_id=row['job_id'],
                            business_title=row['business_title'],
                            salary_range_from=row['salary_range_from'] or None,
                            salary_range_to=row['salary_range_to'] or None,
                            work_location=row['work_location'],
                            posting_date=posting_date,
                            job_description=row['job_description'],
                            closing_date=closing_date
                        )
            self.stdout.write(self.style.SUCCESS('Successfully loaded job data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {e}'))
