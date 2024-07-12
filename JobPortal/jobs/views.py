from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import JobListing, Category, Tag, Company
from .serializers import JobListingSerializer, CategorySerializer, TagSerializer, CompanySerializer
from django.http import Http404


class JobListingViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            job_listings = JobListing.objects.all()
            serializer = JobListingSerializer(job_listings, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = JobListingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            job_listing = self.get_object(pk)
            serializer = JobListingSerializer(job_listing)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            job_listing = self.get_object(pk)
            serializer = JobListingSerializer(job_listing, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return JobListing.objects.get(pk=pk)
        except JobListing.DoesNotExist:
            raise Http404
        
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            job_listing = self.get_object(pk)
            serializer = JobListingSerializer(job_listing, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            job_listing = self.get_object(pk)
            job_listing.delete()
            return Response({"status": True, "msg": "Job deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def get_remote_jobs(self, request):
        try:
            remote_jobs = JobListing.objects.filter(remote_option=True)
            serializer = JobListingSerializer(remote_jobs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
   

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            category_objs = Category.objects.all()
            serializer = CategorySerializer(category_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            category_obj = self.get_object(pk)
            serializer = CategorySerializer(category_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            category_obj = self.get_object(pk)
            serializer = CategorySerializer(category_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
        
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            category_obj = self.get_object(pk)
            serializer = CategorySerializer(category_obj, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            category_obj = self.get_object(pk)
            category_obj.delete()
            return Response({"status": True, "msg": "Category deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TagViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            tag_objs = Tag.objects.all()
            serializer = TagSerializer(tag_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = TagSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            tag_obj = self.get_object(pk)
            serializer = TagSerializer(tag_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            tag_obj = self.get_object(pk)
            serializer = TagSerializer(tag_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404
        
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            tag_obj = self.get_object(pk)
            serializer = TagSerializer(tag_obj, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            tag_obj = self.get_object(pk)
            tag_obj.delete()
            return Response({"status": True, "msg": "Tag deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CompanyViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            company_objs = Company.objects.all()
            serializer = CompanySerializer(company_objs, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            company_obj = self.get_object(pk)
            serializer = CompanySerializer(company_obj)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            company_obj = self.get_object(pk)
            serializer = CompanySerializer(company_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
        
    @action(detail=True, methods=['patch'])
    def parital_update(self, request, pk=None):
        try:
            company_obj = self.get_object(pk)
            serializer = CompanySerializer(company_obj, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        try:
            company_obj = self.get_object(pk)
            company_obj.delete()
            return Response({"status": True, "msg": "Company deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
