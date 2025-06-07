# Create a function that takes a range of 1, 100, 100 being being included and append to a list only the even numbers

def even_only():
    li = []
    for i in range(1, 100):
        if i % 2 == 0:
            li.append(i)
    print(li)
even_only()
