from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)



class Products(models.Model):
    RATING_CHOICE=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    name= models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    price=models.DecimalField(max_digits=20, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE )
    expired_date= models.DateField()
    production_date= models.DateField()
    img= models.ImageField(upload_to='products')
    discount_price=models.DecimalField(max_digits=20, decimal_places=2)
    rating = models.IntegerField(choices=RATING_CHOICE)

    def __str__(self):
        return self.name
