from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import decorator_from_middleware
from django.core.paginator import Paginator
from .middleware import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
import uuid
import razorpay
from .models import Booking_new, Blog


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@decorator_from_middleware(ContactUsMiddleware)
def contact(request, form=None):
    if request.method == "POST":
        if form.is_valid():
            form.cleaned_data['user'] = request.user if request.user.is_authenticated else None
            ContactUs(**form.cleaned_data).save()
    return redirect('/')


def gallery(request):
    page = 1 if 'page' not in request.GET else request.GET['page'] if request.GET['page'] else 1
    gallery_obj = Gallery.objects.filter(is_active=True)
    p = Paginator(gallery_obj, 12)
    gallery_data = p.page(page)
    gallery_list = []
    batch_gallery = []
    for i in gallery_data:
        batch_gallery.append(i)
        if len(batch_gallery) >= 3:
            gallery_list.append(batch_gallery)
            batch_gallery = []
    if len(batch_gallery) < 3:
        gallery_list.append(batch_gallery)
    return render(request, 'gallery.html',
                  {'gallery': gallery_list if any(gallery_list) else [batch_gallery, ], 'gallery_data': gallery_data})



def projects_view(request, slug):
    project_obj = Projects.objects.filter(slug=slug, is_active=True, projects_details__isnull=False)
    if project_obj.exists():
        return render(request, 'pricing.html', {'project': project_obj.first()})
    else:
        return render(request, '404.html')


@decorator_from_middleware(NewsLetterMiddleware)
def news_letter(request, form=None):
    if request.method == "POST":
        if form.is_valid():
            form.cleaned_data['user'] = request.user if request.user.is_authenticated else None
            NewsLetter(**form.cleaned_data).save()
        else:
            print(form.errors)
    return redirect('/')


def map_page_view(request):
    return render(request, 'map_page.html')


def map_view(request):
    map_obj = Map.objects.all()
    return render(request, 'map.html', {'maps': map_obj})


@api_view(['GET', ])
def get_map_one_view(request, id=None):
    if id and Map.objects.filter(id=id).exists():
        map_obj = Map.objects.get(id=id)
        map = map_obj.__dict__
        map.pop('_state')
        map.pop('created_at')
        map.pop('update_at')
        return JsonResponse(map_obj.__dict__, status=200)
    return JsonResponse({'error': 'Map ID is not Correct'}, status=500)


@login_required()
def booking_view(request, id=None):
    if request.method == "POST":
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phone')
        dob = postData.get('dob')
        pan = postData.get('pan')
        country = postData.get('country')
        address = postData.get("address")
        city = postData.get('city')
        state = postData.get('state')
        zip = postData.get('zip')
        plot = Map.objects.get(id=id)
        plot_no = plot.plot_no
        

        value = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'dob' : dob,
            'pan' : pan,
            'country' : country,
            'address' : address,
            'city' : city,
            'state' : state,
            'zip' : zip,
            'plot_no' : plot_no,
        }
        booking_new = Booking_new(email=email,
                                  name=name,
                                  phone=phone,
                                  dob=dob,
                                  pan=pan,
                                  country=country,
                                  address=address,
                                  city=city,
                                  state=state,
                                  zip=zip,
                                  plot_no=plot_no)
        booking_new.register()
        return render(request, 'payment_gateway.html')
    else:
        if id and Map.objects.filter(id=id).exists():
            plot = Map.objects.get(id=id)
            print(plot)
            rand_id = str(uuid.uuid4()).replace('-', '')
            if Booking.objects.filter(user=request.user, plot=plot).exists():
                booking = Booking.objects.get(user=request.user, plot=plot)
            else:
                booking = Booking.objects.create(user=request.user, plot=plot, booking_no=rand_id)
            return render(request, 'booking.html', {'booking': booking, 'plot': plot})

def payment_gateway(request):
    if request.method == "POST":
        amount = 200000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_live_GSu749zmGMPc2s', 'OP0Hk8pMkM3rFsVhaIsJw2nu'))
        # client = razorpay.Client(auth=('rzp_test_SiVKbGwENw5IBn', 'SpEy59vK3tRgbjicGZXU0edO'))
        payment = client.order.create({'amount':amount, 'payment_capture':'1'})
    return render(request, 'payment_gateway.html')

def success(request):
    return render(request, 'success.html')
def failure(request):
    return render(request, 'failure.html')

def privacy(request):
    return render(request, 'privacy.html')


def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')


def disclaimer(request):
    return render(request, 'Disclaimer.html')


def palm(request):
    return render(request, 'palm.html')


def oxygen(request):
    return render(request, 'oxygen.html')


def corridor(request):
    return render(request, 'corridor.html')


def ganesh(request):
    return render(request, 'ganesh.html')


def ganeshext(request):
    return render(request, 'ganeshext.html')


def corpclub(request):
    return render(request, 'corpclub.html')


def kingdom(request):
    return render(request, 'kingdom.html')


def capital(request):
    return render(request, 'capital.html')


def projects(request):
    page = 1 if 'page' not in request.GET else request.GET['page'] if request.GET['page'] else 1
    gallery_obj = OurProjects.objects.filter(is_active=True)
    p = Paginator(gallery_obj, 50)
    gallery_data = p.page(page)
    gallery_list = []
    batch_gallery = []
    for i in gallery_data:
        batch_gallery.append(i)
        if len(batch_gallery) >= 4:
            gallery_list.append(batch_gallery)
            batch_gallery = []
    if len(batch_gallery) < 4:
        gallery_list.append(batch_gallery)
    return render(request, 'allprojects.html',
                  {'gallery': gallery_list if any(gallery_list) else [batch_gallery, ], 'gallery_data': gallery_data})



# edits
def sold_out(request):
    return render(request, 'sold_out.html')






def blog(request):
    blogs = Blog.objects.all()
    values = {
        'blogs' : blogs
    }
    print(blogs)
    for blog in blogs:
        title = blog.title
        print(title)
    return render(request, 'blog.html', values)

def comingsoon(request):
    return render(request, 'comingsoon.html')

def indextest(request):
    return render(request, 'indextest.html')



