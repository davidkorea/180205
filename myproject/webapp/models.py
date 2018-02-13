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


class Comment(models.Model):
    name = models.CharField(null=True, blank=True,max_length=20)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Caselog, related_name='under_comments',
                                  null=True, blank=True, on_delete=models.CASCADE)
    best_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.comment