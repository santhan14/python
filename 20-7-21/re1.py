import re
text="santhan143@gmail.com"
sand=re.search("[a-zA-Z0-9]{1,100}@gmail.com$",text)
print("result:",sand)
