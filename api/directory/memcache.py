from werkzeug.contrib.cache import MemcachedCache
from models import Directory


class AppCache(MemcachedCache):
    """
    Class to be used for memcached interaction.
    """
    
    def __init__(self):
        MemcachedCache.__init__(self, servers=['127.0.0.1:11211'])
        
    def get_data(self, parent_key, sub_key):
        key = "%s__%s" % (parent_key, sub_key)
        data = self.get(key)
        
        if not data:
            query = {"pincode": sub_key}
            data = Directory.objects.filter(**query)
            self.set_data(key, list(data))
        return data
    
    def set_data(self, key, data):
        self.set(key, data)
    