from django.db import models

# Create your models here.
class Emp(models.Model):
    Empno=models.IntegerField(5)
    Ename=models.CharField(max_length=30,primary_key=True)
    Job=models.CharField(max_length=30,null=False)
    Mgr=models.IntegerField(5)
    Hiredate=models.DateField()
    Sal=models.IntegerField(6)
    Comm=models.IntegerField(5)
    Deptno=models.IntegerField(5)

    def __str__(self):
        return self.Ename



class Dept(models.Model):
    Deptno=models.ForeignKey(Emp,on_delete=models.CASCADE)
    Dname=models.CharField(max_length=50)
    Loc=models.CharField(max_length=50)

    def __str__(self):
        return self.Dname

