from django.db import models



class Post(models.Model):
	"""docstring for Posts"""
	text = models.TextField()


	def __str__(self):
		return self.text[:50]
		
