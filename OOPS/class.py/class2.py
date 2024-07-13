#specific methods : specific methods are automatically called by the interpreter when we create the object 
# __init__ is used to create specific methods and specific properties 
#mandatoryly we are providing the self argument
#self is used to store the instance object address or self is used for carying the instance object address
#If we use __init__ for creating specific properties of an object then it is known as constructor
'''SPECIFIC PROPERTIES CANNOT BE ACCESED BY USING CLASS'''
#SYTAX FOR CREATING SPECIFIC PROPERTIES
''' objectname.specificproperty=value '''
#EXAMPLE
class kalki:
    p_name='VAMSIKRISHNA'
    p_strength='SELFCONFIDENCE'
    p_code=1001811
    p_address='INDIA'
    def __init__(self,n,r,b):
        self.subject_name=n
        self.subject_reason=r
        self.subject_needs=b
earth=kalki('earth','need a protector',' A saviour')
print(earth.subject_name)
print(kalki.p_code)
#WE CANNOT ACCESS SPECIFIC PROPERTIES BY USING  CLASS REFERENCE 
#print(kalki.subject_name) #error