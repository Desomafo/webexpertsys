from django.db import models

# Create your models here.

class Tablet(models.Model):
    

    class Meta:
        verbose_name = 'Планшет'
        verbose_name_plural = 'Планшеты'


    manufacturer = models.CharField('Производитель', max_length=30)
    model = models.CharField('Модель', max_length=80, unique=True)
    price = models.FloatField('Цена')
    display_size = models.CharField('Размер экрана', max_length=30)
    display_resolution = models.CharField('Разрешение экрана', max_length=12)
    display_technology = models.CharField('Матрица экрана', max_length=20)
    os_version = models.CharField('Версия ОС', max_length=30)
    cellular = models.CharField('Мобильная связь', max_length=20)
    storage_capacity = models.CharField('Объем внутренней памяти', max_length=10)
    ram_capacity = models.CharField('Объем ОЗУ', max_length=15)
    battery_life = models.CharField('Объем батареи', max_length=10)
    camera = models.CharField('Камера', max_length=40)
    thickness = models.CharField('Толщина устройства', max_length=20)
    weight = models.CharField('Вес', max_length=15)


    def __str__(self):
        return "{} {} {}".format(self.manufacturer, self.model, self.storage_capacity) 

    def get_description(self):
        values = [getattr(self, field.name) for field in self._meta.get_fields()]
        desc = "{}".format(values[0])
        for value in values[1:]:
            desc += ", {}".format(value)
        return desc

class Property(models.Model):

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'

    tablet_property = models.CharField('Свойство', max_length=40)
    property_translation = models.CharField('Перевод', max_length=40)
    number = models.IntegerField('Приоритет', null=True)

    def __str__(self):
        return "{} - {}".format(self.number, self.property_translation)

    def update_properties():
        fields = [[f.name, f.verbose_name] for f in Tablet._meta.get_fields()]
        fields = fields[1:]
        for number, prop in enumerate(fields):
            up_prop = Property.objects.get_or_create(tablet_property=prop[0], property_translation=prop[1])[0]
            up_prop.number = number+1
            up_prop.save()
            print(up_prop.tablet_property, up_prop.number)

