from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.restful import fields, marshal_with, marshal
from models import Directory

#field to be allowed
resource_fields = {
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

#arg parser
parser = reqparse.RequestParser()
parser.add_argument('office_name', type=str, location=['form', 'args'])
parser.add_argument('pincode', type=int, location=['form', 'args'])
parser.add_argument('office_type', type=str, location=['form', 'args'])
parser.add_argument('delivery_status', type=str, location=['form', 'args'])
parser.add_argument('division_name', type=str, location=['form', 'args'])
parser.add_argument('region_name', type=str, location=['form', 'args'])
parser.add_argument('circle_name', type=str, location=['form', 'args'])
parser.add_argument('taluk', type=str, location=['form', 'args'])
parser.add_argument('district_name', type=str, location=['form', 'args'])
parser.add_argument('state_name', type=str, location=['form', 'args'])


class DirectoryResource(restful.Resource):
    """
    Resource contains logic for GET and POST.
    """
    
    def get(self):
        args = parser.parse_args()
        input_args = DirectoryView.prepare_query_dict(args)
        print input_args
        if input_args:
            return marshal(list(Directory.objects.filter(**input_args)[:20]), resource_fields)
        else:
            return marshal(list(Directory.objects.all()[:20]), resource_fields)

    marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        print args
        task = Directory.objects.create(**args)
        print task
        return {"office_name": task.office_name}, 201
    
    @staticmethod
    def prepare_query_dict(args):
        input_arg = {}
        for key, value in args.iteritems():
            if value is not None:
                input_arg[key + "__icontains"] = value
                
        return input_arg


class DirectoryUpdateResource(restful.Resource):
    """
    Resource contains logic for PUT and DELETE
    """
    
    def put(self, directory_key):
        args = parser.parse_args()
        input_arg = DirectoryUpdateView.cleanup_none(args)
        Directory.objects.update(write_concern={'pincode':directory_key}, **input_arg)
        return '', 201
    
    def delete(self, directory_key):
        Directory.objects.delete(write_concern={'pincode':directory_key})
        return '', 204
    
    @staticmethod
    def cleanup_none(args):
        input_arg = {}
        
        for key, value in args.iteritems():
            
            if value is not None:
                input_arg[key] = value

        return input_arg