print("Hello world !\n")

print("\"Hello world !\" ")

phrase = "Perkenalkan nama saya "

character_name = "Danny"

print(phrase + character_name + ",salam kenal")
#phrase jadi huruf kecil
print(phrase.lower() + character_name + ",salam kenal")
#phrase jadi huruf besar
print(phrase.upper() + character_name + ",salam kenal")
#memberi nilai apakah phrase huruf besar
print(phrase.isupper())
#membesarkan phrase,cek apakah phrase besar atau tidak
print(phrase.upper().isupper())
#menentukan panjang phrase
print(len(phrase))
#print huruf ke-0 dari phrase
print(phrase[0])
#memberikan indeks dimana ada huruf P
print(phrase.index("P"))
#memberikan indeks dimana kata saya mulai
print(phrase.index("saya"))
#menggantikan kata nama dengan kata replace
print(phrase.replace("nama","kata replace"))