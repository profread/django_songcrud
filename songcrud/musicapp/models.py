from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    album = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}"


class Lyrics(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        if len(self.content) > 100:
            return f"{self.content[:100]}..."
        else:
            return f"{self.content}"
        