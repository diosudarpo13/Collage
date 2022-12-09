from time import sleep
def kel4():
    print ('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
    print ('*    Selamat Datang Di Project Kelompok 3       *')
    print ('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
    print ('*    Tema Project     : Kredit Mobil            *')
    print ('+    Anggota Kelompok : - Tantri Lindri Lestari +')
    print ('*                     : - Maharani Vianni K.    *')
    print ('+                     : - Dio Bagaskara Sudarpo +')
    print ('*                     : - Faiz Rabbani          *')
    print ('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
    sleep(1)
def agya():
    print ('=================================================')
    print ('|                      AGYA                     |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.2 G M/T               Rp. 158,500,000 |')
    print ('|    2. 1.2 G M/T GR SPORT      Rp. 164,350,000 |')
    print ('|    3. 1.2 G A/T GR SPORT      Rp. 180,150,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/...] : "))
    if tipe == 1:
        otr = 158500000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

    elif tipe == 2:
        otr = 164350000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')


    elif tipe == 3:
        otr = 180150000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                agya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        agya()
def calya():
    print ('=================================================')
    print ('|                      CALYA                    |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.2 E M/T STD           Rp. 158,600,000 |')
    print ('|    2. 1.2 E M/T               Rp. 161,500,000 |')
    print ('|    3. 1.2 G M/T               Rp. 167,000,000 |')
    print ('|    4. 1.2 G A/T               Rp. 181,100,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/4/...] : "))
    if tipe == 1:
        otr = 158600000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 161500000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 3:
        otr = 167100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 4:
        otr = 181100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                calya()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        calya()
def yaris():
    print ('=================================================')
    print ('|                      YARIS                    |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.5 G CVT 3 AB          Rp. 295,800,000 |')
    print ('|    2. 1.5 S M/T GR 3 AB       Rp. 308,100,000 |')
    print ('|    3. 1.5 S CVT GR 3 AB       Rp. 320,300,000 |')
    print ('|    4. 1.5 S CVT GR 7 AB       Rp. 325,700,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/4/...] : "))
    if tipe == 1:
        otr = 295800000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 308100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 3:
        otr = 320300000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 4:
        otr = 325700000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                yaris()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        yaris()
def rush():
    print ('=================================================')
    print ('|                      RUSH                     |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.5 G M/T               Rp. 278,800,000 |')
    print ('|    2. 1.5 G A/T               Rp. 289,600,000 |')
    print ('|    3. 1.5 S M/T GR SPORT      Rp. 291,500,000 |')
    print ('|    4. 1.5 S A/T GR SPORT      Rp. 302,200,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/4/...] : "))
    if tipe == 1:
        otr = 278800000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 289600000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 3:
        otr = 291500000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 4:
        otr = 302200000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                rush()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        rush()
def avanza():
    print ('=================================================')
    print ('|                      AVANZA                   |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.3 E M/T               Rp. 233,100,000 |')
    print ('|    2. 1.3 E CVT               Rp. 247,800,000 |')
    print ('|    3. 1.5 G M/T               Rp. 255,100,000 |')
    print ('|    4. 1.5 G CVT               Rp. 269,800,000 |')
    print ('|    5. 1.5 G CVT TSS           Rp. 295,800,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/4/...] : "))
    if tipe == 1:
        otr = 233100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 247800000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 3:
        otr = 255100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 4:
        otr = 269800000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 5:
        otr = 295800000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                avanza()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        avanza()
def voxy():
    print ('=================================================')
    print ('|                      VOXY                     |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 2.0 VOXY A/T NON PC     Rp. 574,600,000 |')
    print ('|    2. 2.0 VOXY A/T PC         Rp. 577,600,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/...] : "))
    if tipe == 1:
        otr = 574600000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                voxy()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                voxy()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                voxy()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 577600000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                voxy()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                voxy()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                voxy()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        voxy()
def vios():
    print ('=================================================')
    print ('|                      VIOS                     |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.5 G CVT               Rp. 325,700,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/...] : "))
    if tipe == 1:
        otr = 325700000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                vios()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                vios()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                vios()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        vios()
def camry():
    print ('=================================================')
    print ('|                      CAMRY                    |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 2.5 V A/T NON PC        Rp. 711,200,000 |')
    print ('|    2. 2.5 V A/T PC            Rp. 714,300,000 |')
    print ('|    3. 2.5 L A/T HV NON PC     Rp. 844,100,000 |')
    print ('|    4. 2.5 L A/T HV PC         Rp. 847,100,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/3/4/...] : "))
    if tipe == 1:
        otr = 711200000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1
            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 714300000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 3:
        otr = 844100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 4:
        otr = 847100000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                camry()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        camry()
def corollacross():
    print ('=================================================')
    print ('|                  COROLLA CROSS                |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.8 HV A/T Non PC       Rp. 535,300,000 |')
    print ('|    2. 1.8 HV A/T PC           Rp. 538,200,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/...] : "))
    if tipe == 1:
        otr = 535300000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollacross()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollacross()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollacross()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 538200000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollacross()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollacross()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollacross()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        corollacross()
def corollaaltis():
    print ('=================================================')
    print ('|                 COROLLA ALTIS                 |')
    print ('=================================================')
    print ('|    No.   Tipe                     Harga       |')
    print ('=================================================')
    print ('|    1. 1.8 V A/T NON PC        Rp. 493,600,000 |')
    print ('|    2. 1.8 HV A/T NON PC       Rp. 545,000,000 |')
    print ('|    99. Kembali Ke Jenis                       |')
    print ('=================================================')
    tipe = int(input("Pilih [1/2/...] : "))
    if tipe == 1:
        otr = 493600000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollaaltis()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollaaltis()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')

        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollaaltis()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 2:
        otr = 545000000
        polis = 50000
        bf = int(input('Masukan Nominal Booking Anda [Minimal Rp. 2000000] : '))
        while bf < 2000000:
            print('Nominal Tersebut dibawah Rp. 2000000')
            bf = int(input('Masukan Nominal Booking : '))
            continue
        dpm = otr * 0.2
        dp = dpm - bf
        
        if otr < 350000000:
            admin = 0.025
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02778
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.03459
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.04097
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04712
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.05306
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollaaltis()
            
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
        
        elif otr >= 350000000 and otr < 650000000:
            admin = 0.015
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.02362
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.02968
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.03535
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.04084
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.04613
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollaaltis()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
                
        elif otr >= 650000000 and otr < 950000000:
            admin = 0.01
            print ('=================================================')
            print ('|                 Tenor / Cicilan               |')
            print ('=================================================')
            print ('|    No.              Bulan                     |')
            print ('=================================================')
            print ('|    1.     12 Bulan                            |')
            print ('|    2.     24 Bulan                            |')
            print ('|    3.     36 Bulan                            |')
            print ('|    4.     48 Bulan                            |')
            print ('|    5.     60 Bulan                            |')
            print ('|    99. Kembali Ke Menu                        |')
            print ('=================================================')
            tenor = int(input("Pilih [1/2/3/...] : "))
            if tenor == 1:
                bulan = 12
                asuransi = 0.01466
                bunga = 0.046
            elif tenor == 2:
                bulan = 24
                asuransi = 0.01945
                bunga = 0.05
            elif tenor == 3:
                bulan = 36
                asuransi = 0.02398
                bunga = 0.0525
            elif tenor == 4:
                bulan = 48
                asuransi = 0.0284
                bunga = 0.0575
            elif tenor == 5:
                bulan = 60
                asuransi = 0.03268
                bunga = 0.066
            elif tipe == 99:
                menu()
            else:
                print('Nomor Salah !!!')
                corollaaltis()
            
            total_asuransi = asuransi * otr
            total_hutang = otr - dp
            pokok_angsuran = total_hutang / bulan
            total_admin = admin * total_hutang
            total_bunga = bunga * total_hutang
            pokok_bunga = total_bunga / 12
            anggaran_perbulan = pokok_angsuran + pokok_bunga
            tenor = bulan - 1

            
            if otr > 350000000 and bulan == 60:
                diskon = 0.3 * total_admin
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                total_dp_diskon = dp + total_asuransi + diskon + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('                                                            ')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total                         : Rp.', int(total_dp))
                print ('    Diskon Admin                  : Rp.', int(diskon))
                print ('                                  ---------------------- -')
                print ('    Total DP                      : Rp.', int(total_dp_diskon))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
            else:
                total_dp = dp + total_asuransi + total_admin + polis + anggaran_perbulan
                print ('============================================================')
                print ('          Rincian Pembayaran untuk', nama)
                print ('============================================================')
                print ('        Total Sudah Termasuk Angsuran Bulan Pertama         ')
                print ('============================================================')
                print ('    Harga mobil                   : Rp.', otr)
                print ('    Tenor                         :', bulan, 'bulan')
                print ('    DP                            : Rp.', int(dpm))
                print ('    Asuransi                      : Rp.', int(total_asuransi))
                print ('    Admin                         : Rp.', int(total_admin))
                print ('    Polis                         : Rp.', polis)
                print ('    Angsuran Pertama              : Rp.', int(anggaran_perbulan))
                print ('                                  ---------------------- +')
                print ('    Total DP                      : Rp.', int(total_dp))
                print ('============================================================')
                print ('    Angsuran Perbulan             : Rp.', int(anggaran_perbulan), '/', tenor, 'bulan')
                print ('============================================================')
    elif tipe == 99:
        menu()
    else:
        print('Nomor Salah !!!')
        corollaaltis()
def menu():
    print ('=================================================')
    print ('|                     Toyota                    |')
    print ('=================================================')
    print ('|    No.              Jenis                     |')
    print ('=================================================')
    print ('|    1. NEW AGYA                                |')
    print ('|    2. NEW CALYA                               |')
    print ('|    3. NEW YARIS                               |')
    print ('|    4. NEW RUSH                                |')
    print ('|    5. NEW AVANZA                              |')
    print ('|    6. NEW VOXY                                |')
    print ('|    7. NEW VIOS                                |')
    print ('|    8. NEW CAMRY                               |')
    print ('|    9. COROLLA CROSS                           |')
    print ('|    10. COROLLA ALTIS                          |')
    print ('=================================================')
    jenis = int(input("Pilih [1/2/3/...] : "))
    if jenis == 1:
        agya()
    elif jenis == 2:
        calya()
    elif jenis == 3:
        yaris()
    elif jenis == 4:
        rush()
    elif jenis == 5:
        avanza()
    elif jenis == 6:
        voxy()
    elif jenis == 7:
        vios()
    elif jenis == 8:
        camry()
    elif jenis == 9:
        corollacross()
    elif jenis == 10:
        corollaaltis()
kel4()
nama = input('Masukan Nama Anda : ')
print ( "Hallo", nama, "Silahkan pilih :")
menu()