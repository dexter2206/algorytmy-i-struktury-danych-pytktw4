import operator

if __name__ == '__main__':
    numbers = [1, 31, 21, 37, 0, 5]
    print(sorted(numbers,reverse=True))
    print(numbers)

    names = ["Ala", "Konrad", "Mariusz", "Marek"]
    print(sorted(names, key=len))
    print(sorted(names))

    def lastname(student):
        return student["lastname"]

    students = [
        {"firstname": "Ala", "lastname": "Nowak"},
        {"firstname": "Jacek", "lastname": "Kowalski"},
        {"firstname": "Hania", "lastname": "Kuźba"}
    ]

    print(sorted(students, key=lastname))
    print(sorted(students, key=operator.itemgetter("lastname")))
