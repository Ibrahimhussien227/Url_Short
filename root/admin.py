from django.contrib import admin

from root.models import Url

# Register your models here.

# Register the model that we did in model so we can handle it in the admin page
admin.site.register(Url)
