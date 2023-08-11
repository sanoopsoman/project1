from django.db import models


# Create your models here.
class tbl_staff(models.Model):
    emp_id = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    des = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.CharField(max_length=30)
    phone = models.IntegerField()

    class meta:
        tbl_data = "tbl_staff"


class tbl_accounts(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    desig = models.CharField(max_length=20)
    salary = models.IntegerField()
    branch = models.CharField(max_length=30)
    place = models.CharField(max_length=20)

    class meta:
        data_tbl = "tbl_accounts"


class tbl_person(models.Model):
    emp_name = models.CharField(max_length=20)
    salary = models.IntegerField()
    pf = models.IntegerField()
    address = models.CharField(max_length=70)
    exp = models.IntegerField()
    status = models.CharField(max_length=20)

    class meta:
        tbl_per = "tbl_person"


class tbl_flower(models.Model):
    name = models.CharField(max_length=25)
    img = models.CharField(max_length=500)
    price = models.IntegerField()

    class meta:
        tbl_flr = "tbl_flower"
