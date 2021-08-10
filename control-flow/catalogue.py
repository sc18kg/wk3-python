book = {
    "name" : "The Iliad",
    "author" : "Homer",
    "rating" : 7
}

for item in book:
    print(item)    # When iterating through a dictionary you get the keys

for item in book.values():
    print(item)             # prints the values

for item in book.items():
    print(item)             # prints key and value

for key, value in book.items():
    print(f"The {key} is {value}")      # If the items has two values you can assign two variables

library = [
    {
    "title" : "The Iliad",
    "author" : "Homer",
    "rating" : 7
    },
    {
    "title" : "The Foundation of Mathematics",
    "author" : "Ian Stweart & David Tall",
    "rating" : 8.5
    },
    {
    "title" : "The Very Hungry Caterpillar",
    "author" : "Eric Carle",
    "rating" : 10,
    "synopsis": "Caterpillar eats lots and transforms"
    }

]

for books in library:
    if "synopsis" in books.keys():
        print(f"Title: {books['title']} \nSynopsis : {books['synopsis']}") 


for books in library:
    synopsis = books.get("synopsis")
    if synopsis:
        print(f"Title: {books['title']} \nSynopsis : {synopsis}")    


x = range(10)
for i in x:
    print(i)