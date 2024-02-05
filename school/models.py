from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField("Module", related_name="students")

    def __str__(self):
        return self.name


class Module(models.Model):
    module_name = models.CharField(max_length=100)
    module_duration = models.IntegerField()
    class_room = models.IntegerField()

    def __str__(self):
        return self.module_name
