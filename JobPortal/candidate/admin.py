from django.contrib import admin
from .models import CandidateProfile, Education, Skill, Experience, Resume, Application

admin.site.register(CandidateProfile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Resume)
admin.site.register(Application)
