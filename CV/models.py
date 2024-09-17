from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    gpa = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    def __str__(self):
        return self.school

class Research(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    tutor = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Internship(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    tutor = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Honor(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Addition(models.Model):
    item = models.CharField(max_length=200)
    def __str__(self):
        return self.item