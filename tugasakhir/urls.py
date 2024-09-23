from django.contrib import admin
from django.urls import path
from mahasiswa.views import *
from django.contrib.auth.views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('mahasiswa/', mahasiswa, name='mahasiswa'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
    path('daftar-tugas-akhir/', upload, name='data_upload'),
    path('upload/', upload_syarat, name='upload'),
    path('daftar-tugas-akhir/detail/<int:id_tugasakhir>', detail_tugas_akhir, name='detail_ta'),
    path('daftar-tugas-akhir/hapus/<int:id_tugasakhir>', hapus_ta, name='hapus_tugasakhir'),
    path('daftar-tugas-akhir/ubah/<int:id_tugasakhir>', ubah_ta, name='ubah_tugasakhir'),
    path('data-dosen-pembimbing/', data_dospem, name='data_dospem'),
    path('daftar-dosen-pembimbing/', daftar_dospem, name='daftar_dospem'),
    path('tambah-dosen-pembimbing/', tambah_dospem, name='tambah_dospem'),
    path('dospem/ubah/<int:id_dosenpembimbing>', ubah_dosen_pembimbing, name='ubah_dospem'),
    path('dospem/hapus/<int:id_dosenpembimbing>', hapus_dosen_pembimbing, name='hapus_dospem'),
    path('jadwal-ujian-sidang/', jadwal_ujian, name='jadwal_ujian'),
    path('daftar-jadwal-ujian-sidang/', daftar_jadwal_ujian, name='daftar_jadwal_ujian'),
    path('tambah-jadwal-ujian-sidang/', tambah_jadwal_ujian, name='tambah_jadwal_ujian'),
    path('jadwal-ujian-sidang/ubah/<int:id_jadwalujian>', ubah_jadwal_ujian, name='ubah_jadwal_ujian'),
    path('jadwal-ujian-sidang/hapus/<int:id_jadwalujian>', hapus_jadwal_ujian, name='hapus_jadwal_ujian'),
    path('data-validasi/', data_validasi, name='data_validasi'),
    path('data-validasi-dosen-pembimbing/', validasi_dosen_pembimbing, name='validasi_dospem'),
    path('data-validasi-dosen-pembimbing/validasi/<int:id_validasi_dospem>', ubah_validasi_dospem, name='ubah_validasi_dospem'),
    path('data-validasi-akademik/', validasi_akademik, name='validasi_akademik'),
    path('data-validasi-akademik/validasi/<int:id_validasi_akademik>', ubah_validasi_akademik, name='ubah_validasi_akademik'),
    path('data-validasi-akademik/detail/<int:id_validasi_akademik>', detail_validasi_akademik, name='detail_validasi_akademik'),
    path('data-validasi-keuangan', validasi_keuangan, name='validasi_keuangan'),
    path('data-validasi-keuangan/ubah/<int:id_validasi_keuangan>', ubah_validasi_keuangan, name='ubah_validasi_keuangan'),
    path('login/', LoginView.as_view(), name='masuk'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('buku/', index, name='buku'),                                   
    path('berita-acara-mahasiswa/', berita_acara_mahasiswa, name='berita_acara_mahasiswa'),                                   
    path('berita-acara/', berita_acara, name='berita_acara'),                                   
    path('presensi-kehadiran/', presensi_kehadiran, name='presensi_kehadiran'),                                   
    path('lembar-revisi/', lembar_revisi, name='lembar_revisi'),                                   
    path('lembar-yudisium/', lembar_yudisium, name='lembar_yudisium'),                                   
    path('rekapitulasi-penilaian/', lembar_rekapitulasi, name='lembar_rekapitulasi'),                                   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)