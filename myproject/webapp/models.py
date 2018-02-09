from django.db import models


# Create your models here.
class Caselog(models.Model):
    caseid = models.CharField(null=True, blank=True,max_length=200)
    orgnization = models.CharField(null=True, blank=True,max_length=200)
    problem = models.CharField(null=True, blank=True,max_length=200)
    solution = models.TextField(null=True, blank=True)
    # handleby = models.CharField(max_length=100, default='',
    #                             choices=((u'Andy',u'Andy'),(u'David',u'David')))
    MEMBER = (
        ('david','David'),
        ('andy','Andy'),
    )
    handleby = models.CharField(null=True, blank=True, max_length=5, choices=MEMBER)
    date = models.DateField(null=True)
    def __str__(self):
        return self.caseid
