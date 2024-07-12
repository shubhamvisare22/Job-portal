from django.db import models
from django.conf import settings
from jobs.models import JobListing  

User = settings.AUTH_USER_MODEL

class CandidateProfile(models.Model):
    """
    Stores detailed information about the candidate.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile', limit_choices_to={'role': 'candidate'})
    cand_full_name = models.CharField(max_length=255)
    cand_phone_number = models.CharField(max_length=15, blank=True, null=True)
    cand_location = models.CharField(max_length=255, blank=True, null=True)
    cand_bio = models.TextField(blank=True, null=True)
    cand_profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    cand_linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    cand_website_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cand_full_name

class Application(models.Model):
    """
    Tracks the jobs a candidate has applied for and their application status.
    """
    
    APPLICATION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications')
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey('Resume', on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, default='pending')
    cover_letter = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('candidate', 'job_listing')

    def __str__(self):
        return f"{self.candidate} applied to {self.job_listing}"

class Resume(models.Model):
    """
    Stores resumes or CVs uploaded by the candidate.
    """
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='resumes')
    resume_file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Resume for {self.candidate}"

class Education(models.Model):
    """
    Tracks educational background.
    """
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='educations')
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"

class Experience(models.Model):
    """
    Tracks professional experience.
    """
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Skill(models.Model):
    """
    Lists skills the candidate has.
    """
    
    SKILL_PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, choices=SKILL_PROFICIENCY_CHOICES, default='beginner')

    def __str__(self):
        return f"{self.name} ({self.proficiency})"
