def f(detector):
    for person in detector:
        print(person,person[-1])
        if person == person[-1]:
            print('chuj')
print(f("-++"))