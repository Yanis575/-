from django.db import models


class Questions(models.Model):
    questions = models.CharField(max_length=256, verbose_name='Вопрос')
    answer = models.CharField(max_length=256, verbose_name= 'Ответ', blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name= 'Категория')
    correct = models.CharField(max_length=256,
                               verbose_name= 'Правильный ответ', default=' ')
    describe = models.TextField(verbose_name= 'Развернутый ответ', blank=True)
    picture = models.ImageField('Фотография', upload_to='questions',
                                blank=True)


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('questions',)

    def __str__(self):
        return self.questions[:40]

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Название категории')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name