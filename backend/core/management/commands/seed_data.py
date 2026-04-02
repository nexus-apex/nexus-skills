from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Assessment, AssessCandidate, AssessQuestion
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusSkills with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusskills.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Assessment.objects.count() == 0:
            for i in range(10):
                Assessment.objects.create(
                    title=f"Sample Assessment {i+1}",
                    category=random.choice(["technical", "aptitude", "personality", "language", "domain"]),
                    duration_mins=random.randint(1, 100),
                    questions_count=random.randint(1, 100),
                    status=random.choice(["draft", "published", "archived"]),
                    attempts=random.randint(1, 100),
                    pass_score=random.randint(1, 100),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Assessment records created'))

        if AssessCandidate.objects.count() == 0:
            for i in range(10):
                AssessCandidate.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    assessment_title=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    score=random.randint(1, 100),
                    status=random.choice(["invited", "started", "completed", "expired"]),
                    started_at=date.today() - timedelta(days=random.randint(0, 90)),
                    completed_at=date.today() - timedelta(days=random.randint(0, 90)),
                    percentile=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 AssessCandidate records created'))

        if AssessQuestion.objects.count() == 0:
            for i in range(10):
                AssessQuestion.objects.create(
                    assessment_title=f"Sample AssessQuestion {i+1}",
                    question=f"Sample question for record {i+1}",
                    question_type=random.choice(["mcq", "true_false", "coding", "short_answer"]),
                    difficulty=random.choice(["easy", "medium", "hard"]),
                    points=random.randint(1, 100),
                    position=random.randint(1, 100),
                    correct_answer=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 AssessQuestion records created'))
