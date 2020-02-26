from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    posted_by =  models.CharField(max_length=100, null=True)
    count = models.CharField(max_length=100)
    police = models.CharField(max_length=100)
    police_department_address = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    health_department_address = models.CharField(max_length=100)


    def __str__(self):
        return f' {self.name} Neighborhood'


    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
                   
    @classmethod
    def find_neighborhood_by_id(cls,id):
        neighborhood_result = cls.objects.get(id=id)
        return neighborhood_result
 
    @classmethod
    def update_occupants(cls,current_value,new_value):
        fetched_object = cls.objects.filter(count=current_value).update(count=new_value)
        return fetched_object

    @classmethod
    def update_neighborhood(cls,current_value,new_value):
        fetched_object = cls.objects.filter(count=current_value).update(count=new_value)
        return fetched_object


    @classmethod
    def retrieve_all(cls):
        all_objects = Neighborhood.objects.all()
        for item in all_objects:
            return item

class Business(models.Model):
    business_name = models.CharField(max_length=100, unique= True)
    business_user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_neighborhood = models.ForeignKey(Neighborhood, null=True)
    business_email = models.EmailField(max_length=100, unique= True) 
    
    
    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    
    @classmethod              
    def find_business_by_id(cls,id):
        business_result = cls.objects.get(id=id)
        return business_result

    
    @classmethod
    def update_business(cls,current_value,new_value):
        fetched_object = cls.objects.filter(business_name=current_value).update(business_name=new_value)
        return fetched_object


    def search_by_business(cls,search_term):
        search_result = cls.objects.filter(business_name__icontains=search_term)
        return search_result   