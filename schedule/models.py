from django.db import models



class Todo(models.Model):
    text = models.CharField(max_length=40)
    date=models.DateTimeField(auto_now_add=True,auto_now=False,null=True)

    def __str__(self):
        return self.text