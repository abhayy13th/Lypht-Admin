from django.db import models


# Create your models here.
class Tag(models.Model):
    Categories = (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food'),
        ('Beauty', 'Beauty'),
        ('Sports', 'Sports'),
        ('Books', 'Books'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=200, null=True, choices=Categories)

    def __str__(self):
        return self.name


class Sos(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    rider_name = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    discount = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name


class UserTag(models.Model):
    UserCategories = (
        ('Rider', 'Rider'),
        ('Passenger', 'Passenger'),
    )

    usertype = models.CharField(max_length=200, null=True, choices=UserCategories)

    def __str__(self):
        return self.usertype


class Rider(models.Model):
    rider_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    newRideStatus = models.CharField(max_length=200, null=True)
    points = models.IntegerField(null=True)
    type = models.ForeignKey(UserTag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BikeDetails(models.Model):
    bike_number = models.CharField(max_length=200, null=True)
    bike_model = models.CharField(max_length=200, null=True)
    bike_color = models.CharField(max_length=200, null=True)
    rider_id = models.ForeignKey(Rider, on_delete=models.CASCADE)

    def __str__(self):
        return self.bike_number


class Passenger(models.Model):
    passenger_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    points = models.IntegerField(null=True)
    type = models.ForeignKey(UserTag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RideRequests(models.Model):
    ride_request_id = models.CharField(max_length=200, null=True)
    created_at = models.CharField(max_length=200, null=True)
    rider_id = models.ForeignKey(Rider, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True)
    points = models.IntegerField(null=True)
    originAddress = models.CharField(max_length=200, null=True)
    destinationAddress = models.CharField(max_length=200, null=True)
    originLat = models.FloatField(null=True)
    originLng = models.FloatField(null=True)
    destinationLat = models.FloatField(null=True)
    destinationLng = models.FloatField(null=True)
    distance = models.FloatField(null=True)
    duration = models.FloatField(null=True)
    passenger_name = models.CharField(max_length=200, null=True)
    passenger_phone = models.CharField(max_length=200, null=True)
    rider_name = models.CharField(max_length=200, null=True)
    rider_phone = models.CharField(max_length=200, null=True)
    rider_bike_number = models.CharField(max_length=200, null=True)
    rider_bike_model = models.CharField(max_length=200, null=True)
    rider_bike_color = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.ride_request_id
