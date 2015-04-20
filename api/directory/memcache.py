from werkzeug.contrib.cache import MemcachedCache
from models import Directory


class AppCache(MemcachedCache):
    """
    Class to be used for memcached interaction.
    Currently get request uses for pincode as key.
    """
    
    def __init__(self):
        MemcachedCache.__init__(self, servers=['127.0.0.1:11211'])
        
    def get_data(self, parent_key, sub_key):
        """
        If data is not is cache get it from db and set in cache
        """
        
        key = "%s__%s" % (parent_key, sub_key)
        data = self.get(key)
        
        if not data:
            query = {"id": sub_key}
            data = Directory.objects.filter(**query)
            self.set_data(key, list(data))
        return data
    
    def set_data(self, key, data):
        """
        For setting data
        """
        
        self.set(key, data)
        
    def delete_data(self, parent_key, sub_key, clear_from_db=True):
        """
        Used to delete record from db if clear_from_db=True, also
        clens up from cache.
        """
        
        num_records = 0
        
        if clear_from_db:
            num_records = Directory.objects(id=sub_key).delete()

        key = "%s__%s" % (parent_key, sub_key)
        self.delete(key)
        return num_records
    