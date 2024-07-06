from django.contrib import admin
from home.models import Registration,ItemInsert,Contact,Checkout,OrderUpdate,Blogpost, Cart


# Register your models here.
admin.site.register(Registration)
admin.site.register(ItemInsert)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(OrderUpdate)
admin.site.register(Blogpost)
admin.site.register(Cart)