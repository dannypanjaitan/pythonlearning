#meminta input dari user
num = int(input("Masukkan bilangan :"))
#bilangan prima harus lebih dari satu
if num>1 :
    for i in range (2,num):
        if (num%i) == 0 :
            print(num, "bukan bilangan prima")
            print(i, "kali", num//i, "=", num)
            break 
        else:
            print(num, "adalah bilangan prima")
else:
    print(num, "bukan bilangan prima")