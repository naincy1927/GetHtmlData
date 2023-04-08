from django.db import models
# OPTIONS = (
#     ('yes','yes'),
#     ('no','no')
# )


# DAYS = (
#     ('Sunday','Sunday'),
#     ('Monday','Monday'),
#     ('Tuesday','Tuesday'),
#     ('Wednesday','Wednesday'),
#     ('Thrusday','Thrusday'),
#     ('Friday','Frinday'),
#     ('Saturday','Saturday')
# )

# ACTIVITY = (
#     ('Feeding drives','Feeding drives'),
#     ('Sterilization process','Sterilization process'), 
#     ('Adoption help','Adoption help'),
#     ('digital awarness','digital awarness'),
#     ('vaccination helping','vaccination helping') 
# )
 

# ALERGY =(
#     ('Dog','Dog'),
#     ('Cat','Cat'),
#     ('Dust','Dust'),
#     ('None','None')
# )

# Create your models here.
class myModel(models.Model):

    

    Name            = models.CharField(max_length= 100 , null = False)
    email           = models.EmailField(max_length=200,null=False)
    phone           = models.CharField(max_length=10, null=False)
    wattsapp        = models.CharField(null=False , max_length=10)
    age             = models.CharField(max_length=100, null=False)
    city            = models.CharField(max_length= 100 , null = False)
    zipCode         = models.CharField(max_length=100 ,null = False)
    contactShare    = models.CharField(max_length= 100 , null = False)#,choices=OPTIONS)
    Allergy         = models.CharField(max_length= 100 , null = False )#, choices=ALERGY)
    daysAttending  = models.CharField(max_length= 100 , null = False)#,choices=DAYS)
    activities     = models.CharField(max_length= 100 , null = False)# choices=ACTIVITY)
    about          = models.TextField(max_length= 100 , null=False ,default="not given")
