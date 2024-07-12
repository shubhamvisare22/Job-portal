from rest_framework import serializers
from .models import CandidateProfile, Application, Resume, Education, Experience, Skill
from jobs.models import JobListing
from django.core.validators import RegexValidator, URLValidator

class CandidateProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  

    cand_full_name = serializers.CharField(
        max_length=255, 
        required=True, 
        validators=[RegexValidator(regex='^[a-zA-Z ]*$', message='Full name must contain only letters and spaces.')]
    )
    cand_phone_number = serializers.CharField(
        max_length=15, 
        required=False, 
        allow_blank=True, 
        validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')]
    )
    cand_location = serializers.CharField(max_length=255, required=False, allow_blank=True)
    cand_bio = serializers.CharField(required=False, allow_blank=True)
    cand_profile_picture = serializers.ImageField(required=False, allow_null=True)
    cand_linkedin_url = serializers.URLField(
        max_length=255, 
        required=False, 
        allow_blank=True, 
        validators=[URLValidator(message='Enter a valid LinkedIn URL.')]
    )
    cand_website_url = serializers.URLField(
        max_length=255, 
        required=False, 
        allow_blank=True, 
        validators=[URLValidator(message='Enter a valid website URL.')]
    )

    class Meta:
        model = CandidateProfile
        fields = [
            'id', 'user', 'cand_full_name', 'cand_phone_number', 
            'cand_location', 'cand_bio', 'cand_profile_picture', 
            'cand_linkedin_url', 'cand_website_url', 'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class ApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=CandidateProfile.objects.all())
    job_listing = serializers.PrimaryKeyRelatedField(queryset=JobListing.objects.all())
    resume = serializers.PrimaryKeyRelatedField(queryset=Resume.objects.all(), required=False, allow_null=True)
    cover_letter = serializers.CharField(required=False, allow_blank=True)
    status = serializers.ChoiceField(choices=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='pending')

    class Meta:
        model = Application
        fields = [
            'id', 'candidate', 'job_listing', 'created_at', 'updated_at',
            'status', 'cover_letter', 'resume'
        ]
        read_only_fields = ['id', 'created_at','updated_at']

    def validate(self, data):
        if Application.objects.filter(candidate=data['candidate'], job_listing=data['job_listing']).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        return data

class ResumeSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=CandidateProfile.objects.all())
    resume_file = serializers.FileField()

    class Meta:
        model = Resume
        fields = ['id', 'candidate', 'resume_file', 'created_at']
        read_only_fields = ['id', 'created_at']

class EducationSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=CandidateProfile.objects.all())
    institution_name = serializers.CharField(max_length=255, required=True)
    degree = serializers.CharField(max_length=255, required=True)
    field_of_study = serializers.CharField(max_length=255, required=False, allow_blank=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=False, allow_null=True)
    grade = serializers.CharField(max_length=50, required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Education
        fields = [
            'id', 'candidate', 'institution_name', 'degree', 
            'field_of_study', 'start_date', 'end_date', 'grade', 
            'description'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        if data['end_date'] and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data

class ExperienceSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=CandidateProfile.objects.all())
    job_title = serializers.CharField(max_length=255, required=True)
    company_name = serializers.CharField(max_length=255, required=True)
    location = serializers.CharField(max_length=255, required=False, allow_blank=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=False, allow_null=True)
    responsibilities = serializers.CharField(required=False, allow_blank=True)
    currently_working = serializers.BooleanField(default=False)

    class Meta:
        model = Experience
        fields = [
            'id', 'candidate', 'job_title', 'company_name', 
            'location', 'start_date', 'end_date', 
            'responsibilities', 'currently_working'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        if data['end_date'] and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data

class SkillSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=CandidateProfile.objects.all())
    name = serializers.CharField(max_length=100, required=True)
    proficiency = serializers.ChoiceField(choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ], default='beginner')

    class Meta:
        model = Skill
        fields = ['id', 'candidate', 'name', 'proficiency']
        read_only_fields = ['id']
