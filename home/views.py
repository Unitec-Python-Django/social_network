from builtins import dict

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, RedirectView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseFormView

from messaging.models import Chat, Message
from post.forms import PostUploadForm
from post.models import Post

class A:
    pk = None
    type = None


class HomeIndex(View, TemplateResponseMixin):
    template_name = 'home/photo_home.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.first()
        return self.render_to_response(context={'post': post})


class UploadIndexView(BaseFormView, TemplateResponseMixin):
    form_class = PostUploadForm
    template_name = 'home/photo_upload.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={'form': PostUploadForm()})

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES
        form = PostUploadForm(data=data, files=files)
        if not form.is_valid():
            self.render_to_response(context=self.get_context_data(form=form))
        Post.objects.create(user=request.user, **form.cleaned_data)
        return self.render_to_response(context={})


class ChatIndexView(RedirectView, TemplateResponseMixin):
    pattern_name = 'chat_detail'
    template_name = 'home/photo_chat.html'

    def get(self, request, *args, **kwargs):
        current_chat = Chat.objects.find_all_of(request.user).first()

        if current_chat:
            return super().get(request, current_chat.id)

        chats = []
        current_chat = None
        messages = []
        return self.render_to_response(context={'chats': chats, 'current_chat': current_chat, 'messages': messages})


class ChatDetailView(DetailView, TemplateResponseMixin):
    queryset = Chat.objects.all()

    template_name = 'home/photo_chat.html'

    def get(self, request, pk=None, *args, **kwargs):
        chats = Chat.objects.find_all_of(request.user)
        current_chat = self.get_object()
        messages = Message.objects.filter(chat=current_chat)
        return self.render_to_response(context={'current_chat': current_chat, 'chats': chats, 'messages': messages})


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
