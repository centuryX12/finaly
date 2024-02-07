from django.db import models

class Information(models.Model):
    info_about = models.TextField(blank=True, null=True, verbose_name='содержание')



    class Meta:
        db_table = 'Information'
        verbose_name = 'Описание приложения'
        verbose_name_plural = 'описании приложения'
