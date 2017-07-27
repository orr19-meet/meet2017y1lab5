##c=0
##for number in range(1,100+1):
##    print(number)
##    c=c+number
##print(c)
##    

def add_numbers(start,end):
    c=0
    for num in range(start,end):
        print(num)
        c=c+num
    
    return(c)
answer=add_numbers(1000,5000)
print(answer)
