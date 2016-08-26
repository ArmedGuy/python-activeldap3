from ldap3 import *
from ActiveLdap3 import *
class LdapModel(object):
    _key
    _baseDN = "ou=%s,dc=example,dc=com"
    _objectClasses = []
    _connection = None
    _knownValues = ["_connection", "_modValues", "_currentValues", "_deleteValues", "_dirty", "dn"]
    def __init__(self, dn, currentValues=[]):
        self.dn = dn
        self._newValues = {}
        self._currentValues = currentValues
        self._deleteValues = []
        self._dirty = False
    
    def __getattr__(self, attr):
        if attr in _knownValues:
            return super(LdapModel, self).__getattr__(attr)
        else:
            if attr in self.__dict__['_modValues'].keys():
                return self.__dict__['_modValues'][attr]
            else:
                return self.__dict__['_currentValues']

    def __setattr__(self, attr, val):
        if attr in _knownValues:
            super(LdapModel, self).__setattr__(attr, val)
        else:
            self.__dict__['_modValues'][attr] = val
    def __delattr__(self, attr):
        if not attr in self.__dict__['_deleteValues']:
            self.__dict__['_deleteValues'].append(attr)

    
    # Class functions
    def merge(self, attrs):
        for k,v in attrs:
            self.__setattr__(k,v)

    def commit(self):
        pass
    

    # Static functions
    @classmethod
    def all(cls):
        pass

    @classmethod
    def get(cls, primary):
        cls._connection.search(cls._baseDN, "%s=%s" % (cls._key, primary))