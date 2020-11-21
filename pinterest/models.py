from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now

# Create your models here.

class ImageFile(models.Model):
	sno=models.AutoField(primary_key=True)
	title = models.CharField(max_length=50,null=True,blank=True)
	about = models.TextField(max_length=100,null=True,blank=True)
	image = models.ImageField(upload_to='pins/%Y/%m/%d/', max_length=100,default='http://dfoundation.moneylife.in/media/uploads/video_thumbnails/default-image.png')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User,related_name='user_profile',on_delete=models.CASCADE,null=True)



	def __str__(self):
		return self.title

class Comment(models.Model):
	"""docstring for Comment"""
	sno=models.AutoField(primary_key=True)
	comment=models.CharField(max_length=255,null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	pin=models.ForeignKey(ImageFile, on_delete=models.CASCADE)
	# parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
	timestamp= models.DateTimeField(default=now)


	def __str__(self):
		return self.comment 
		 
		