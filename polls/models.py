from django.db import models


class QR(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    sampled_by = models.CharField(max_length=250, verbose_name='Sampled by')
    unit = models.CharField(max_length=250, verbose_name='Unit')
    sample_point = models.CharField(max_length=250, verbose_name='Sample Point')
    sample_type = models.CharField(max_length=250, verbose_name='Sample Type')
    data_time = models.DateTimeField(auto_now=False, auto_now_add=False,  verbose_name='Date Time')
    hashing_name = models.CharField(max_length=250, verbose_name='Hash Name')
    
    #class Meta:
        #abstract = True

    def __str__(self):
        return self.hashing_name
    


class Barcode(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    sampled_by = models.CharField(max_length=250, verbose_name='Sampled by')
    unit = models.CharField(max_length=250, verbose_name='Unit')
    sample_point = models.CharField(max_length=250, verbose_name='Sample Point')
    sample_type = models.CharField(max_length=250, verbose_name='Sample Type')
    data_time = models.DateTimeField(auto_now=False, auto_now_add=False,  verbose_name='Date Time')
    hashing_name = models.CharField(max_length=250, verbose_name='Hash Name')
    
    #class Meta:
        #abstract = True

    def __str__(self):
        return self.hashing_name
