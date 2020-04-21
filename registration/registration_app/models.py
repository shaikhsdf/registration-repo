from django.db import models

class newUser(models.Model):
    fullname = models.CharField(max_length=200)
    usrname = models.CharField(max_length=100, default='0000')
    password = models.CharField(max_length=20)
    email = models.EmailField()
    registeredon = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
