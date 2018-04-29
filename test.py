#Step2
import random

a=int(input())
example_list=[x+random.randint(1,10) for x in range(1,a)]
i=int(input('Введите номер из списка'))
try:
    print(example_list[i])
except IndexError:
    print('В списке меньше аргументов')
    print('Список состоит из {} данных.'.format(i))
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22

#Step3
def fun(a,b):
    if a>0 and b>0:
        result=a+b
    elif a<0 and b<0:
        result=a-b
    else:
        result=0
    return result
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#Step4
def find_two_max(a,b,c):
    list=[a,b,c]
    list.sort()
    return list[2], list[1]
find_two_max(3,7,1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Step5
def filter_list(a, mod=False):
    new_list_chet=[]
    new_list_else=[]
    for i in a:
        if i%2==0:
            new_list_chet.append(i)
        else:
            new_list_else.append(i)
    if mod==False:
        return new_list_else
    else:
        return new_list_chet
st=int(input())
ds=[x for x in range(0,st+1)]
filter_list(ds, False)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Step6
def find_min_max(*args):
    a=args[0]
    b=args[0]
    for i in args:
        if i<a:
            a=i
    for i in args:
        if i>b:
            b=i
    return a,b
find_min_max(4,2,5,2,3,6,3,3,2,3,4,12,4,3,2,534,2,3,54,3,6)

#Step7
def lower_upper_case(string, case=True):
    if case:
        return string.lower()
    else:
        return string.upper()
lower_upper_case('Hello World!',False)

#Step8
def unit_string(glue=':', **kwargs,):
    out_string=''
    for key, value in kwargs.items():
        if len(kwargs[key])>3:
            out_string+=kwargs[key]
            out_string+=glue
    return out_string[:-1]
unit_string(name1='John', n2='Lisa', n3='Den', n4='Mikky')
