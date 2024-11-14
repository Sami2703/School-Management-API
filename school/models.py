from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=150)
    teacher = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

