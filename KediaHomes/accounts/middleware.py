from django.utils.deprecation import MiddlewareMixin
from .forms import *
from django.http import HttpResponse
from Kedia.models import Projects, OurProjects
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from KediaHomes.form_error import form_error_json


class AuthenticationMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        jwt_object = JWTAuthentication()
        header = jwt_object.get_header(request)
        if header is not None:
            raw_token = jwt_object.get_raw_token(header)
            validated_token = jwt_object.get_validated_token(raw_token)
            user = jwt_object.get_user(validated_token)
            if user.token == str(validated_token):
                request.user = user
                return None
            else:
                return Response(data={'error': "Invalid Token"}, status=404)


class CommonResponseMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.project_config = {
            'Villa': Projects.objects.filter(type='Villa', is_active=True),
            'Apartment': Projects.objects.filter(type='Apartment', is_active=True),
            'Plots': Projects.objects.filter(type='Plots', is_active=True),
            'our_projects': OurProjects.objects.filter()

        }


class UserLoginMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = UserLoginForm(data=request.POST if request.POST else request.data)
            if form.is_valid():
                return view_func(request, form)
            else:
                return Response(data=form_error_json(form), status=500)


class APIRegisterMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            user = request.user if request.user.is_authenticated else None
            form = RegisterForm(data=request.data, initial=user)
            if form.is_valid():
                return view_func(request, form)
            else:
                return Response(data=form_error_json(form), status=500)


class APIProfileMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "PUT":
            form = ProfileForm(data=request.data, instance=request.user, files=request.FILES)
            if form.is_valid():
                return view_func(request, form)
            else:
                return Response(data=form_error_json(form), status=500)
        return view_func(request, None)


class ErrorHandleMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        return HttpResponse(exception)


class RegisterMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            user = request.user if request.user.is_authenticated else None
            form = RegisterForm(data=request.POST, initial=user)
            return view_func(request, form)


class ProfileMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            return view_func(request, form)


class ForgetPasswordMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = ForgetPasswordForm(data=request.POST)
            return view_func(request, form)
        else:
            return view_func(request, ForgetPasswordForm())
