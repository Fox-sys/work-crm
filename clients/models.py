from django.db import models


class Client(models.Model):
    name = models.CharField('Имя', max_length=150)
    lastname = models.CharField('Фамилия', max_length=150)
    phone = models.CharField('Телефон', max_length=15, blank=True)
    telegram = models.CharField('Telegram', max_length=100, blank=True)
    vk = models.CharField('Вк', max_length=150, blank=True)
    problem_client = models.BooleanField('Проблемный клиент', default=False)

    def __str__(self):
        return f'{self.lastname} {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
