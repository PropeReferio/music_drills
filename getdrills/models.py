from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name

    # TODO add harp drills
    # TODO add users/auth for drills by person


class Drill(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.description[:22]}..."
