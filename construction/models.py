from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class ContactInfo(models.Model):
    first_telephone = models.CharField(max_length = 18)
    second_telephone = models.CharField(max_length = 18)
    e_mail_address = models.EmailField()
    maps_address = models.TextField()
    date = models.DateField(auto_now = True, editable = False)
    slug = models.SlugField(blank = True, db_index = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.e_mail_address)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.e_mail_address}"
    
class HeaderIntroduction(models.Model):
    heading = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    background_image = models.CharField(max_length = 50)
    slug = models.SlugField(blank = True, db_index = True)
    isActive = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.heading}"

class AboutUs(models.Model):
    heading = models.CharField(max_length = 60)
    description = models.TextField()
    video = models.CharField(max_length = 50)
    slug = models.SlugField(blank = True, db_index = True)
    isActive = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.heading}"


class Chart(models.Model):
    firstChartNumber = models.CharField(max_length = 10)
    firstChartDescription = models.CharField(max_length = 30)
    
    secondChartNumber = models.CharField(max_length = 10)
    secondChartdescription = models.CharField(max_length = 30)
    
    thirdChartNumber = models.CharField(max_length = 10)
    thirdChartDescription = models.CharField(max_length = 30)
    
    fourthChartNumber = models.CharField(max_length = 10)
    fourthChartDescription = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.firstChartDescription}"


class Services(models.Model):
    heading = models.CharField(max_length = 25)
    description = models.TextField()
    image = models.CharField(max_length = 50)
    isActive = models.BooleanField(default = False)
    slug = models.SlugField(blank = True, db_index = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.heading}"

class Projects(models.Model):
    heading = models.CharField(max_length = 25)
    mini_description = models.CharField(max_length = 25)
    #ck editor code is here
    detail_description = RichTextField(default="")
    image_front = models.CharField(max_length = 50)
    image_back = models.CharField(max_length = 50)
    isActive = models.BooleanField(default = False)
    isMain = models.BooleanField(default = False)
    address = models.TextField(default = "")
    slug = models.SlugField(blank = True, db_index = True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.heading}"
    
class Comments(models.Model):
    name_surname = models.CharField(max_length = 50)
    image = models.CharField(max_length = 50)
    comment = models.TextField()
    isActive = models.BooleanField(default = False)
    score = models.PositiveIntegerField()
    slug = models.SlugField(blank = True, db_index = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_surname)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.name_surname}"
    

class SocialAccount(models.Model):
    faceaccount = models.CharField(max_length = 100)
    instaccount = models.CharField(max_length = 100)
    twitteraccount = models.CharField(max_length = 100)
    linkedinaccount = models.CharField(max_length = 100)
    googlemaps = models.TextField()
    slug = models.SlugField(blank = True, db_index = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.instaccount)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.instaccount}"
    
class contact_info(models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length=40)
    e_mail_address = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now=True, editable=False)
    slug = models.SlugField(blank=True, db_index=True)
    

    def __str__(self):
        return f"{self.first_name} + {self.last_name}"