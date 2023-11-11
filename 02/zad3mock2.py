def f(n):

    words = n.split() 
    x=[]
    for word in words:
        if word:  
            first_letter = word[0]
            x.append(first_letter)
    return "".join(x)

print(f('Internet of Things'))
