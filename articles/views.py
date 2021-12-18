from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Articles

class ListViewPage(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'article_list.html'

class DetailViewPage(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'article_detail.html'

class CreateViewPage(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articles
    fields = ('title', 'summary', 'text', 'photo',)
    template_name = 'article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class UpdateViewPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ('title', 'summary', 'text', 'photo',)
    template_name = 'article_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeleteViewPage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# Create your views here.
