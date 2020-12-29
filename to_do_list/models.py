from django.db import models


class Items(models.Model):
    content = models.CharField(max_length=1200)
    status = models.BooleanField(default=False)


# class ListItems(models.Model):
#     id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)