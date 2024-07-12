from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_companies', limit_choices_to={'role': 'company'})

    def __str__(self):
        return f"{self.name} managed by {self.managed_by}"

class JobListing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_listings')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='job_listings')
    tags = models.ManyToManyField(Tag, blank=True, related_name='job_listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)  # E.g., Full-time, Part-time
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)  # E.g., Junior, Mid, Senior
    remote_option = models.BooleanField(default=False)
    application_deadline = models.DateField(blank=True, null=True)
    is_opened = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.title} by {self.company}"
