with open("password.txt","r") as firstfile,open("1stday.txt","r")as secondfile:
    for line in firstfile:
        secondfile.write(line)
