from django.utils.decorators import decorator_from_middleware
from django.core.paginator import Paginator
from .middleware import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['GET', ])
def api_projects_view(request, slug=None):
    if slug:
        if Projects.objects.filter(slug=slug, is_active=True).exists():
            serializer = ProjectsSerializer(instance=Projects.objects.get(slug=slug, is_active=True), many=False)
            return Response(data=serializer.data, status=200)
        else:
            return Response(data={'error': "Projects is not Active Now"}, status=200)
    else:
        serializer = ProjectsSerializer(instance=Projects.objects.filter(), many=True)
        return Response(data=serializer.data, status=200)


@api_view(['GET', ])
def api_map_view(request):
    serializer = MapSerializer(instance=Map.objects.all(), many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET', ])
def api_map_one_view(request, plot_no):
    serializer = MapSerializer(instance=Map.objects.get(plot_no=plot_no), many=False)
    return Response(data=serializer.data, status=200)


@api_view(['POST', ])
@decorator_from_middleware(ContactUsMiddleware)
def api_contact_us_view(request, form):
    if form.is_valid():
        serializer = ContactUsSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Thank you, we will contact you soon"}, status=200)
        else:
            return Response(data=serializer.errors, status=200)
    else:
        return Response(data=form.errors.as_json(), status=200)


@api_view(['POST', ])
@decorator_from_middleware(NewsLetterMiddleware)
def api_news_letter_view(request, form):
    if form.is_valid():
        serializer = NewsLetterSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Thank you, we will contact you soon"}, status=200)
        else:
            return Response(data=serializer.errors, status=200)
    else:
        return Response(data=form.errors.as_json(), status=200)
