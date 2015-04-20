from flask.ext.restful import fields, marshal_with, marshal
from memcache import AppCache, Directory
from parser import ParameterParser


#field to be allowed
resource_fields = {
    'id': fields.String,
    'office_name': fields.String,
    'pincode': fields.Integer,
    'office_type': fields.String,
    'delivery_status': fields.String,
    'division_name': fields.String,
    'region_name': fields.String,
    'circle_name': fields.String,
    'taluk': fields.String,
    'district_name': fields.String,
    'state_name': fields.String 
}


class DirectoryResource(ParameterParser):
    """
    Resource contains logic for GET and POST.
    """
    
    def get(self):
        args = self.parser.parse_args()
        input_args = DirectoryResource.prepare_query_dict(args)
        
        if input_args:
            return marshal(
                list(Directory.objects.filter(**input_args)[:20]),
                resource_fields
            )
        else:
            return marshal(
                list(Directory.objects.all()[:20]),
                resource_fields
            )

    marshal_with(resource_fields)
    def post(self):
        args = self.parser.parse_args()
        task = Directory.objects.create(**args)
        return {"office_name": task.office_name}, 201
    
    @staticmethod
    def prepare_query_dict(args):
        input_arg = {}
        
        for key, value in args.iteritems():
            if value is not None:
                input_arg[key + "__icontains"] = value
                
        return input_arg


class DirectoryUpdateResource(ParameterParser):
    """
    Resource contains logic for PUT and DELETE
    """
    
    def __init__(self):
        ParameterParser.__init__(self)
        self.app_cache = AppCache()
    
    def get(self, directory_key):
        data = self.app_cache.get_data("id", directory_key)
        return marshal(list(data), resource_fields)
    
    def put(self, directory_key):
        args = self.parser.parse_args()
        input_arg = DirectoryUpdateResource.cleanup_none(args)
        
        if input_arg:
            Directory.objects(id=directory_key).update(
                **input_arg
            )
            self.app_cache.delete_data(
                "id", directory_key, clear_from_db=False
            )
        return '', 201
    
    def delete(self, directory_key):
        num_records = self.app_cache.delete_data("id", directory_key)
        return '', 204
    
    @staticmethod
    def cleanup_none(args):
        input_arg = {}
        
        for key, value in args.iteritems():
            
            if value is not None:
                input_arg[key] = value

        return input_arg