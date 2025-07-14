from django.contrib import admin
from .models import Customer



class AdminCustomer(admin.ModelAdmin):

    list_display = ('id', 'name', 'phone', 'email', 'address', 'created_at')

    list_filter = ('phone', 'email')

    ordering = ('id', )

    def save_model(self, request, obj, form, change):
        obj._allow_save = True  # 💡 admin panel orqali kiritishga ruxsat
        super().save_model(request, obj, form, change)


admin.site.register(Customer, AdminCustomer)



##### admin
### 12345