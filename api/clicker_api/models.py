from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField('Логин', max_length=32, unique=True)
    password = models.CharField('Пароль', max_length=16)
    score = models.FloatField('Очки', default=0)
    
    def __str__(self):
        return self.login
    
    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'


class Name(models.Model):
    name = models.CharField('Имя', max_length=32)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'имя'
        verbose_name_plural = 'Имена'


class Kind(models.Model):
    name = models.CharField('Название', max_length=32)
    life_duration = models.IntegerField('Продолжительность жизни (в годах)')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'вид'
        verbose_name_plural = 'Виды'
  
    
class Animal(models.Model):
    name = models.ForeignKey(Name, models.PROTECT, verbose_name='Имя')
    age = models.IntegerField('Возраст', default=0)
    kind = models.ForeignKey(Kind, models.PROTECT, verbose_name='Вид')
    user = models.ForeignKey(User, models.PROTECT, verbose_name='Владелец')
    
    def __str__(self):
        return f"{self.kind} {self.name}"
    
    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = 'Животные'
    