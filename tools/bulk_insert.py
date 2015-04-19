import sys
import csv
from pymongo import MongoClient

try:
    file_path = sys.argv[1]
except:
    print "Please specify file path"

client = MongoClient('localhost', 27017)
db = client['app_directory']
directory = db.directory

query_list = []

with open(file_path) as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        try:
            query_list.append({
                'taluk': unicode(row['Taluk']), 'state_name': unicode(row['statename']),
                'office_name': unicode(row['officename']), 'division_name': unicode(row['divisionname']),
                'pincode': int(row['pincode']), 'circle_name': unicode(row['circlename']),
                'delivery_status': unicode(row['Deliverystatus']), 'office_type': unicode(row['officeType']),
                'district_name': unicode(row['Districtname']), 'region_name': unicode(row['regionname'])
            })
        except UnicodeDecodeError:
            continue
        
        if len(query_list) == 1000:
            print query_list
            directory.insert(query_list)
            del query_list
            query_list = []
            print query_list
        
    if query_list:
        directory.insert(query_list)