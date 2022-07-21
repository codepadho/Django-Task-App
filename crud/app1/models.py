from django.db import models

# Create your models here.

class Task(models.Model):
    pro = (
        ('High','High priority'),
        ('Medium','Medium priority'),
        ('Low','low priority'),
    )
    id = models.AutoField(unique=True,primary_key=True,editable=False)
    name = models.CharField(unique=True,max_length=200,null=True,blank=True)
    priority = models.CharField(max_length=200,choices=pro)
    discription= models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return str(self.id)
    class Meta:
        ordering = ['id']