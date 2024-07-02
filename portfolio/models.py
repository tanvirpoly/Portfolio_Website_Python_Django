from django.db import models

# Create your models here.
class Social(models.Model):
    name = models.CharField(max_length=20)
    icon_class = models.CharField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return f"{self.name} {self.icon_class}"
    
class Email(models.Model):
    email = models.EmailField()
    def __str__(self):
        return f"{self.email}"
class Phone(models.Model):
    phone_number = models.CharField(max_length=14)
    def __str__(self):
        return f"{self.phone_number}"
class Address(models.Model):
    address = models.CharField(max_length=140)
    def __str__(self):
        return f"{self.address}"
class Skills(models.Model):
    TYPE_CHOICES = (
    ("Technical", "Technical"),
    ("Proffesional", "Proffesional"),
)
    type = models.CharField(max_length=50,choices=TYPE_CHOICES)
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()
    def __str__(self):
        return f"{self.name}" 
class Global(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    email =  models.ManyToManyField(Email)
    phone_number =  models.ManyToManyField(Phone)
    present_address =  models.ManyToManyField(Address)
    image = models.ImageField(default=None,upload_to='profile')
    social_link = models.ManyToManyField(Social)
    def __str__(self):
        return f"{self.name}"
    
class About(models.Model):
    description = models.TextField()
    skills= models.ManyToManyField(Skills)
    file = models.FileField(upload_to="resume/")
    def __str__(self):
        return f"{self.description}" 
