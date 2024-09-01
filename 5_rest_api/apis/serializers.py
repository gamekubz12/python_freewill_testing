from .models import School, Classrooms, Teachers, Students, Student_list
from rest_framework import serializers

# code here
class ClassroomSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Classrooms
        fields = ["id", "school_id", "class_no", "subclass_no"]

    def get_id(self, obj):
        return obj.get_id()

class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only = True)
    classroom = ClassroomSerializer(many = True, read_only = True)
    class Meta:
        model = School
        fields = ["id", "name", "code", "address", "classroom"]

    def get_id(self, obj):
        return obj.get_id()

class TeacherSerializer(serializers.ModelField):
    id = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Teachers
        fields = ["id", "school_id", "firstname", "lastname", "gender"]

    def get_id(self, obj):
        return obj.get_id()

class StudentSerializer(serializers.ModelField):
    id = serializers.SerializerMethodField(read_only = True)
    # classroom = Student_list.objects.filter()
    class Meta:
        model = Students
        fields = ["id", "school_id", "firstname", "lastname", "gender"]

    def get_id(self, obj):
        return obj.get_id()
