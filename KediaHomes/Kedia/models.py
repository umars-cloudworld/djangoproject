from django.db import models
from django.db.models.aggregates import Max
from accounts.models import User


class OurProjects(models.Model):
    image = models.FileField(upload_to='Projects/')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=65500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='contact_us_user', blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    message = models.TextField(max_length=65500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class NewsLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='news_letter_user', blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class Projects(models.Model):
    type = models.CharField(max_length=255, choices=[('Villa', 'Villa'), ('Apartment', 'Apartment'), ('Plots', 'Plots')])
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class Pricing(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="projects_details",  blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=65500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class Map(models.Model):
    plot_no = models.CharField(max_length=10, unique=True)
    Coordinate = models.CharField(max_length=100)
    plot_size = models.CharField(max_length=100, blank=True, null=True)
    direction = models.CharField(max_length=250, blank=True, null=True)
    dimension = models.CharField(max_length=250, blank=True, null=True)
    plc = models.BooleanField(default=False)
    plan_choices = [('2D', '2D'), ('3D', '3D')]
    plan = models.CharField(max_length=255, choices=plan_choices, default='2D')
    floor = models.CharField(max_length=250, blank=True, null=True)
    elevation = models.CharField(max_length=250, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_user')
    plot = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='booking_plot')
    booking_no = models.CharField(max_length=250, unique=True)
    booking_amount = models.FloatField(default=50000.00)
    txn_id = models.CharField(max_length=250, blank=True, null=True)
    txn_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Booking_new(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    dob = models.DateField()
    pan = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    plot_no = models.CharField(max_length=30,  default='NA')

    def register(self):
        self.save()

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('KEDIAHOMES%Y%m%dODR')
        return super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    img_src = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    def register(self):
        self.save()