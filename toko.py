menu =[["Nasi Goreng",15000],["Nasi Kuning",14000],["Nasi Pecel",12000]]

def menu_makanan ():
    print("#------------------------------#")
    print("# No | Nama Makanan | Harga    #")
    print("#------------------------------#")
    i = 1
    for item in menu :
        print("# " + str(i) + "|" + item[0] + "|" + str(item[1]) +"#")
        i+=1
    print("#------------------------------#")
    print("# 0 | Checkout #")
    print("#------------------------------#")
    return 

menu_makanan()
jawaban = ""
catatan_pilihan = []
while jawaban != "0":
    jawaban = input("Pilih menu makanan ")
    menu_makanan()
    if jawaban != "0":
        catatan_pilihan.append(int(jawaban)-1)

no = 1
print("Pesanan Anda :")
total = 0
for pilihan in catatan_pilihan:
    print("Makanan ke-"+str(no)+"="+menu[pilihan][0]+"Harga +"+str(menu[pilihan][1]))
    no += 1
    total = total + menu[pilihan][1]

print("Total pembayaran "+str(total))