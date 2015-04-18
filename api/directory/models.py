from mongoengine import *


class Directory(Document):
    office_name = StringField(max_length=50, required=True)
    pincode = IntField(required=True)
    office_type = StringField(max_length=50, required=True)
    delivery_status = StringField(max_length=50, required=True)
    division_name = StringField(max_length=50, required=True)
    region_name = StringField(max_length=50, required=True)
    circle_name = StringField(max_length=50, required=True)
    taluk = StringField(max_length=50, required=True)
    district_name = StringField(max_length=50, required=True)
    state_name = StringField(max_length=50, required=True)
    
    def __unicode__(self):
        return self.office_name


#{ "circle_name": "Andhra Pradesh", "delivery_status": "Delivery", "district_name": "Adilabad", "division_name": "Adilabad", "office_name": "Ada B.O", "office_type": "B.O", "pincode": 504293, "region_name": "Hyderabad", "state_name": "ANDHRA PRADESH", "taluk": "Asifabad" } 