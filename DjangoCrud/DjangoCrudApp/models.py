from djongo import  models


# Create your models here.
class Cricket(models.Model):
    _id=models.ObjectIdField(null=False)
    Cricketer_Name=models.CharField(max_length=50)
    Cricketer_Age=models.IntegerField(max_length=3)
    Cricketer_Team_Name=models.CharField(max_length=255)
    Batsman = models.BooleanField(default=False)
    Bowler = models.BooleanField(default=False)
    No_of_catches = models.CharField(max_length=255, null=True)
    No_of_Matches = models.CharField(max_length=255,null=True)
    Strike_Rate = models.CharField(max_length=255, null=True)
    # image = models.ImageField(upload_to='images', null=True)
    image = models.FileField(db_column='image_url', blank=True, null=True, upload_to='images/')
    user_details=models.JSONField()
    objects= models.DjongoManager()



