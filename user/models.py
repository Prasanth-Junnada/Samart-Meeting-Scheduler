from django.db import models

# Create your models here.


class User1(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    otp = models.IntegerField(null=True)
    mobile = models.TextField(max_length=10,null=True)
    verify = models.CharField(default='no',max_length=100)


class avail(models.Model):
    user = models.ForeignKey(User1, on_delete=models.CASCADE)
    mon = models.CharField(max_length=500,null=True)
    tue = models.CharField(max_length=500,null=True)
    wed = models.CharField(max_length=500,null=True)
    thr = models.CharField(max_length=500,null=True)
    fri = models.CharField(max_length=500,null=True)
    sat = models.CharField(max_length=500,null=True)
    sun = models.CharField(max_length=500,null=True)
    sun_start = models.TextField(null=True)
    sun_end = models.TextField(null=True)
    mon_start = models.TextField(null=True)
    mon_end = models.TextField(null=True)
    tue_start = models.TextField(null=True)
    tue_end = models.TextField(null=True)
    wed_start = models.TextField(null=True)
    wed_end = models.TextField(null=True)
    thu_start = models.TextField(null=True)
    thu_end = models.TextField(null=True)
    fri_start = models.TextField(null=True)
    fri_end = models.TextField(null=True)
    sat_start = models.TextField(null=True)
    sat_end = models.TextField(null=True)



class Meeting(models.Model):
    user = models.ForeignKey(User1, on_delete=models.CASCADE)
    creator_user_id = models.IntegerField(null=True)  # New field to store the creator's user ID
    name = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1000, null=True)
    desc = models.TextField()
    mail = models.EmailField(null=True)
    duration = models.CharField(max_length=1000, null=True)
    time = models.TextField(max_length=1000, null=True)
    day = models.TextField(max_length=1000, null=True)



