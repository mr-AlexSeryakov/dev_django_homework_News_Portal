from django_filters import FilterSet, CharFilter
from .models import Post

class ProductFilter(FilterSet):
    """
    Фильтр для модели Post по имени автора

    Позволяет фильтровать записи модели Post,
    на совподении имени автора ('author__user__username)

    Атрибуты:
        author_name (CharFilter): фильтр по имени автора с поиском без учета регистра.
    """
    author_name = CharFilter(
        field_name='author__user__username',
        lookup_expr='icontains',
        label = 'Имя автора'
        )
    
    class Meta:
        model = Post
        fields = ['author_name']
