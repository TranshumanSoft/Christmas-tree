starsnumber = int(input("How many lines do you want for your tree?"))
counterstars = ''
counter = 0
while True:
    counterstars = counterstars + "*"
    print(counterstars)
    counter = counter + 1
    if counter == starsnumber:
        break
print("Here's your Christmas Tree!")