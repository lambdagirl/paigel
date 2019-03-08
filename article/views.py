from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy,reverse
from .models import Article, Images
from django.shortcuts import get_object_or_404, render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ArticleForm, ImageFormSet
from django.db import transaction


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    def get_queryset(self):
        return Article.objects.active

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = kwargs["object"]
        context['images'] = Images.objects.filter(article__title = article)
        return context

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    #form_class = ImageFormSet
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_new.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['article_form'] = ArticleForm(self.request.POST)
            context['formset'] = ImageFormSet(self.request.POST,
                                              self.request.FILES,
                                              queryset=Images.objects.none())
        else:
            context['article_form'] = ArticleForm()
            context['formset'] = ImageFormSet(queryset=Images.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        article_form = context['article_form']
        formset = context['formset']
        if article_form.is_valid() and formset.is_valid():
            article_form = article_form.save(commit=False)
            article_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(article=article_form, image=image)
                    photo.save()
            return redirect(article_form.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
'''

def post(request):
    if request.method == 'POST':

        articleForm = ArticleForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if articleForm.is_valid() and formset.is_valid():
            article_form = articleForm.save(commit=False)
            article_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(article=article_form, image=image)
                    photo.save()
            return HttpResponseRedirect("/")
        else:
            print(articleForm.errors, formset.errors)
    else:
        articleForm = ArticleForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'article_new.html',
                  {'articleForm': articleForm, 'formset': formset})
                  '''
