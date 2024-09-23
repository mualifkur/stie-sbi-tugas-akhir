from django.contrib import admin
from mahasiswa.models import *

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'jurusan', 'tahun']
    search_fields = ['nim', 'nama', 'jurusan', 'tahun']
    list_per_page = 4
    
class TugasAkhirAdmin(admin.ModelAdmin):
    list_display = [
        'mahasiswa_id',
        'judul',
        'acc_ujian',
        'bebas_teori',
        'krs',
        'cek_plagiasi',
        'file_tugas_akhir',
        'sk_diterima',
        'sk_selesai',
        'lembar_penilaian',
        'kepemilikan_usaha',
        'bukti_mou_spk',
        'ijazah_terakhir',
        'akte_kelahiran',
        'ktp_kk',
        'foto',
        'status_validasi_dospem',
        'status_validasi_keuangan',
        'status_validasi_akademik',
        ]
    search_fields = ['judul']
    list_per_page = 4
    
class DospemAdmin(admin.ModelAdmin):
    list_display = ['nama_dosen', 'mahasiswa_id']
    search_fields = ['nama_dosen']
    list_per_page = 3
    
class JadwalUjianAdmin(admin.ModelAdmin):
    list_display = ['mahasiswa_id', 'hari', 'tanggal', 'penguji1', 'penguji2', 'pengawas']
    search_fields = ['hari']
    list_per_page = 4

admin.site.register(JadwalUjian, JadwalUjianAdmin)
admin.site.register(DosenPembimbing, DospemAdmin)
admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Tugasakhir, TugasAkhirAdmin)
admin.site.register(User)   