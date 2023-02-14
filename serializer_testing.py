from django.utils import timezone
from rest_framework import serializers

"""
The final way of adding validation is with validator functions.
These are functions that have one argument, the value to validate.
They should raise serializers.ValidationError if an exception occurs, or just do nothing (and not return anything) if the value is valid.
They are useful if you want to apply the same validation to multiple fields
"""

def is_capitalized(value):
    if value[0].lower()==value[0]:
        raise serializers.ValidationError("Value must be capitalized")

class User:
    def __init__(self, username, email=None, first_name=None, last_name=None, password=None, join_date=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.join_date = join_date or timezone.now()
    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=20, required=False,validators=[is_capitalized])
    last_name = serializers.CharField(max_length=20, required=False,validators=[is_capitalized])
    password = serializers.CharField(write_only=True, required=False)
    join_date = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    """
    In order to validate any field of the serializer , we can have methods like validate_<field_name>
    In this case , validating emails of example.com domains only
    """
    def validate_email(self, email):
        email = email.lower()
        domain = email.split("@")[1]
        if domain!="example.com":
            raise serializers.ValidationError("domain must be example.com")
        return email
    """
    In order to validate multiple fields of the serializer , we can have a method names validate
    This is also called object-level-validation
    This is similiar to a clean method on a django form
    As an example, let's make our UserSerializer require a user to supply a first name
    if they provide a last name, and vice versa 
    (i.e. they will need to provide either both names, or neither, but not just one)
    """

    def validate(self,data):
        if (not data.get("first_name")) != (not data.get("last_name")):
            raise serializers.ValidationError("First and Last must be both present or both absent")
        return data

    


user = User("cwilson", "cwilson@example.com", "Callum", password="p4ssw0rd")