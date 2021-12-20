from django.contrib import admin
from home.models import Contact, Product,Orders
from home.models import signup
#from home.views import signup

# Register your models here.
admin.site.register(Contact)
admin.site.register(signup)
admin.site.register(Product)
admin.site.register(Orders)
