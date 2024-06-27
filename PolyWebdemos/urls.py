"""
URL configuration for PolyWebdemos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from main_app.views import LecturerViewSet, PersonViewSet, CourseViewSet, SlideViewSet, PresentationViewSet, \
    presentation_view, presentation_detail_view, index

router = routers.DefaultRouter()
# api урлы в которых лежат данные модели
router.register('api/lecturer', LecturerViewSet)
router.register('api/person', PersonViewSet)
router.register('api/course', CourseViewSet)
router.register('api/presentation', PresentationViewSet)
router.register('api/slide', SlideViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('', include(router.urls)),
    path('presentation/', presentation_view),
    path('presentations/<int:presentation_id>/', presentation_detail_view, name='presentation_detail'),
    path('api/', include(router.urls)),
    path('', index, name='index'),
]
