import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Assessment, AssessCandidate, AssessQuestion


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['assessment_count'] = Assessment.objects.count()
    ctx['assessment_technical'] = Assessment.objects.filter(category='technical').count()
    ctx['assessment_aptitude'] = Assessment.objects.filter(category='aptitude').count()
    ctx['assessment_personality'] = Assessment.objects.filter(category='personality').count()
    ctx['assesscandidate_count'] = AssessCandidate.objects.count()
    ctx['assesscandidate_invited'] = AssessCandidate.objects.filter(status='invited').count()
    ctx['assesscandidate_started'] = AssessCandidate.objects.filter(status='started').count()
    ctx['assesscandidate_completed'] = AssessCandidate.objects.filter(status='completed').count()
    ctx['assessquestion_count'] = AssessQuestion.objects.count()
    ctx['assessquestion_mcq'] = AssessQuestion.objects.filter(question_type='mcq').count()
    ctx['assessquestion_true_false'] = AssessQuestion.objects.filter(question_type='true_false').count()
    ctx['assessquestion_coding'] = AssessQuestion.objects.filter(question_type='coding').count()
    ctx['recent'] = Assessment.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def assessment_list(request):
    qs = Assessment.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'assessment_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def assessment_create(request):
    if request.method == 'POST':
        obj = Assessment()
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.questions_count = request.POST.get('questions_count') or 0
        obj.status = request.POST.get('status', '')
        obj.attempts = request.POST.get('attempts') or 0
        obj.pass_score = request.POST.get('pass_score') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/assessments/')
    return render(request, 'assessment_form.html', {'editing': False})


@login_required
def assessment_edit(request, pk):
    obj = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.questions_count = request.POST.get('questions_count') or 0
        obj.status = request.POST.get('status', '')
        obj.attempts = request.POST.get('attempts') or 0
        obj.pass_score = request.POST.get('pass_score') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/assessments/')
    return render(request, 'assessment_form.html', {'record': obj, 'editing': True})


@login_required
def assessment_delete(request, pk):
    obj = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/assessments/')


@login_required
def assesscandidate_list(request):
    qs = AssessCandidate.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'assesscandidate_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def assesscandidate_create(request):
    if request.method == 'POST':
        obj = AssessCandidate()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.assessment_title = request.POST.get('assessment_title', '')
        obj.score = request.POST.get('score') or 0
        obj.status = request.POST.get('status', '')
        obj.started_at = request.POST.get('started_at') or None
        obj.completed_at = request.POST.get('completed_at') or None
        obj.percentile = request.POST.get('percentile') or 0
        obj.save()
        return redirect('/assesscandidates/')
    return render(request, 'assesscandidate_form.html', {'editing': False})


@login_required
def assesscandidate_edit(request, pk):
    obj = get_object_or_404(AssessCandidate, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.assessment_title = request.POST.get('assessment_title', '')
        obj.score = request.POST.get('score') or 0
        obj.status = request.POST.get('status', '')
        obj.started_at = request.POST.get('started_at') or None
        obj.completed_at = request.POST.get('completed_at') or None
        obj.percentile = request.POST.get('percentile') or 0
        obj.save()
        return redirect('/assesscandidates/')
    return render(request, 'assesscandidate_form.html', {'record': obj, 'editing': True})


@login_required
def assesscandidate_delete(request, pk):
    obj = get_object_or_404(AssessCandidate, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/assesscandidates/')


@login_required
def assessquestion_list(request):
    qs = AssessQuestion.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(assessment_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(question_type=status_filter)
    return render(request, 'assessquestion_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def assessquestion_create(request):
    if request.method == 'POST':
        obj = AssessQuestion()
        obj.assessment_title = request.POST.get('assessment_title', '')
        obj.question = request.POST.get('question', '')
        obj.question_type = request.POST.get('question_type', '')
        obj.difficulty = request.POST.get('difficulty', '')
        obj.points = request.POST.get('points') or 0
        obj.position = request.POST.get('position') or 0
        obj.correct_answer = request.POST.get('correct_answer', '')
        obj.save()
        return redirect('/assessquestions/')
    return render(request, 'assessquestion_form.html', {'editing': False})


@login_required
def assessquestion_edit(request, pk):
    obj = get_object_or_404(AssessQuestion, pk=pk)
    if request.method == 'POST':
        obj.assessment_title = request.POST.get('assessment_title', '')
        obj.question = request.POST.get('question', '')
        obj.question_type = request.POST.get('question_type', '')
        obj.difficulty = request.POST.get('difficulty', '')
        obj.points = request.POST.get('points') or 0
        obj.position = request.POST.get('position') or 0
        obj.correct_answer = request.POST.get('correct_answer', '')
        obj.save()
        return redirect('/assessquestions/')
    return render(request, 'assessquestion_form.html', {'record': obj, 'editing': True})


@login_required
def assessquestion_delete(request, pk):
    obj = get_object_or_404(AssessQuestion, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/assessquestions/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['assessment_count'] = Assessment.objects.count()
    data['assesscandidate_count'] = AssessCandidate.objects.count()
    data['assessquestion_count'] = AssessQuestion.objects.count()
    return JsonResponse(data)
