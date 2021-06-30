from django.db import models

# Test Model for saving the data in the database

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    first_question = models.CharField(max_length=100,null=True)
    first_answers = models.CharField(max_length=100,null=True)
    second_question = models.CharField(max_length=100,null=True)
    second_answers = models.CharField(max_length=100,null=True)
    datetime = models.DateTimeField(auto_now_add=True,max_length=100,null=True)

    def __str__(self):
        return str(self.name)