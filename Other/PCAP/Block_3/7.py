plane = "Cessna"
counter = 0 
for c in plane * 2:
    if c in ["e", "a"]:
        counter += 1
print(counter)

#4
#The code is error-free and will successfully. As plane * 2 evaluates to 'CessnaCessna', so will return True 4 times