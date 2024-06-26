from django.db import models

# Create your models here.

class Meeting(models.Model):
    subject = models.CharField(max_length=100, verbose_name="Toplantı Konusu")
    date = models.DateField(verbose_name="Tarih")
    start_time = models.TimeField(verbose_name="Başlangıç Saati")
    end_time = models.TimeField(verbose_name="Bitiş Saati")
    participants = models.TextField(verbose_name="Katılımcılar")

    def __str__(self):
        return self.subject