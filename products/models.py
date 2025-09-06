from django.db import models

class product(models.Model):
    x =[
        ('general' , 'general'),
        ('Electronics','Electronics'),
        ('clothing','clothing'),
        ('Books','Books'),
    ]
    name = models.CharField(max_length=235, verbose_name='product name')
    description = models.TextField(default='nada', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    img = models.ImageField(upload_to='products/%y/%m/%d',null=True,blank=True)
    category = models.CharField(max_length=100,default='general',choices=x,help_text='select a category for the product')
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-price"]
        

from django.db import models

from django.db import models

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    created_add = models.DateTimeField(null=True)
    
    def __str__(self):
     
        return f"{self.date} {self.time}"
       


    


    


