from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'country', 'avatar')

@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid_course', 'paid_lesson', 'amount', 'payment_method')
