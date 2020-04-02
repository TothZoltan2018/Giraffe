friends = ["Kevin", "Karen", "Keg"]
#things = ["Kevin", 2, True] # Ez is jo!

print(friends) #A konzolon: ['Kevin', 'Karen', 'Keg']
print(friends[1]) #A konzolon: Karen
print(friends[-2]) #A konzolon: Karen !!! c#-ban nincs ilyen
print(friends[1:]) #A konzolon: ['Karen', 'Keg'] !!! c#-ban nincs ilyen

friends = ["Kevin", "Karen", "Keg", "Oscar", "Toby"]
print(friends[1:4]) #A konzolon: ['Karen', 'Keg', 'Oscar'] !!! c#-ban nincs ilyen

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers) # ['Kevin', 'Karen', 'Keg', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
print(friends)

friends.append("Creed") # ['Kevin', 'Karen', 'Keg', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']
print(friends)
friends.insert(2, "Bela")
print(friends)

friends.remove("Bela")
print(friends)

#friends.clear()
popped = friends.pop()
print(popped), print(friends)

print(friends.index("Keg"))

friends = ["Kevin", "Karen", "Keg", "Oscar", "Toby"]
friends.append("Creed"), friends.append("Creed"), friends.append("Creed")
print(friends), print(friends.count("Creed"))

lucky_numbers = [8, 4, 15, 42, 16, 23]
lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers.sort(reverse=True)
print(lucky_numbers)

lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)

