from django.contrib import admin
from .models import Assessment, AssessCandidate, AssessQuestion

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "duration_mins", "questions_count", "status", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["title"]

@admin.register(AssessCandidate)
class AssessCandidateAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "assessment_title", "score", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "phone"]

@admin.register(AssessQuestion)
class AssessQuestionAdmin(admin.ModelAdmin):
    list_display = ["assessment_title", "question_type", "difficulty", "points", "position", "created_at"]
    list_filter = ["question_type", "difficulty"]
    search_fields = ["assessment_title", "correct_answer"]
