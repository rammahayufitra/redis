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
|5|membuat append key|append key value| append ramma1 " hayu"|
|6|mengambil beberapa pattern|keys pattern| keys ramma*|
|7|set sebagian data|setrange key start end|-----------|
|8|get sebagian data|getrange key start end|-----------|
|9|melakukan get multiple key|mget key1 key2| mget ramma1 ramma2|
|10|melakukan set multiple key|mset key1 value1 key2 value2|mset ramma1 "hallo ramma1" ramma2 "hallo ramma2"|
