from django.db import models

class Assessment(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[("technical", "Technical"), ("aptitude", "Aptitude"), ("personality", "Personality"), ("language", "Language"), ("domain", "Domain")], default="technical")
    duration_mins = models.IntegerField(default=0)
    questions_count = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("published", "Published"), ("archived", "Archived")], default="draft")
    attempts = models.IntegerField(default=0)
    pass_score = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class AssessCandidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    assessment_title = models.CharField(max_length=255, blank=True, default="")
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("invited", "Invited"), ("started", "Started"), ("completed", "Completed"), ("expired", "Expired")], default="invited")
    started_at = models.DateField(null=True, blank=True)
    completed_at = models.DateField(null=True, blank=True)
    percentile = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class AssessQuestion(models.Model):
    assessment_title = models.CharField(max_length=255)
    question = models.TextField(blank=True, default="")
    question_type = models.CharField(max_length=50, choices=[("mcq", "MCQ"), ("true_false", "True False"), ("coding", "Coding"), ("short_answer", "Short Answer")], default="mcq")
    difficulty = models.CharField(max_length=50, choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")], default="easy")
    points = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    correct_answer = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.assessment_title
