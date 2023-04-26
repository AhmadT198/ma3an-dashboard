from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


class MemberAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Member
    list_display = ("full_name", "inside_tanta", "is_active",)
    list_filter = ("full_name", "email", "committee", "inside_tanta")
    fieldsets = (
        (None, {"fields": ("full_name", "email", "address", "inside_tanta", "committee", "phonenumbers")}),
    )

    add_fieldsets = (
        ("Personal Info", {
            "classes": ("wide",),
            "fields": (
                "full_name", "email", "address", "inside_tanta", "password1", "password2", "phonenumbers")}
         ),
        ("Inside Ma'an", {
            "classes": ("wide",),
            "fields": (
                "committee",)}
         ),
    )
    search_fields = ("email", "full_name",)
    ordering = ("email", "full_name", "inside_tanta")


admin.site.register(Member, MemberAdmin)
admin.site.register(Event)
admin.site.register(Committee)
admin.site.register(PhoneNumber)
admin.site.register(Image)
admin.site.register(Document)



