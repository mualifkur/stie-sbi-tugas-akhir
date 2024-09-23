from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=15)
    nama = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=40)
    tahun = models.IntegerField(null=True)
    
    def __str__(self):
        return self.nim

class Tugasakhir(models.Model):
    validasi_choices = [
        ("Sudah Divalidasi", "Sudah Divalidasi"),
        ("Belum Divalidasi", "Belum Divalidasi"),
    ]
    
    judul = models.CharField(max_length=50)
    mahasiswa_id = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)
    acc_ujian = models.FileField(upload_to='bukti_acc_ujian/', null=True)
    bebas_teori = models.FileField(upload_to='bukti_bebas_teori/', null=True)
    krs = models.FileField(upload_to='bukti_krs/', null=True)
    cek_plagiasi = models.FileField(upload_to='bukti_hasil_cek-plagiasi/', null=True)
    file_tugas_akhir = models.FileField(upload_to='file_tugas_akhir/', null=True)
    sk_diterima = models.FileField(upload_to='sk_diterima/', null=True)
    sk_selesai = models.FileField(upload_to='sk_selesai/', null=True)
    lembar_penilaian = models.FileField(upload_to='lembar_penilian/', null=True)
    kepemilikan_usaha = models.FileField(upload_to='bukti_usaha/', null=True)
    bukti_mou_spk = models.FileField(upload_to='bukti_mou_spk/', null=True)
    ijazah_terakhir = models.FileField(upload_to='bukti_ijazah_terakhir/', null=True)
    akte_kelahiran = models.FileField(upload_to='bukti_akte_kelahiran/', null=True)
    ktp_kk = models.FileField(upload_to='bukti_ktp_kk/', null=True)
    foto = models.FileField(upload_to='pas_foto/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    status_validasi_dospem = models.CharField(choices=validasi_choices, null=True, max_length=50, default="Belum Divalidasi")
    status_validasi_keuangan = models.CharField(choices=validasi_choices, null=True, max_length=50, default="Belum Divalidasi")
    status_validasi_akademik = models.CharField(choices=validasi_choices, null=True, max_length=50, default="Belum Divalidasi")
    
    def __str__(self):
        return self.judul
    
class DosenPembimbing(models.Model):
    nama_dosen = models.CharField(max_length=50)
    mahasiswa_id = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nama_dosen
    
class JadwalUjian(models.Model):
    hari = models.CharField(max_length=10)
    tanggal = models.DateField(null=True)
    penguji1 = models.CharField(max_length=50)
    penguji2 = models.CharField(max_length=50)
    pengawas = models.CharField(max_length=50)
    mahasiswa_id = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.hari
    

class UserManager(BaseUserManager):
    def create_user(self, id_pengguna, password=None, **extra_fields):
        if not id_pengguna:
            raise ValueError('id_pengguna harus diisi')

        user = self.model(id_pengguna=id_pengguna, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_pengguna, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser harus memiliki is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser harus memiliki is_superuser=True.')

        return self.create_user(id_pengguna, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    nama_pengguna = models.CharField(max_length=255)
    id_pengguna = models.CharField(max_length=20, unique=True,primary_key=True)
    keterangan = models.CharField(max_length=255)
    prodi = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'id_pengguna'
    REQUIRED_FIELDS = ['nama_pengguna', 'email']

    objects = UserManager()

    def _str_(self):
        return str(self.id_pengguna)