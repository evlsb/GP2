from django.db import models


class Sensor(models.Model):
    position = models.CharField('Позиция', max_length=50)
    description = models.CharField('Описание', max_length=250)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    units = models.ForeignKey('EngUnits', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}/catupdate'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class EngUnits(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}/engupdate'

    class Meta:
        verbose_name = 'Ед. изм.'
        verbose_name_plural = 'Ед. изм.'