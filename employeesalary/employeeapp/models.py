from django.db import models

class Grade(models.Model):
    position = models.CharField(max_length=20)
    basic_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position

class Employee(models.Model):
    grade_status = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='Grade_fk')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    extra_work_hours = models.PositiveIntegerField(default=0)
    bonus = models.PositiveIntegerField(default=0)
    income_tax = models.PositiveIntegerField(default=0)
    gross_salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.gross_salary = (self.grade_status.basic_salary + (self.extra_work_hours * 25) + self.bonus
                             - ((self.income_tax/100) * self.grade_status.basic_salary))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name