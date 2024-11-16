#Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
#in each case.
#* Write a loop that counts up from 0 to 50 in increments of 1.
#* Write a loop that counts down from 50 to 0 in decrements of 1.
#* Write a loop that counts up from 30 to 50 in increments of 1.
#* Write a loop that counts down from 50 to 10 in decrements of 2.
#* Write a loop that counts up from 100 to 200 in increments of 5.
#*You may include all loops in a single project*

#this is a loop that increases by 1 in steps from 0 to 50
print("Advancing from 0 to 50 in increments of 1:")
for mnr in range(0, 51):
    print(mnr)

#this is a loop that decreases by 1 in steps from 50 to 0
print("\nDescending from 50 to 0 in decrements of 1:")
for mnr in range(50, -1, -1):
    print(mnr)

#this is a loop that increases by 1 in steps from 30 to 50
print("\nAdvancing from 30 to 50 in increments of 1:")
for mnr in range(30, 51):
    print(mnr)

#this is a loop that decreases by 2 in steps from 50 to 10
print("\nDescending from 50 to 10 in decrements of 2:")
for mnr in range(50, 9, -2):
    print(mnr)

#this is a loop that increases by 5 in steps from 100 to 200
print("\nAdvancing from 100 to 200 in increments of 1:")
for mnr in range(100, 201, 5):
    print(mnr)