from django.urls import path
from .views import CandidateProfileViewset, ResumeViewset, EducationViewset, ExperienceViewset, SkillViewset, ApplicationViewset


urlpatterns = [

    # -------------------------------- Candidate ------------------------------------
    path('candidate-list/', CandidateProfileViewset.as_view({'get': 'list'}), name='candidate-list'),
    path('candidate-create/', CandidateProfileViewset.as_view({'post': 'create'}), name='candidate-create'),
    path('candidate-retrieve/<int:pk>/', CandidateProfileViewset.as_view({'get': 'retrieve'}), name='candidate-retrieve'),
    path('candidate-update/<int:pk>/', CandidateProfileViewset.as_view({'put': 'update'}), name='candidate-update'),
    path('candidate-parital-update/<int:pk>/', CandidateProfileViewset.as_view({'patch': 'parital_update'}), name='candidate-parital-update'),
    path('candidate-delete/<int:pk>/', CandidateProfileViewset.as_view({'delete': 'delete'}), name='candidate-delete'),
    
    # -------------------------------- Resumes ------------------------------------
    path('resume-list/', ResumeViewset.as_view({'get': 'list'}), name='resume-list'),
    path('resume-create/', ResumeViewset.as_view({'post': 'create'}), name='resume-create'),
    path('resume-retrieve/<int:pk>/', ResumeViewset.as_view({'get': 'retrieve'}), name='resume-retrieve'),
    path('resume-update/<int:pk>/', ResumeViewset.as_view({'put': 'update'}), name='resume-update'),
    path('resume-parital-update/<int:pk>/', ResumeViewset.as_view({'patch': 'parital_update'}), name='resume-parital-update'),
    path('resume-delete/<int:pk>/', ResumeViewset.as_view({'delete': 'delete'}), name='resume-delete'),

    # -------------------------------- Education ------------------------------------
    path('education-list/', EducationViewset.as_view({'get': 'list'}), name='education-list'),
    path('education-create/', EducationViewset.as_view({'post': 'create'}), name='education-create'),
    path('education-retrieve/<int:pk>/', EducationViewset.as_view({'get': 'retrieve'}), name='education-retrieve'),
    path('education-update/<int:pk>/', EducationViewset.as_view({'put': 'update'}), name='education-update'),
    path('education-parital-update/<int:pk>/', EducationViewset.as_view({'patch': 'parital_update'}), name='education-parital-update'),
    path('education-delete/<int:pk>/', EducationViewset.as_view({'delete': 'delete'}), name='education-delete'),

    # -------------------------------- Experience ------------------------------------
    path('experience-list/', ExperienceViewset.as_view({'get': 'list'}), name='experience-list'),
    path('experience-create/', ExperienceViewset.as_view({'post': 'create'}), name='experience-create'),
    path('experience-retrieve/<int:pk>/', ExperienceViewset.as_view({'get': 'retrieve'}), name='experience-retrieve'),
    path('experience-update/<int:pk>/', ExperienceViewset.as_view({'put': 'update'}), name='experience-update'),
    path('experience-parital-update/<int:pk>/', ExperienceViewset.as_view({'patch': 'parital_update'}), name='experience-parital-update'),
    path('experience-delete/<int:pk>/', ExperienceViewset.as_view({'delete': 'delete'}), name='experience-delete'),

    # -------------------------------- Skill ------------------------------------
    path('skill-list/', SkillViewset.as_view({'get': 'list'}), name='skill-list'),
    path('skill-create/', SkillViewset.as_view({'post': 'create'}), name='skill-create'),
    path('skill-retrieve/<int:pk>/', SkillViewset.as_view({'get': 'retrieve'}), name='skill-retrieve'),
    path('skill-update/<int:pk>/', SkillViewset.as_view({'put': 'update'}), name='skill-update'),
    path('skill-parital-update/<int:pk>/', SkillViewset.as_view({'patch': 'parital_update'}), name='skill-parital-update'),
    path('skill-delete/<int:pk>/', SkillViewset.as_view({'delete': 'delete'}), name='skill-delete'),

    # -------------------------------- Application ------------------------------------
    path('application-list/', ApplicationViewset.as_view({'get': 'list'}), name='application-list'),
    path('application-create/', ApplicationViewset.as_view({'post': 'create'}), name='application-create'),
    path('application-retrieve/<int:pk>/', ApplicationViewset.as_view({'get': 'retrieve'}), name='application-retrieve'),
    path('application-update/<int:pk>/', ApplicationViewset.as_view({'put': 'update'}), name='application-update'),
    path('application-parital-update/<int:pk>/', ApplicationViewset.as_view({'patch': 'parital_update'}), name='application-parital-update'),
    path('application-delete/<int:pk>/', ApplicationViewset.as_view({'delete': 'delete'}), name='application-delete'),

]