from django.db import models

# recipe table
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    branch = models.CharField(max_length=60)

    def __str__(self):
        return self.name