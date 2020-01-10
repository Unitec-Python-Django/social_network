from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse


class HomeIndex(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Home Page')


class PostIndexView(View, TemplateResponseMixin):
    template_name = 'post_index.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context=None)

    def post(self, request, *args, **kwargs):
        data = request.POST
        return HttpResponseRedirect(reverse('posts_detail', kwargs=dict(pk=data['pk'])))

    def delete(self, request, *args, **kwargs):
        data = request.POST
        return HttpResponseRedirect(reverse('posts_detail', kwargs=dict(pk=data['pk'])))


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        return HttpResponse('Post Page - %s' % pk)


class PostDetailTypeView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = kwargs.get('type')

        return HttpResponse('Post Page - %s of Type - %s' % (pk, type))


def home_index(request):
    return HttpResponse('Home Page')


@csrf_protect
def post_index(request):
    if request.method == 'GET':
        return render(request=request, template_name='post_index.html')
    elif request.method == 'POST':
        data = request.POST
        return HttpResponseRedirect(reverse('posts_detail', kwargs=dict(pk=data['pk'])))


def post_detail(request, *args, **kwargs):
    pk = kwargs.get('pk', None)
    return HttpResponse('Post Page - %s' % pk)


def post_detail_type(request, *args, **kwargs):
    pk = kwargs.get('pk')
    type = kwargs.get('type')

    return HttpResponse('Post Page - %s of Type - %s' % (pk, type))
