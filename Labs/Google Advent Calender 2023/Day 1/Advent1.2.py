# Specify the filename
filename = 'advent1.txt'

# Open the file in read mode
with open(filename, 'r') as file:
    # Loop through each line in the file
    sumnum = 0
    finalnumberz = []
    for line in file:
        numberz = ''
        )
        for letter in line:
            if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                numberz = numberz + letter
        sliced = numberz[0]
        sliced2 = numberz[-1]
        finalnumberz = (sliced+sliced2)
        sumnum = sumnum + int(finalnumberz)
        print (sumnum)