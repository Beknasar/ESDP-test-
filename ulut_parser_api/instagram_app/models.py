from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя пользователя')
    account_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='Код аккаунта')
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Полное имя')
    avatar_url = models.CharField(max_length=200, null=True, blank=True, verbose_name='Аватар url')
    biography = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Биография')

    def __str__(self):
        return f"{self.username}. {self.account_code}"

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class AccountPost(models.Model):
    owner = models.ForeignKey('instagram_app.Account', related_name='account_posts',
                              on_delete=models.CASCADE, verbose_name='Автор поста')
    post_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='Код поста')
    caption = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание поста')

    def __str__(self):
        return f'{self.owner}-{self.post_code}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostMedia(models.Model):
    post_id = models.ForeignKey('instagram_app.AccountPost', related_name='post_medias',
                                on_delete=models.CASCADE, verbose_name='ID поста')
    media_url = models.CharField(max_length=300, null=False, blank=False, verbose_name='Медиа URL')

    def __str__(self):
        return f'{self.pk} - {self.post_id}'

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'