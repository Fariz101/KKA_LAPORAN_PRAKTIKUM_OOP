# KKA_LAPORAN_PRAKTIKUM_OOP
Tugas Analisis 1:
• Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris
hero1 = Hero...? Coba lakukan print(hero1.hp).
Jawaban: <img width="564" height="95" alt="image" src="https://github.com/user-attachments/assets/a420fc97-ef85-44fa-bf81-a100e0eb8501" />
Hp dari hero1 akan berubah menjadi 500 dari sebelumnya yaitu 100

Tugas Analisis 2:
• Perhatikan parameter lawan pada method serang. Parameter tersebut
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini
penting?
Jawaban: Karena dengan menerima objek utuh maka method serang bisa membaca data dari lawan yang tidak hanya berisi string nama

Tugas Analisis 3:
• Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan
komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian
jalankan programnya.
Jawaban: <img width="636" height="202" alt="image" src="https://github.com/user-attachments/assets/9e607002-c2ba-4079-9e17-42d7cb6ae06e" />
Akan muncul error
• Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no
attribute 'name', padahal kita sudah mengirim nama "Eudora" saat
pembuatan objek?
Jawaban: Muncul error "AttributeError: 'Mage' object has no attribute 'name'", dikarenakan atribut name di class Mage tidak di definisikan secara mandiri, melainkan dengan pewarisan dari class hero.
• Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke
class Induk!
Jawaban: Peran dari fungsi super() ialah untuk mengakses class induk dengan mendifiniskan atribut dari class induk ke class anak

Tugas Analisis 4:
1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling
bawah (luar class):
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan
temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling)
dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman
yang baik.
Jawaban: Nilai HP muncul. Alasan mengapa Python masih mengizinkan Name Mangling ialah untuk mencegah subclass menimpa variabel milik parent class. Kita tidak melakukannya dikarenakan itu akan melanggar kontrak encapsulation dan bisa menyebabkan kerusakan data
2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya
hanya self.__hp = nilai_baru.
Pertanyaan: Kemudian lakukan hero1.set_hp(-100).
Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method
Setter sangat penting untuk menjaga integritas data dalam game!
Jawaban: Data HP Hero akan muncul dengan nilai -100, alasan mengapa method setter sangat penting ialah untuk memberikan validasi pada data game karena bila hal seperti HP yang bernilai -100 ini muncul maka itu akan menjadi bug yang tak masuk akal karena karakter game tidak seharusnya memiliki HP -100.

Tugas Analisis 5:
1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh
blok method def serang(self, target):. Jalankan programnya.
Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti
pesan error Can't instantiate abstract class Hero with abstract
method...?
Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di
Interface?
Jawaban: Error yang muncul adalah "TypeError: Can't instantiate abstract class Hero without an implementation for abstract method 'serang'". Menurut saya arti error itu adalah kita menetapkan sebuah abstract class bernama Hero yang memiliki abstract method "serang" tanpa mengimplementasikannya di class konkret. Konsekuensinya adalah akan muncul error "TypeError: Can't instantiate abstract class Hero without an implementation for abstract method 'serang'"
2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit().
Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?
Jawaban: Karena class GameUnit adalah abstract class yang memang dari python dilarang untuk dibuat menjadi objek. Gunanya ialah sebagai interface atau template atribut untuk class anaknya

Tugas Analisis 6:
1. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf
pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class
baru bernama Healer(Hero).
Isi method serang milik Healer dengan: print(f"{self.name} tidak
menyerang, tapi menyembuhkan teman!").
Masukkan objek Healer ke dalam list pasukan.
o Pertanyaan: Apakah program berjalan lancar?
o Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer
ketika harus mengupdate game dengan karakter baru di masa depan?
Jawaban: Ya program berjalan lancar. Keuntungan utama menurut saya adalah untuk mempermudah dan mempercepat proses penambahan atau pembaruan karakter baru dimasaa depan karena tidak perlu membongkar seluruh program seperti bila tidak menggunakan Polimorfisme.
2. Konsistensi Penamaan: Ubah nama method serang pada class Archer
menjadi tembak_panah. Jalankan program.
Pertanyaan: Apa yang terjadi?
Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan
berbagai Child Class harus persis sama?
Jawaban: Program di class archer tidak dijalankan melainkan menjalankan program di method serang yang berada di class Hero. Dikarenakan kontrak antar class mengharuskan method yang ada di Child Class harus sama dengan yang ada di Parent Class supaya program bisa dijalankan.

# Output Tugas Proyek Kelompok

<img width="597" height="471" alt="image" src="https://github.com/user-attachments/assets/e28ab5af-9426-405b-87e0-2430c6ed829e" />
