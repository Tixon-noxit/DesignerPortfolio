from django.db import models
from PIL import Image

# Образование

class Education(models.Model):
    periodOfStudy = models.TextField(max_length=1000, blank=True, verbose_name="Период обучения")  # Период обучения
    theNameOfTheInstitution = models.TextField(max_length=1000, blank=True,
                                               verbose_name="Название заведения/курсов")  # Название заведения
    receivedSkills = models.TextField(max_length=1000, blank=True,
                                      verbose_name="Полученные умения")  # Полученные умения
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.theNameOfTheInstitution

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'



# Значки компаний-партнеров (Сотрудничество)

class Partners(models.Model):
    name = models.TextField(max_length=1000, blank=True, verbose_name="Клиент")  # Имя клиента
    Photos = models.ImageField(blank=True, verbose_name="Лого клиента")  # Лого Клиента
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'        