def Function(n):

    #print('Hello Django girls!')

    #date = 10

    if n <= 10:
        dd = n
        print('Number minor/equal to 10')
        print(dd)
    elif n >= 20:   
        dd = n
        print('Number greater/equal 20')
        print(dd)
    else:
        dd = n
        print('Number in between')
        print(dd)

number = [1, 4, 25, 18, 9, 20]

for n in number: 
    Function(n)
    
    #print('Next date')



