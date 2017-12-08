i=a=b=c=0
nama=[]
nim=[]
kls=[]
jur=[]
ang=[]
while True:
    print("Masukkan data ke - "),i+1
    nama.append(int(input("Nama anda : ")))
    nim.append(int(input("NIM Anda : ")))
    if len(npm[i])!=8:
       print("NIM Salah")
       print
       nama.pop(i)
       nim.pop(i)
       continue
    kls.append(raw_input("Kelas Anda : "))
    if len(kls[i])!=5:
       print("Kelas Salah")
       print
       nama.pop(i)
       nim.pop(i)
       kls.pop(i)
       continue
    jur.append(kls[i][1:3])
    ang.append(nim[i][3:5])
    if jur[i]=="IA":
        jur[i]="Teknik Informatika"
        a+=1
    elif jur[i]=="IB":
        jur[i]="Teknik Industri"
        b+=1
    elif jur[i]=="IC":
        jur[i]="Teknik Mesin"
        c+=1
    else:
        print("Kelas Salah")
        print
        continue
    lagi=""
    while lagi!="y" and lagi!="t":
        lagi=raw_input("INPUT LAGI [Y/T] : ")
    i+=1
    if lagi=="t":
        break
print("                        Daftar Mahasiswa ")
print("========================================================================")
print("No.  Nama     NPM     Kelas  Angkatan  Jurusan")
print("========================================================================")
for n in range(i):
    print("n+1", "nama[n]", ",nim[n]", "kls[n]", "ang[n]", "jur[n]")
print("TOTAL JURUSAN TEKNIK INFORMATIKA = "),a,"orang\n"
print("TOTAL JURUSAN TEKNIK INDUSTRI = "),b,"orang\n"
print("TOTAL JURUSAN TEKNIK MESIN = "),c,"orang\n"
ing=""
while ing!="y" and ing!="t":
    ing=raw_input("Ingin melihat hasil [Y/T]? ")
if ing=="y":
    cari=raw_input("Cari berdasarkan NIM : ")
    for n in range(i):
        if cari==nim[n]:
            print
            print("Nama :"),nama[n]
            print("Kelas :"),kls[n]
            print("Angkatan :"),ang[n]
            print("Jurusan :"),jur[n]
            break
        else:
            print("NIM TIDAK ADA")
            break