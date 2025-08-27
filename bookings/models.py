from django.db import models

# Create your models here.

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    package_id = models.ForeignKey('TravelPackage', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    travel_mode = models.CharField(max_length=50)
    no_of_seats= models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking to {self.destination} by {self.user.username}"
    
class TravelPackage(models.Model):
    package_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # travel_type = models.CharField(max_length=50) #air water land
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    seats_available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name