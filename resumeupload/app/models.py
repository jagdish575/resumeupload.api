from django.db import models

# Create your models here.
STATECHOICE =(('Madhypradesh','Madhypradesh'),('Bhihar','Bhihar'))
class Resume (models.Model):
    name = models.CharField(max_length=100) 
    email =models.EmailField()
    dob =models.DateField(auto_now=False,auto_now_add=False)
    state = models.CharField(choices=STATECHOICE,max_length=50)
    gender = models.CharField(max_length=20)
    loaction=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',blank=True)
    docs =models.FileField(upload_to='docs',blank=True)


    def __str__(self):
        return self.name




