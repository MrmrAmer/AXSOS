from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not postData['title']:          
            errors["missing_field_title"] = "Please Enter Title Name."
        elif len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if not postData['network']:          
            errors["missing_field_network"] = "Please Enter Network Name."        
        elif len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        desc = postData['desc'].strip()
        if 0 < len(desc) < 10:
            errors["desc"] = "Description should be at least 10 characters"
            
        release_date_str = postData.get('date', '').strip()

        if not release_date_str:
            errors['release_date'] = "Release date is required."
        else:
            release_date_obj = date.fromisoformat(release_date_str)
            if release_date_obj >= date.today():
                errors['release_date'] = "Release date must be in the past."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()