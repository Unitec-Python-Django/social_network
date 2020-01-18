from django.db import models


class User(models.Model):

    USER_GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(choices=USER_GENDER, max_length=10)
    photo = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    jobs = models.ManyToManyField('home.WorkPlace', related_name='users')

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=55, null=True)
    address = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=15)
    ceo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    ssn = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    portfolio_url = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
