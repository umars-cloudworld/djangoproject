from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from .forms import *
from django.http import HttpResponse
from django.urls import resolve


class ContactUsMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = ContactUsForm(data=request.POST)
            return view_func(request, form)
        else:
            return view_func(request)


class NewsLetterMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = NewsLetterForm(data=request.POST)
            return view_func(request, form)
