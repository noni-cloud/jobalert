from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company}"


class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    location_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    radius_km = models.PositiveIntegerField(default=10, help_text="Alert radius in kilometers")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class JobAlert(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='alerts')
    seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='alerts')
    distance_km = models.FloatField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'seeker')
        ordering = ['-created_at']

    def __str__(self):
        return f"Alert for {self.seeker.name} about {self.job.title} ({self.distance_km:.1f} km)"

