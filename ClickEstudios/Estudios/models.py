from django.db import models

# Create your models here.

class Servicio(models.Model):
      img = models.ImageField(upload_to='media/servicios')
      name = models.CharField(max_length=100)
      date_create = models.DateTimeField(auto_now_add=True)
      active = models.BooleanField(default=True)

      def __str__(self):
            return self.name

class Plan(models.Model):
      servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
      img = models.ImageField(upload_to='media/plan')
      name = models.CharField(max_length=100)
      price = models.IntegerField(default=0)
      date_create = models.DateTimeField(auto_now_add=True)
      active = models.BooleanField(default=True)

      def __str__(self):
            return self.name
      

class PlanAtributos(models.Model):
      plan = models.ForeignKey(Plan, related_name='plan', on_delete=models.CASCADE)
      active = models.BooleanField(default=True)
      name = models.CharField(max_length=100, default='Profesional')

      def __str__(self):
            return self.plan.name
