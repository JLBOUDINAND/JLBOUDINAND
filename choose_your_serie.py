print("What is your favorite TV show?")
books = ["Harry Potter", "Lord of the Rings", "Star Wars"]
print("Options:")
for i in range(len(books)): # use len() to get the length of the list
    print("Press " + str(i) + " for " + books[i]) # use str() to convert the index to a string

while True:
    try:
        index = int(input("Enter a number: "))
        if 0 <= index < len(books): # verify that the index is valid
            selected_book = books[index]
            break  # leave the loop
        else:
            print("Invalid choice, out of range!")
    except ValueError:
        print("Invalid input, please enter a valid number!")

print("Good choice! I love " + selected_book + ". It's a wonderful TV show!")
print("Thank you for using the TV show selector!")
