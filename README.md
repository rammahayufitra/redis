# redis
1.perintah pindah database<br> 
select [nomor database]<br>
2.Strings di redis 
|no|keterangan|perintah|contoh|
|--|----------|--------|------|
|1|menyimpan data string di key|set key value| set ramma1 "hallo ramma selamat data diredis"|
|2|mengambil data string di key|get key|get ramma1
|3|check apakah di key ada data|exists key|exists ramma1
|4|menghapus key|del key|del ramma1 (untuk satu key) & del ramma1 ramma2 (untuk banyak key)|
|5|melakukan append data|append ramma1 " hayu" contoh hasil "ramma hayu"|