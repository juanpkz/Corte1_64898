def main(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

if __name__=="__main__":
    main(1,2,3,4,5,6,7, i=10, j=15)