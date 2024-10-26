from django.db import models

# from django.db import models
class TemperatureRecord(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, default='No description')  # Set a default value

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"

