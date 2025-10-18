from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        """Обновляет рейтинг текущего автора"""
        # суммарный рейтинг каждой статьи автора умножается на 3
        article_rating = self.post_set.aggregate(total=Sum('rating'))['total'] or 0
        # суммарный рейтинг всех комментариев автора
        comment_rating = self.user.comment_set.aggregate(total=Sum('rating'))['total']
        # суммарный рейтинг всех комментариев к статьям автора
        post_comment_rating = 0
        for post in self.post_set.all():
            post_comment_rating += post.comments.aggregate(total=Sum('rating'))['total'] or 0
        
        self.rating = article_rating * 3 + comment_rating + post_comment_rating
        self.save()

    def __str__(self):
        return self.user.username.title()

class Category(models.Model):
    sport = 'Sport'
    it_industry = 'IT'
    games = 'Games'
    russian_extreme = 'RusExt'
    development = 'Dev'

    CATEGORYES = [
        (sport, 'Спорт'),
        (it_industry, 'it-индустрия'),
        (games, 'игры'),
        (russian_extreme, 'Русский экстрим'),
        (development, 'Развитие')
    ]
    category_name = models.CharField(max_length=20,
                                     choices=CATEGORYES,
                                     unique= True)
    
    def __str__(self):
        return self.category_name.title()

class Post(models.Model):
    article = 'AR'
    news = 'NW'

    POST_TYPES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey('Author', on_delete=models.CASCADE) # связь «один ко многим» с моделью Author
    post_type = models.CharField(max_length=2, choices=POST_TYPES) # поле с выбором — «статья» или «новость»
    created_at = models.DateTimeField(auto_now_add=True) # автоматически добавляемая дата и время создания
    categories = models.ManyToManyField('Category') # связь «многие ко многим» с моделью Category
    title = models.CharField(max_length=255) # заголовок статьи/новости
    text = models.TextField() # текст статьи/новости
    rating = models.IntegerField(default=0) # рейтинг статьи/новости.

    def like(self):
        """like() увеличивают рейтинг на единицу."""
        self.rating += 1
        self.save()

    def dislike(self):
        """dislike() уменьшают рейтинг на единицу."""
        self.rating -= 1
        self.save()   

    def preview(self):
        """Возвращает начало статьи (предварительный просмотр) 
        длиной 124 символа и добавляет многоточие в конце"""
        return self.text[:124] + '...'
    
    def __str__(self):
        return self.title.title()
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class PostCategory(models.Model):
    """Таблица многих ко многим"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # связь «один ко многим» с моделью Post
    category = models.ForeignKey('Category', on_delete=models.CASCADE) # связь «один ко многим» с моделью Category

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments') # связь «один ко многим» с моделью Pos
    user = models.ForeignKey(User, on_delete=models.CASCADE) # связь «один ко многим» со встроенной моделью User
    text = models.TextField() # текст комментария
    created_at = models.DateTimeField(auto_now_add=True) # дата и время создания комментария
    rating = models.IntegerField(default=0) # рейтинг комментария

    def like(self):
        """like() увеличивают рейтинг на единицу."""
        self.rating += 1
        self.save()

    def dislike(self):
        """dislike() уменьшают рейтинг на единицу."""
        self.rating -= 1
        self.save()