val=int(input('Please, type a number:  '))
lst=[int((x/2)**3) for x in range(val) if x%3==0]

print(lst)


