from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field import modelfields

from .managers import CustomUserManager

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField

from .managers import CustomUserManager


class Member(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(_("email address"), unique=True)
    committee = models.ManyToManyField("Committee")
    phonenumbers = models.ManyToManyField("PhoneNumber")
    inside_tanta = models.BooleanField(default=False)
    address= models.CharField(max_length=250, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"


class Event(models.Model):
    eventName = models.CharField(max_length=250, blank=False, null=False)
    images = models.ManyToManyField("Image")
    date_held = models.DateField()
    duration = models.IntegerField(default=1)
    place_held = models.CharField(max_length=250, null=True)
    hosts = models.ManyToManyField("Member", related_name="HostedEvents")
    eventManager = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True, related_name="eventManagerRoles")
    eventViceManager = models.ManyToManyField("Member", related_name="eventViceManagerRoles")
    eventHRLeader = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True, related_name="eventHRLeaderRoles")
    eventPRLeader = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True, related_name="eventPRLeaderRoles")
    eventActivityLeader = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True,
                                            related_name="eventActivityRoles")
    eventFRLeader = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True, related_name="eventFRLeaderRoles")
    eventMediaLeader = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True,
                                         related_name="eventMediaLeaderRoles")
    eventOrganisationLeader = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True,
                                                related_name="eventOrganisationLeaderRoles")

    documents = models.ManyToManyField("Document")
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Committee(models.Model):
    CommitteeName = models.CharField(max_length=3, blank=False, null=False, choices=[
        ("HR", "HR"),
        ("FR", "FR"),
        ("PR", "PR"),
        ("ACT", "Activity"),
        ("MD", "Media"),
        ("MDV", "Media - Videos"),
        ("MDS", "Media - Social & Design"),
        ("MDT", "Media - Twitter"),
        ("MDI", "Media - Instagram"),

    ])

    class Meta:
        verbose_name = "Committee"
        verbose_name_plural = "Committees"

#
class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list

    def __str__(self):
        display_name = self.phone_number
        if display_name:
            return display_name

class Image(models.Model):
    image = models.ImageField(upload_to="eventPics")

class Document(models.Model):
    file = models.FileField(upload_to="files")

    def __str__(self):
        display_name = str(self.file)
        if display_name:
            return display_name