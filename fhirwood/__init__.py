__version__="0.1.0"

class FhirBase:
    def add_kv(self, obj, key, value=None, propname=None):
        """Add data to an object at key, key. 

        if value is None, then the the value is pulled from a local data member (either key or propname)"""

        if value is None:
            if propname is None:
                propname = key

            value = eval(f"self.{propname}")

        if value:
            obj[key] = value        
