from django.db import models
from django.contrib.auth import get_user_model #Returns the active User model , current logged in user
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

# Create your models here.

User = get_user_model()

class Gender(models.TextChoices):
    """TextChoices is a way to create a group of choices for model fields"""
    MALE = "Male", _("Male") #string representation
    FEMALE = "Female", _("Female") #string representation
    OTHER = "Other", _("Other") #string representation


class Profile(TimeStampedUUIDModel):
    """Inheriting from TimeStampedUUIDModel enables use id and pkid from that class, without defining it again """

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE) #one user to one profile
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+41524204242")
    about_me = models.TextField(verbose_name=_("About me"), default="say something about yourself")
    licence = models.CharField(verbose_name=_("Real Estate License"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="KE", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Nairobi", blank=False ,null=False)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, 
                    help_text= _("Are you looking to Buy a Property?"))
    is_seller = models.BooleanField(verbose_name=_("Seller"), default=False, 
                    help_text= _("Are you looking to sell a Property?"))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, 
                    help_text= _("Are you an agent?"))
    top_agent = models.BooleanField(verbose_name=_("Top agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Number of Reviews"), default=0, null=True, blank=True)


    def __str__(self):
        return f"{self.user.username}'s profile"



