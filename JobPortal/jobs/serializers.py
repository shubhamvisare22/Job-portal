from rest_framework import serializers
from .models import Category, Tag, Company, JobListing
from .utils import valid_website

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
        

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    website = serializers.URLField(max_length=255, allow_blank=True, allow_null=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'website', 'description', 'created_at', 'updated_at', 'managed_by')
        read_only_fields = ('id', 'created_at', 'updated_at', 'managed_by')

    def validate_website(self, value):
        if value and not valid_website(value):
            raise serializers.ValidationError("Invalid website entered.")
        return value

class JobListingSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = TagSerializer(many=True, required=False)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    requirements = serializers.CharField(allow_blank=True, allow_null=True)
    responsibilities = serializers.CharField(allow_blank=True, allow_null=True)
    location = serializers.CharField(max_length=100, required=True)
    job_type = serializers.CharField(max_length=50, required=True)
    salary = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True, required=False)
    experience_level = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    remote_option = serializers.BooleanField(default=False)
    application_deadline = serializers.DateField(allow_null=True, required=False)

    class Meta:
        model = JobListing
        fields = (
            'id', 'company', 'category', 'tags', 'title', 'description', 'requirements', 
            'responsibilities', 'location', 'job_type', 'salary', 'experience_level', 
            'remote_option', 'application_deadline', 'created_at', 'updated_at','is_opened'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Job title must be at least 5 characters long.")
        return value

    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Job description must be at least 20 characters long.")
        return value

    def validate_location(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Location must only contain alphabetic characters.")
        return value

    def validate_job_type(self, value):
        allowed_job_types = ('Full-time', 'Part-time', 'Contract', 'Temporary', 'Internship')
        if value not in allowed_job_types:
            raise serializers.ValidationError(f"Job type must be one of: {', '.join(allowed_job_types)}")
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        job_listing = JobListing.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            job_listing.tags.add(tag)
        return job_listing

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.requirements = validated_data.get('requirements', instance.requirements)
        instance.responsibilities = validated_data.get('responsibilities', instance.responsibilities)
        instance.location = validated_data.get('location', instance.location)
        instance.job_type = validated_data.get('job_type', instance.job_type)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.experience_level = validated_data.get('experience_level', instance.experience_level)
        instance.remote_option = validated_data.get('remote_option', instance.remote_option)
        instance.application_deadline = validated_data.get('application_deadline', instance.application_deadline)
        instance.save()

        # Update tags
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(**tag_data)
                instance.tags.add(tag)

        return instance
