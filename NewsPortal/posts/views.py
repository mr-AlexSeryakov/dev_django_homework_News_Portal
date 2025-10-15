from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

from .filters import ProductFilter

from .forms import ProductForm

from django.http import HttpResponseRedirect
# Create your views here.

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
    paginate_by = 3

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

def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news/')
        
    return render(request, 'post_edit.html', {'form':form})