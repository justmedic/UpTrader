from django.db import models
from django.utils.text import slugify
from transliterate import translit


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительский пункт")
    display_on_pages = models.ManyToManyField('MenuDisplayPage', blank=True, verbose_name="Показывать на страницах")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        генерация юрла если не указан через админку
        """
        if not self.url:  
            self.url = slugify(translit(self.name, 'ru', reversed=True))  # транслит нужен если название меню на русском  
        super().save(*args, **kwargs)

class MenuDisplayPage(models.Model):
    url = models.CharField(max_length=255, unique=True, verbose_name="URL страницы")
    
    def __str__(self):
        return self.url
