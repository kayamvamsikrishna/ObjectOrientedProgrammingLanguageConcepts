class Bank:
    bank_name='SBI'
    bank_ifsc=12345
    bank_roi=6
    bank_address='America'
vamsi=Bank()
krishna=Bank()
print(Bank.bank_roi)##accesing the generic properties using class
print(vamsi.bank_name)#accesing the generic properties using object
#first senario
Bank.bank_name='Union'#modifying the generic properties using class
print(Bank.bank_name)
print(vamsi.bank_name)
#second senario
vamsi.bank_name='AXIS'#modifying the generic properties using object
print(vamsi.bank_name)
print(Bank.bank_name)
#creation
Bank.bank_mobile_number=9639171877#creation of generic properties using class
print(Bank.bank_mobile_number)
print(vamsi.bank_mobile_number)
vamsi.mobile_number=6305416407#creation of specific properties using object
print(vamsi.mobile_number)
#print(Bank.mobile_number) ''' generic property is not created '''
'''we cannot create new generic property using object'''
