from django.db import models

# Create your models here.
class ChaiVariety(models.Model):
    
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(auto_now_add=True)
    chai_type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    
    
    def __str__(self):
        return self.name 
    
    
    