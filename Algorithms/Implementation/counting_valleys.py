n = int(input(""))
steps = input("")
total = 0
valleys = 0
mountains = 0
for i in steps:
    if i =="U":
        total += 1
        if (total-1)==0:
            mountains += 1
    else:
        total -= 1
        if (total+1)==0:
            valleys += 1

print(valleys)
        
        
        
        