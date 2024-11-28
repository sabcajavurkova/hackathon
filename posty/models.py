from django.db import models

class Report(models.Model):
    username = models.CharField(max_length=25, default='', blank=True)
    address = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0, editable=False)
    dislikes = models.IntegerField(default=0, editable=False)
    
    @property
    def number_of_likes(self):
        return self.likes.count()
    
    @property
    def number_of_dislikes(self):
        return self.dislikes.count()
    
    