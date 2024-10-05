# without using reg-ex

#555-444-6666

def is_phone_number(p_string):
    if len(p_string)!=12:
        #not a phone number size
        
        return False
    for i in range(0,3):
        if not p_string[i].isdecimal():
            #area code is missing
            return False
    if p_string[3]!='-':
        # missing 1st dash
        return False
        
    for i in range(4,7):
        if not p_string[i].isdecimal():
            #missing 1st digit
            return False
    if p_string[7]!='-':
        # missing 2nd dash
        return False
    for i in range(8,12):
        if not p_string[i].isdecimal():
            #last digit is missing
            return False
    return True
    
    
    
print(is_phone_number("11a-123-9999"))

ip ="my number is :111-777-8888 and office number is: 333-444-8888"

p_number=False

for i in range(len(ip)):
    inp=ip[i:i+12]
    if is_phone_number(inp):
        print(f"Phone number found is:{inp}")
        p_number=True

if not p_number:
    print("There is no number")
  
        
