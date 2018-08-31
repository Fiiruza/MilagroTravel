from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from .forms import *


class HomePage(View):

    def get(self, request):
        tours = Tour.objects.all()
        request_form = RequestForm()
        context = {
            'tours': tours,
            'request_form': request_form
        }

        return render(request, 'home.html', context)

    def post(self, request):
        request_form = RequestForm(request.POST)
        #request_form.name = request.POST.cleaned_data['name']
        #request_form.email = request.POST.cleaned_data['email']
        #request_form.phone_number = request.cleaned_data['phone_number']
        #request_form.message = request.POST.cleaned_data['message']
        if request_form.is_valid():
            request_form.save()
            context = {
                'name': request_form.cleaned_data['name']
            }
            return render(request, 'success.html', context)
        else:
            tours = Tour.objects.all()
            request_form = RequestForm()
            context = {
                'tours': tours,
                'request_form': request_form
            }
            return render(request, 'home.html', context)


class NewsApi(View):
    def get(self, request):
        requested_page_number = request.GET.get('page', 1)
        news = NewsPost.objects.all().order_by('-published_date')
        paginator = Paginator(news, 3)
        try:
            posts = paginator.get_page(requested_page_number)
        except PageNotAnInteger or EmptyPage:
            posts = paginator.get_page(1)
        posts_as_jsons = []
        for post in posts:
            posts_as_jsons.append(post.as_dict())
        pages = paginator.num_pages
        result = {
            'posts': posts_as_jsons,
            'pages': pages
        }
        return JsonResponse(result)

