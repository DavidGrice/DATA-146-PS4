def exp(a,b):
    if (b == 0):
        return a
    else:
        return a*exp(a,b=b-1)

def find_val(target, numbers, start_index=0):
    if (start_index > len(numbers)):
        return -1
    elif (target == numbers[start_index]):
        return start_index
    else:
        return find_val(target, numbers, start_index=start_index+1)

if __name__ == '__main__':
    #print(exp(2,2))
    numbers = [1,2,3,4,5,6,7,8,9,90]
    print(find_val(90,numbers,0))