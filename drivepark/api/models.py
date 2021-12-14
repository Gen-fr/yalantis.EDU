from django.db import models

# Create your models here.
class Driver(models.Model):
    id = models.AutoField(
        primary_key=True)
    first_name = models.CharField(
        max_length=40,
        null=False,
        blank=False)
    last_name = models.CharField(
        max_length=40,
        null=False,
        blank=False)
    created_at = models.DateField(
        auto_now_add=True,
        # null=False,
        # blank=False
        )
    updated_at = models.DateField(
        auto_now=True,
        # null=False,
        # blank=False
        )

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'Drivers'
            
class Vehicle(models.Model):
    id = models.AutoField(
        primary_key=True)
    driver_id = models.ForeignKey(
        Driver, 
        null=True,
        blank=True,
        default=None,
        #on_delete=models.CASCADE),
        on_delete=models.SET_DEFAULT)
    make = models.CharField(
        max_length=20)
    model = models.CharField(
        max_length=20)
    plate_number = models.CharField(
        max_length=8,
        null=False,
        blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        # null=False,
        # blank=False
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        # null=False,
        # blank=False
        )

    def __str__(self):
        return self.model


    class Meta:
        db_table = 'Vehicles'