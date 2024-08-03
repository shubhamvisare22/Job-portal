from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CandidateProfile, Resume, Education, Experience, Skill, Application
from .serializers import CandidateProfileSerializer, ResumeSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer, ApplicationSerializer
from django.http import Http404
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(tags=['Candidate']),
    create=extend_schema(tags=['Candidate']),
    retrieve=extend_schema(tags=['Candidate']),
    update=extend_schema(tags=['Candidate']),
    delete=extend_schema(tags=['Candidate']),
)
class CandidateProfileViewset(viewsets.ViewSet):
    def list(self, request):
        try:
            candidate_profile_objs = CandidateProfile.objects.all()
            serializer = CandidateProfileSerializer(
                candidate_profile_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = CandidateProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            candidate_profile_obj = self.get_object(pk)
            serializer = CandidateProfileSerializer(candidate_profile_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            candidate_profile_obj = self.get_object(pk)
            serializer = CandidateProfileSerializer(
                candidate_profile_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return CandidateProfile.objects.get(pk=pk)
        except CandidateProfile.DoesNotExist:
            raise Http404

    @extend_schema(tags=['Candidate'])
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            candidate_profile_obj = self.get_object(pk)
            serializer = CandidateProfileSerializer(
                candidate_profile_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            candidate_profile_obj = self.get_object(pk)
            candidate_profile_obj.delete()
            return Response({"status": True, "msg": "candidate deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=['Resume']),
    create=extend_schema(tags=['Resume']),
    retrieve=extend_schema(tags=['Resume']),
    update=extend_schema(tags=['Resume']),
    delete=extend_schema(tags=['Resume']),
)
class ResumeViewset(viewsets.ViewSet):
    def list(self, request):
        try:
            resume_objs = Resume.objects.all()
            serializer = ResumeSerializer(resume_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = ResumeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            resume_obj = self.get_object(pk)
            serializer = ResumeSerializer(resume_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            resume_obj = self.get_object(pk)
            serializer = ResumeSerializer(resume_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            raise Http404

    @extend_schema(tags=['Candidate'])
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            resume_obj = self.get_object(pk)
            serializer = ResumeSerializer(
                resume_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            resume_obj = self.get_object(pk)
            resume_obj.delete()
            return Response({"status": True, "msg": "resume deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=['Education']),
    create=extend_schema(tags=['Education']),
    retrieve=extend_schema(tags=['Education']),
    update=extend_schema(tags=['Education']),
    delete=extend_schema(tags=['Education']),
)
class EducationViewset(viewsets.ViewSet):

    def list(self, request):
        try:
            education_objs = Education.objects.all()
            serializer = EducationSerializer(education_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = EducationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            education_obj = self.get_object(pk)
            serializer = EducationSerializer(education_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            education_obj = self.get_object(pk)
            serializer = EducationSerializer(education_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Education.objects.get(pk=pk)
        except Education.DoesNotExist:
            raise Http404

    @extend_schema(tags=['Education'])
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            education_obj = self.get_object(pk)
            serializer = EducationSerializer(
                education_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            education_obj = self.get_object(pk)
            education_obj.delete()
            return Response({"status": True, "msg": "education deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=['Experience']),
    create=extend_schema(tags=['Experience']),
    retrieve=extend_schema(tags=['Experience']),
    update=extend_schema(tags=['Experience']),
    delete=extend_schema(tags=['Experience']),
)
class ExperienceViewset(viewsets.ViewSet):

    def list(self, request):
        try:
            experience_objs = Experience.objects.all()
            serializer = ExperienceSerializer(experience_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = ExperienceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            experience_obj = self.get_object(pk)
            serializer = ExperienceSerializer(experience_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            experience_obj = self.get_object(pk)
            serializer = ExperienceSerializer(
                experience_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise Http404

    @extend_schema(tags=['Experience'])
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            experience_obj = self.get_object(pk)
            serializer = ExperienceSerializer(
                experience_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            experience_obj = self.get_object(pk)
            experience_obj.delete()
            return Response({"status": True, "msg": "experience deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=['Skill']),
    create=extend_schema(tags=['Skill']),
    retrieve=extend_schema(tags=['Skill']),
    update=extend_schema(tags=['Skill']),
    delete=extend_schema(tags=['Skill']),
)
class SkillViewset(viewsets.ViewSet):

    def list(self, request):
        try:
            skill_objs = Skill.objects.all()
            serializer = SkillSerializer(skill_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = SkillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            skill_obj = self.get_object(pk)
            serializer = SkillSerializer(skill_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            skill_obj = self.get_object(pk)
            serializer = SkillSerializer(skill_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    @extend_schema(tags=['Skill'])
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            skill_obj = self.get_object(pk)
            serializer = SkillSerializer(
                skill_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            skill_obj = self.get_object(pk)
            skill_obj.delete()
            return Response({"status": True, "msg": "skill deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=['Application']),
    create=extend_schema(tags=['Application']),
    retrieve=extend_schema(tags=['Application']),
    update=extend_schema(tags=['Application']),
    delete=extend_schema(tags=['Application']),
)
class ApplicationViewset(viewsets.ViewSet):

    def list(self, request):
        try:
            application_objs = Application.objects.all()
            serializer = ApplicationSerializer(application_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = ApplicationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            application_obj = self.get_object(pk)
            serializer = ApplicationSerializer(application_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            application_obj = self.get_object(pk)
            serializer = ApplicationSerializer(
                application_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    @extend_schema(tags=['Application'])
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            application_obj = self.get_object(pk)
            serializer = ApplicationSerializer(
                application_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            application_obj = self.get_object(pk)
            application_obj.delete()
            return Response({"status": True, "msg": "Application deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
