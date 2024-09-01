from django.db import models

# Create your models here.

class AbstractID(models.Model):
    id = models.IntegerField(primary_key = True)

    class Meta:
        abstract = True

class School(AbstractID):
    name = models.CharField(max_length = 250)
    code = models.CharField(max_length = 250)
    address = models.CharField(max_length = 250)

    class Meta:
        db_table = "school"

    def get_id(self):
        return self.id

class Classrooms(AbstractID):
    school_id = models.ForeignKey(School, related_name = 'classroom', on_delete = models.CASCADE)
    class_no = models.IntegerField()
    subclass_no = models.IntegerField()

    class Meta:
        db_table = "classrooms"
    
    def get_id(self):
        return self.id

class Teachers(AbstractID):
    school_id = models.ForeignKey(School, related_name = 'teacher', on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250)
    gender = models.CharField(max_length = 250)
    in_classroom_list = models.ManyToManyField(Classrooms, related_name = 'teacher_in_classroom')

    class Meta:
        db_table = "teachers"
    
    def get_id(self):
        return self.id

class Students(AbstractID):
    school_id = models.ForeignKey(School, on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250)
    gender = models.CharField(max_length = 250)

    class Meta:
        db_table = "students"
    
    def get_id(self):
        return self.id

class Student_list(Students):
    classroom_id = models.ForeignKey(Classrooms, on_delete = models.CASCADE)

    class Meta:
        db_table = "student_list"
