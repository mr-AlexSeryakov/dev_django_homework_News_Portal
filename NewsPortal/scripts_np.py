from posts.models import Author, Category, Post, PostCategory, Comment

"""
Блок кода для выполнения задания 8
"""

"""Обновить рейтинг всех пользователей"""
update_rating = Author.objects.all()
for author in update_rating:
    author.update_rating()
    author.save()

"""
Блок кода, для выполнения задания 9

Вывести username и рейтинг лучшего пользователя
(применяя сортировку и возвращая поля первого объекта).
"""

print()
print('<Топовый user и его рейтинг>')
print()
top_author = Author.objects.order_by('-rating').select_related('user').values('user__username', 'rating')[:1]
print(top_author)
print('--')

"""
Блок кода для выполнения 10 задания

Вывести дату добавления, username автора,
рейтинг, заголовок и превью лучшей статьи,
основываясь на лайках/дислайках к этой статье.
"""
print('<Топовая статья по рейтингу с информацией о полльзователе>')
print()
best_post_qs = Post.objects.select_related('author__user').order_by('-rating')[:1]
result = [{
    'title' : post.title,
    'username' : post.author.user.username,
    'created_at': post.created_at.strftime('%d.%m.%Y'),
    'preview' : post.preview(),
    } for post in best_post_qs]
print(result)
print('--')

"""
Блок кода для выполнения 11 задания

Вывести все комментарии (дата, пользователь,
рейтинг, текст) к этой статье.
"""

print('<Все комментарии к топовой статье>')
print()
post = Post.objects.order_by('-rating')[:1] # Получаем пост с нужным названием get(title='Iphone17 sale')
comments = Comment.objects.filter(post=post) # Получаем все комментарии к этому посту
for comment in comments: 
    print('Дата:', comment.created_at.strftime('%d.%m.%Y %H:%M'))
    print('Пользователь:', comment.user.username)
    print('Рейтинг:', comment.rating)
    print('Текст:', comment.text)