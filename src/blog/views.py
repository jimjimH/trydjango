from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from .forms import ArticleModelForm

from .models import Article
class ArticleObjectMixin(object):
    model = Article
    
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Article, id=id)
        return obj

class ArticleDeleteView_1(ArticleObjectMixin, View):
    template_name = 'article_delete.html'
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('/blog/')
        return render(request, self.template_name, context)


class ArticleUpdateView_1(ArticleObjectMixin, View):
    template_name = 'article_update.html' 
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = ArticleModelForm(instance=obj)
            context = {'form': form, 'object': obj}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            form = ArticleModelForm(request.POST, instance=obj)
            context = {'form': form, 'object': obj}
            if form.is_valid():
                form.save()
                form = ArticleModelForm()
        return render(request, self.template_name, context)

class ArticleCreateView_1(View):
    template_name = 'article_create.html'
    def get(self, request, *args, **kwargs):
        form = ArticleModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ArticleModelForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            form = ArticleModelForm()
        return render(request, self.template_name, context)

class ArticleDetailView_1(ArticleObjectMixin, View):
    template_name = 'article_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

class ArticleListView_1(View):
    template_name = 'article_list.html'
    queryset = Article.objects.all()
    def get(self, request, *args, **kwargs):
        context = {'object_list': self.queryset}
        return render(request, self.template_name, context)

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm


class ArticleListView(ListView):
    template_name = 'article_list.html'  # assign a custom template
    queryset = Article.objects.all()  # default template: blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # override def get_object(): replace pk by id
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    # override def get_object(): replace pk by id
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    queryset = Article.objects.all()
    # success_url = '/'
    # override def get_object(): replace pk by id
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article_list')


def article_create_view(request):
    form = ArticleModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleModelForm()

    context = {
        'form': form
    }
    return render(request, "article_create.html", context)


def article_update_view(request, id):
    obj = get_object_or_404(Article, id=id)
    form = ArticleModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "article_create.html", context)


def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("article_list.html")
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)


def article_list_view(request):
    queryset = Article.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "article_list.html", context)


def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        "object": obj
    }
    return render(request, "article_detail.html", context)
