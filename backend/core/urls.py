from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('assessments/', views.assessment_list, name='assessment_list'),
    path('assessments/create/', views.assessment_create, name='assessment_create'),
    path('assessments/<int:pk>/edit/', views.assessment_edit, name='assessment_edit'),
    path('assessments/<int:pk>/delete/', views.assessment_delete, name='assessment_delete'),
    path('assesscandidates/', views.assesscandidate_list, name='assesscandidate_list'),
    path('assesscandidates/create/', views.assesscandidate_create, name='assesscandidate_create'),
    path('assesscandidates/<int:pk>/edit/', views.assesscandidate_edit, name='assesscandidate_edit'),
    path('assesscandidates/<int:pk>/delete/', views.assesscandidate_delete, name='assesscandidate_delete'),
    path('assessquestions/', views.assessquestion_list, name='assessquestion_list'),
    path('assessquestions/create/', views.assessquestion_create, name='assessquestion_create'),
    path('assessquestions/<int:pk>/edit/', views.assessquestion_edit, name='assessquestion_edit'),
    path('assessquestions/<int:pk>/delete/', views.assessquestion_delete, name='assessquestion_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
