from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_id = models.CharField(max_length=4, unique = True)
    subject = models.CharField(max_length=150, unique = True)

    def __unicode__(self):
        return u'%s,%s'%(self.subject_id, self.subject)

class StudentDep(models.Model):
    CHOICE = (
        (u'CSE',u'Computer Science And Engineering'),
        (u'ECE',u'Electronics And Communication'),
        (u'ME',u'Mechanical Engineering'),
        (u'CHE',u'Chemical Engineering'),
        )
    branch = models.CharField(max_length=150, choices=CHOICE, unique = True)
    subjects =models.ManyToManyField(Subject)
    
    def __unicode__(self):
        return self.branch

class Student(models.Model):
    student_id = models.CharField(max_length=6, primary_key = True)
    student_name = models.CharField(max_length=100)
    student_dep = models.ForeignKey(StudentDep)
    
    def __unicode__(self):
        return self.student_name

class Exam(models.Model):
    CHOSE = (
        (u'100'),
        (u'50'),
        )
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    student_dep = models.ForeignKey(StudentDep)
    maximum_marks = models.CharField(max_length=100)
    marks_obtained = models.IntegerField()