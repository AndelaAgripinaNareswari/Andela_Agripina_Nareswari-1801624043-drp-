from datetime import datetime
print("=================================")
print("APLIKASI MANAJEMEN AKTIVITAS")
print("=================================")
aktivitas = input("Masukkan aktivitas (sarapan/kerja): ").lower()
#Aktivitas sarapan
if aktivitas == "sarapan":
    menu = input("Masukkan menu sarapan: ").lower()
    if menu == "telur":
        print("\nBahan telur tersedia.")
        print("Silakan masak terlebih dahulu.")
        print("Estimasi waktu memasak: 5 menit.")
        elif menu == "ikan":
            print(\nBahan ikan tersedia.")
            print(Silakan masak terlebih dahulu.")
            print("Estimasi waktu memasak: 15 menit>")
            elif menu == "nugget":
                print("\nBahan nugget tersedia.")
                print("Silakan masak terebih dahulu.")
                print("Estimasi waktu memasak: 10 menit.")
                else:
                    print("\nBahan untuk menu tersebut tidak tersedia.")
                    print("Silakan membeli bahan terlebih dahulu>")
                    #Aktivitas Kerja
                    elif aktivitas == "kerja":
                        sekarang = datetime.now()
                        print("\nWaktu saat ini :", sekarang.strftime("%H:%M:%S"))
                        jam_masuk = sekarang.replace(
                            hour=8,
                            minute=0,
                            second=0,
                            microsecond=0
                        )
                        if sekarang > jam_masuk:
                            selisish = sekarang - jam_masuk
                            menit_terlambat = selisih.seconds // 60
                            print("PERINGATAN!")
                            print(f"Anda terlambat masuk kerja {menit_terlambat} menit.")
                            else: 
                                selisih = jam_masuk - sekarang
                                menit_sisa = selisish.seconds // 60
                                print("Anda belum terlambat masuk kerja.")
                                print(f"Sisa waktu menuju jam kerja: {menit_sisa} menit.")
                                #Jika aktivitas tidak sesuai
                                else:
                                    print("\nAktivitas tidak dikenali.")
                                    print("silakan pilih 'sarapan' atau 'kerja'.")
                                    print("\nProgram selesai.")
                                    
                    