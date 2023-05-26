from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Rider)
admin.site.register(Passenger)
admin.site.register(RideRequests)
admin.site.register(UserTag)
admin.site.register(BikeDetails)
admin.site.register(Sos)
admin.site.register(OrderPassenger)
admin.site.register(OrderRider)
