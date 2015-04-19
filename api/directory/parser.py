from flask.ext.restful import reqparse


class ParameterParser(object):
    """
    Allowed parameter in request argument
    """
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('office_name', type=str, location=['form', 'args'])
        self.parser.add_argument('pincode', type=int, location=['form', 'args'])
        self.parser.add_argument('office_type', type=str, location=['form', 'args'])
        self.parser.add_argument('delivery_status', type=str, location=['form', 'args'])
        self.parser.add_argument('division_name', type=str, location=['form', 'args'])
        self.parser.add_argument('region_name', type=str, location=['form', 'args'])
        self.parser.add_argument('circle_name', type=str, location=['form', 'args'])
        self.parser.add_argument('taluk', type=str, location=['form', 'args'])
        self.parser.add_argument('district_name', type=str, location=['form', 'args'])
        self.parser.add_argument('state_name', type=str, location=['form', 'args'])
