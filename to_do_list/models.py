from django.db import models


class Items(models.Model):
    task_name = models.CharField(max_length=120)
    task_description = models.CharField(max_length=1200)
    dt_start = models.DateField()
    dt_end = models.DateField()
    emai = models.EmailField()  # no futuro pode ser o email do user que está criando


class ListItems(models.Model):
    status = models.BooleanField(default=False)
    item_fk = models.ForeignKey(Items, on_delete=models.CASCADE)
    # id_user = models.ForeignKey('auth.User',on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20)


class ListCategory(models.Model):
    category_fk = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_fk = models.ForeignKey(Items, on_delete=models.CASCADE)