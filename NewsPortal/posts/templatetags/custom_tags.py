from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    Тег, берет текущий параметр запроса и по указанному аргументу заменяет не изменяя параметры

    Функция копирует параметр GET из текущего запроса из контекста шаблона,
    обновляет в них параметры, переданные через kwargs,
    и возвращает новую строку параметров в формате URL-запроса

    Args:
        context (dict): контекст шаблона, содержащий объект request.
        **kwargs: пары ключ-значение параметров, которые нужно добавить или заменить в запросе.

    Returns:
        str: строка URL-кодированных параметров запроса с обновлёнными значениями.

    Пример использования в шаблоне:
        <a href="?{% url_replace page=1 %}">1</a>
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()