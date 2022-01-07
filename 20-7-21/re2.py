import re
john="9789110483" 
santh=re.search("[91]?(5|6|7|8|9)[0-9]{6,12}",john)
print("result:",santh)
