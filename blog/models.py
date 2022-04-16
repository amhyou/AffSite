from django.db import models
from ckeditor.fields import RichTextField


class Topic(models.Model):
	name  = models.CharField(max_length=100)
	descr = models.CharField(max_length=10**3)

	def __str__(self):
		return self.name


class Article(models.Model):
	headline = models.CharField(max_length=100)
	summary  = models.TextField(max_length=10**3)
	content  = RichTextField()
	image    = models.ImageField(upload_to ='staticfiles/')
	subject  = models.ForeignKey(Topic, on_delete=models.CASCADE)

	def __str__(self):
		return self.headline


class MSG(models.Model):
	name = models.CharField(max_length=100)
	mail = models.EmailField(max_length = 254)
	body = models.TextField(max_length=10**4)

	def __str__(self):
		return self.mail

class Aboutme(models.Model):
	name = models.CharField(max_length=100)
	address = models.TextField(max_length = 254)
	email = models.EmailField(max_length = 254)
	job = models.TextField(max_length=100)
	goal = models.TextField(max_length=10**4)

class Banner(models.Model):
	society = models.CharField(max_length=100) 
	code = models.TextField(max_length=10000)