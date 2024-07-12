from django.contrib import admin
from .models import JobListing, Tag, Category, Company

admin.site.register(JobListing)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Company)
