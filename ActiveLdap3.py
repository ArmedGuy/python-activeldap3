from ldapmodel import *
class ActiveLdap3():
    defaultConnection = None
    def __init__(self, connection, dc):
        if "." in dc:
            dc = "dc=" + (",dc=".join(dc.split(".")))
        self.dc = dc
        self.connection = connection
        if defaultConnection == None:
            defaultConnection = connection
    
    def model(self, organisationalUnit, cls, settings):
        cls._connection = self.connection
        dnKey = "cn"
        if "key" in settings:
            dnKey = settings["key"]
        cls._baseDN = ",".join(["ou=%s" % organisationalUnit, self.dc])
        cls._key = dnKey
        
        if "objectClass" in settings:
            cls._objectClasses = settings["objectClass"]
        
        

def init(connection):
    return ActiveLdap3(connection)