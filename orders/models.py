from django.db import models


class Order(models.Model):
    client = models.ForeignKey('clients.Client', related_name='orders', on_delete=models.PROTECT, verbose_name='Клиент')
    closed = models.BooleanField('Закрыт', default=False)
    title = models.CharField('Название', max_length=300)
    description = models.TextField('Описание', blank=True, max_length=5000)
    start_time = models.DateField('Дата начала заказа', auto_now_add=True)
    deadline = models.DateField('Дедлайн')
    payed = models.BooleanField('Оплачен', default=False)
    status = models.ForeignKey(
        'Status',
        related_name='orders',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Статус'
    )

    def __str__(self):
        return f'{self.client}: {self.title}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class SubTask(models.Model):
    title = models.CharField('Название', max_length=300)
    done = models.BooleanField('Завершено', default=False)
    order = models.ForeignKey('Order', related_name='subtasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'


class Status(models.Model):
    title = models.CharField('Название', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
