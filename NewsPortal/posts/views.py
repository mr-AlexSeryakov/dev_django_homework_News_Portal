from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, UpdateView, DeleteView
)
from .forms import (
    ProductForm, SearchForm
)  

from .models import Post
from .filters import ProductFilter
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class PostList(ListView):
    """
    Список всех новостей с постраничной навигацией и фильтрацией

    Использует модель Post и отображает шаблон 'post_list.html'.
    Параметры передаются в фильтр ProductFilter для фильтрации новостей через фильтр (filters)

    Атрибуты:
        model (Post): модель новостей.
        template_name (str): шаблон для рендеринга новостей.
        context_object_name (str): имя контекста для списка новостей
        paginate_by (int): количество новостей на одной странице

    Методы:
        get_queryset (self): возвращает отфильтрованный набор объектов модели Post.
        get_context_data (self): расширяет контекст шаблона дополнительными данными.
    """
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        """
        Переопределяем функции для фильтрации списка товаров.
        
        Метод переопределяет базовый get_queryset, для фильтра ProductFilter
        к исходному queryset модели Post на основе параметров запроса (GET).
        Возвращается уже отфильтрованный queryset для дальнейшего использования в списке.

        Returns:
            Возвращаем из функции отфильтрованный список товаров
        """
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        """
        Добавляtn в контекст объект фильтрации.

        Вызывает базовый метод для получения стандартного контекста,
        затем добавляет в контекст фильтр 'filterset', 
        чтобы передать его в шаблон для отображения фильтрации.

        Args:
            **kwargs: дополнительные аргументы контекста.

        Returns:
            dict: расширенный контекст шаблона с ключом 'filterset'.

        """
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    """
    Отображает отдельно страницу с новостью

    Использует модель Post и шаблон 'post_detail.html' для отображения конкретной новости

    Атрибуты:
        model (Post): Модель новости.
        template_name (str): шаблон для рендеринга отдельной новости.
        context_object_name (str): имя контекста для отдельной новости.
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


# Создать
class NewsCreateView(CreateView):
    model = Post
    form_class = ProductForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.post_type = Post.news  # программно задаем тип
        return super().form_valid(form)

class ArticleCreateView(CreateView):
    model = Post
    form_class = ProductForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.post_type = Post.article  # программно задаем тип
        return super().form_valid(form)
    
# Обновить
class NewsUpdate(UpdateView):
    model = Post
    form_class = ProductForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.post_type = Post.news  
        return super().form_valid(form)
    
class ArticleUpdate(UpdateView):
    model = Post
    form_class = ProductForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.post_type = Post.article
        return super().form_valid(form)
    
# Удалить
class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class NewsSearchView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            date = self.request.GET.get('date')

            if title:
                queryset = queryset.filter(title__icontains=title)
            if author:
                queryset = queryset.filter(author__user__username__icontains=author)
            if date:
                queryset = queryset.filter(created_at__gte=date)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context