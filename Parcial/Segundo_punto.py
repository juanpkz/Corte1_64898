def Primos(num):       
 for i in range(1, num + 1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i,' ')

if __name__=="__main__":
    Primos(10)