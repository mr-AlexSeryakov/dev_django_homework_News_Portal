from django import template

register = template.Library()

BAD_WORDS = ['редиска'] # Список плохих слов

@register.filter()
def censor(value):
    """
    Фильтр цензурирует слова которые совподают из списка BAD_WORDS в переданной строке 

    Для каждой слова из BAD_WORDS, заменяет се символы,
    кроме первого символа на символ "*". Первоя буква сохраняется

    Аргументы:
        value (str): исходная строка для проверки

    Возвращает:
        str: строку с цензурированными словами

    Исключения:
        ValueError вызывается если аргумент не является строкой
    
    """
    if not isinstance(value, str):
        raise ValueError("censor filter ожидает строку")
    
    for bad_word in BAD_WORDS:
        replacement = bad_word[0] + '*' * (len(bad_word) - 1)
        # Заменяем как в нижнем регистре, так и с заглавной буквы
        value = value.replace(bad_word, replacement).replace(bad_word.capitalize(), replacement.capitalize())
    return value
