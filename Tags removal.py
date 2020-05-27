import re
with open ("website.txt") as f_obj,open('newwebsite.txt','w') as f_obj2:
    original_content=f_obj.read().rstrip()
    pattern= "<.+?>"
    result=re.sub(pattern,"",str(original_content))
    print(result)
    f_obj2.write(result)


