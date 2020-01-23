from builtins import dict

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateResponseMixin


class A:
    pk = None
    type = None


class HomeIndex(View, TemplateResponseMixin):
    template_name = 'home/photo_base.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(None)


class PostIndexView(View, TemplateResponseMixin):
    template_name = 'home/post_index.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context=None)

    def post(self, request, *args, **kwargs):
        data = request.POST
        return HttpResponseRedirect(reverse('posts_detail', kwargs=dict(pk=data['pk'])))

    def delete(self, request, *args, **kwargs):
        data = request.POST
        return HttpResponseRedirect(reverse('posts_detail', kwargs=dict(pk=data['pk'])))


class PostDetailView(View, TemplateResponseMixin):
    template_name = 'home/post_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        types = [
            'new',
            'old',
        ]
        return self.render_to_response(context={'pk': pk, 'types': types})


class PostDetailTypeView(View, TemplateResponseMixin):
    template_name = 'home/post_detail_type.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = kwargs.get('type')
        template = get_template(self.template_name)
        date = timezone.now()
        data = dict(data=dict(type=type, pk=pk, d=date))

        s = template.render(context=data)
        return HttpResponse(s)

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
