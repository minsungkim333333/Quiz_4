b=int(input("몇 단까지 출력할까요?"))
def qqd(a):
    for x in range(1, a+1):
        print("------["+ str(x)+"단] ------")
        for y in range(1, a+1):
            print(x,"x",y ,"=", x*y)
qqd(b)
