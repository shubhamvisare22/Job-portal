from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobListingViewSet, CategoryViewSet, TagViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'job', JobListingViewSet, basename='job')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    
    # ---------------------------------- Jobs ---------------------------------------
    path('job-list/', JobListingViewSet.as_view({'get': 'list'}), name='job-list'),
    path('job-create/', JobListingViewSet.as_view({'post': 'create'}), name='job-create'),
    path('job-retrieve/<int:pk>/', JobListingViewSet.as_view({'get': 'retrieve'}), name='job-retrieve'),
    path('job-update/<int:pk>/', JobListingViewSet.as_view({'put': 'update'}), name='job-update'),
    path('job-parital-update/<int:pk>/', JobListingViewSet.as_view({'patch': 'parital_update'}), name='job-parital-update'),
    path('job-delete/<int:pk>/', JobListingViewSet.as_view({'delete': 'delete'}), name='job-delete'),
    path('get-remote-jobs/', JobListingViewSet.as_view({'get': 'get_remote_jobs'}), name='get-remote-jobs'),
    
    # ---------------------------------- Category ---------------------------------------
    path('category-list/', CategoryViewSet.as_view({'get': 'list'}), name='category-list'),
    path('category-create/', CategoryViewSet.as_view({'post': 'create'}), name='category-create'),
    path('category-retrieve/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category-retrieve'),
    path('category-update/<int:pk>/', CategoryViewSet.as_view({'put': 'update'}), name='category-update'),
    path('category-parital-update/<int:pk>/', CategoryViewSet.as_view({'patch': 'parital_update'}), name='category-parital-update'),
    path('category-delete/<int:pk>/', CategoryViewSet.as_view({'delete': 'delete'}), name='category-delete'),

    # ---------------------------------- Tags ---------------------------------------
    path('tag-list/', TagViewSet.as_view({'get': 'list'}), name='tag-list'),
    path('tag-create/', TagViewSet.as_view({'post': 'create'}), name='tag-create'),
    path('tag-retrieve/<int:pk>/', TagViewSet.as_view({'get': 'retrieve'}), name='tag-retrieve'),
    path('tag-update/<int:pk>/', TagViewSet.as_view({'put': 'update'}), name='tag-update'),
    path('tag-parital-update/<int:pk>/', TagViewSet.as_view({'patch': 'parital_update'}), name='tag-parital-update'),
    path('tag-delete/<int:pk>/', TagViewSet.as_view({'delete': 'delete'}), name='tag-delete'),

    # ---------------------------------- Company ---------------------------------------
    path('company-list/', CompanyViewSet.as_view({'get': 'list'}), name='company-list'),
    path('company-create/', CompanyViewSet.as_view({'post': 'create'}), name='company-create'),
    path('company-retrieve/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve'}), name='company-retrieve'),
    path('company-update/<int:pk>/', CompanyViewSet.as_view({'put': 'update'}), name='company-update'),
    path('company-parital-update/<int:pk>/', CompanyViewSet.as_view({'patch': 'parital_update'}), name='company-parital-update'),
    path('company-delete/<int:pk>/', CompanyViewSet.as_view({'delete': 'delete'}), name='company-delete'),

]
