from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField()
    foto = models.ImageField(blank=True)
    marks = models.PositiveSmallIntegerField()
    count = models.IntegerField(default=0)
    subcategory = models.ForeignKey("Subcategory", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}    {self.subcategory}'


class Reviews(models.Model):
    CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    mark = models.PositiveSmallIntegerField(choices=CHOICES, default=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.text} {self.user} {self.product}"


class Category(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Subcategory(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Stocks(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Basket(models.Model):
    product = models.CharField(max_length=128, blank=True)
    count = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user}{self.product}{self.price}{self.count}"


class Feedback(models.Model):
    email_sender = models.EmailField()
    topic = models.CharField(max_length=64)
    email_recipient = models.EmailField(default="marketstuffdjango@gmail.com")
    text_message = models.TextField()

    def __str__(self):
        return f"{self.email_sender}{self.topic}{self.email_recipient}{self.text_message}{self.phone_number}"


class CustomUser(models.Model):
    user_for_city = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}"
