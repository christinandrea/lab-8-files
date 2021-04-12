# Christina Andrea Putri - Universitas Kristen Duta Wacana 


# Anda ingin menginput data diri Anda dan keluarga Anda untuk kepentingan sensus penduduk. Setelah itu untuk memastikan data sudah lengkap, Anda ingin melihat kembali 
# data yang Anda input. 

# Input : pilihan menu, jml data, data-data yang diperlukan
# Proses : mengetik data sesuai ketentuan
# Output : data tertulis di dalam file '.txt'

print("=Data Sensus Penduduk=")
print("Menu : \n 1. Masukkan data \n 2. Cek Data \n 3. Keluar")

inp = 0 

handle = open('data.txt','w+')
handle.close()
try : 
    while inp!=3:
        inp = int(input("Masukkan menu pilihan Anda:"))

        if inp == 1 :
            inp_sum = int(input("Jumlah data yang ingin dimasukkan: "))

            for items in range(inp_sum):
                handle = open('data.txt','a+')

                print("Data %d"%(items+1))

                handle.write("Kode Data     Nama      JK      TTL     Alamat      Kelurahan   Kecamatan    Kab./Kota      Provinsi    Status \n")
                nama = input("Nama : ")
                jk = input("Jenis Kelamin (L/P) : ")
                ttl = input("TTL : ")
                alamat= input("Alamat : ")
                kel = input("Kelurahan : ")
                kec = input("Kecamatan : ")
                kab = input("Kab./Kota : ")
                prov = input("Provinsi : ")
                status = input("Status (BM/M) : ")

                handle.write("DS00%d    %s      %s      %s      %s      %s      %s      %s      %s      %s \n"%(items+1,nama,jk,ttl,alamat,kel,kec,kab,prov,status))
            print("Berhasil!")
            handle.close()
        elif inp==2 :
            find = open('data.txt','r')
            print(find)

            for items in find : 
                print(items,end=" ")
            find.close()
        elif inp==3:
            print("Terimakasih sudah menginput data!")
except:
    print("Invalid input")
    