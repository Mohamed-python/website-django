from django.contrib import admin



from .models import Job ,Category
# Register your models here.

# اظهار الحقل في الادمن
admin.site.register(Job)
admin.site.register(Category)