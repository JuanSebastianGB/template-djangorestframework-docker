from django.db import models


# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
    order = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
