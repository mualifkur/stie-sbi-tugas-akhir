from django.forms import ModelForm
from mahasiswa.models import *
from django import forms
from django.utils import formats

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'
        
        widgets = {
            'nim': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'jurusan': forms.TextInput({'class':'form-control'}),
            'tahun': forms.TextInput({'class':'form-control'}),
        }
        
class FormDospem(ModelForm):
    class Meta:
        model = DosenPembimbing
        fields = [
            'mahasiswa_id',
            'nama_dosen',
        ]
        labels = {
            'mahasiswa_id': ('NOMOR POKOK MAHASISWA '),
            'nama_dosen': ('NAMA DOSEN PEMBIMBING '),
        }
        widgets = {
            'mahasiswa_id': forms.Select({'class':'form-control'}),
            'nama_dosen': forms.TextInput({'class':'form-control'}),
        }
        
class FormJadwalUjian(ModelForm):
    class Meta:
        model = JadwalUjian
        fields = [
            'mahasiswa_id',
            'hari',
            'tanggal',
            'penguji1',
            'penguji2',
            'pengawas',
        ]
        labels = {
            'mahasiswa_id':('NOMOR POKOK MAHASISWA '),
            'hari':('HARI '),
            'tanggal':('TANGGAL '),
            'penguji1':('PENGUJI 1 '),
            'penguji2':('PENGUJI 2 '),
            'pengawas':('PENGAWAS '),
        }
        widgets = {
            'mahasiswa_id': forms.Select({'class':'form-control'}),
            'hari': forms.TextInput({'class':'form-control'}),
            'tanggal': forms.DateInput({'class':'form-control','type':'date'}),
            'penguji1': forms.TextInput({'class':'form-control'}),
            'penguji2': forms.TextInput({'class':'form-control'}),
            'pengawas': forms.TextInput({'class':'form-control'}),
        }
        
class FormTugasAkhirAdmin(ModelForm):
    class Meta:
        model = Tugasakhir
        fields = [
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
        
        labels = {
            'mahasiswa_id': ('NOMOR INDUK MAHASISWA '),
            'judul': ('JUDUL TUGAS AKHIR '),
            'acc_ujian': ('BUKTI ACC UJIAN SIDANG '),
            'bebas_teori': ('BUKTI BEBAS TEORI DARI DOSEN PEMBIMBING AKADEMIK '),
            'krs': ('BUKTI KRS PADA SEMESTER BERJALAN '),
            'cek_plagiasi': ('BUKTI HASIL CEK PLAGIASI '),
            'file_tugas_akhir': ('SOFT FILE TUGAS AKHIR '),
            'sk_diterima': ('SURAT KETERANGAN DITERIMA DARI TEMPAT TUGAS AKHIR '),
            'sk_selesai': ('SURAT KETERANGAN SELESAI DARI TEMPAT TUGAS AKHIR '),
            'lembar_penilaian': ('LEMBAR PENILAIAN (KHUSUS TAM) '),
            'kepemilikan_usaha': ('BUKTI KEPEMILIKAN USAHA (KHUSUS TAW) '),
            'bukti_mou_spk': ('BUKTI MoU ATAU SPK '),
            'ijazah_terakhir': ('BUKTI UJAZAH TERAKHIR '),
            'akte_kelahiran': ('BUKTI AKTE KELAHIRAN '),
            'ktp_kk': ('BUKTI KTP ATAU KK '),
            'foto': ('PAS FOTO HITAM PUTIH (2X3) '),
            'status_validasi_dospem': ('STATUS VALIDASI DOSEN PEMBIMBING '),
            'status_validasi_dospem': ('STATUS VALIDASI KEUANGAN '),
            'status_validasi_dospem': ('STATUS VALIDASI AKADEMIK '),
        }
        
        widgets = {
            'mahasiswa_id': forms.Select({'class':'form-control'}),
            'judul': forms.TextInput({'class':'form-control'}),
            'acc_ujian': forms.FileInput({'class':'form-control'}),
            'bebas_teori': forms.FileInput({'class':'form-control'}),
            'krs': forms.FileInput({'class':'form-control'}),
            'cek_plagiasi': forms.FileInput({'class':'form-control'}),
            'file_tugas_akhir': forms.FileInput({'class':'form-control'}),
            'sk_diterima': forms.FileInput({'class':'form-control'}),
            'sk_selesai': forms.FileInput({'class':'form-control'}),
            'lembar_penilaian': forms.FileInput({'class':'form-control'}),
            'kepemilikan_usaha': forms.FileInput({'class':'form-control'}),
            'bukti_mou_spk': forms.FileInput({'class':'form-control'}),
            'ijazah_terakhir': forms.FileInput({'class':'form-control'}),
            'akte_kelahiran': forms.FileInput({'class':'form-control'}),
            'ktp_kk': forms.FileInput({'class':'form-control'}),
            'foto': forms.FileInput({'class':'form-control'}),
            'status_validasi_dospem': forms.Select({'class':'form-control'}),
            'status_validasi_keuangan': forms.Select({'class':'form-control'}),
            'status_validasi_akademik': forms.Select({'class':'form-control'}),
        }

class FormTugasAkhir(ModelForm):
    class Meta:
        model = Tugasakhir
        fields = [
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
            ]
        
        labels = {
            'mahasiswa_id': ('NOMOR POKOK MAHASISWA '),
            'judul': ('JUDUL TUGAS AKHIR '),
            'acc_ujian': ('BUKTI ACC UJIAN SIDANG '),
            'bebas_teori': ('BUKTI BEBAS TEORI DARI DOSEN PEMBIMBING AKADEMIK '),
            'krs': ('BUKTI KRS PADA SEMESTER BERJALAN '),
            'cek_plagiasi': ('BUKTI HASIL CEK PLAGIASI '),
            'file_tugas_akhir': ('SOFT FILE TUGAS AKHIR '),
            'sk_diterima': ('SURAT KETERANGAN DITERIMA DARI TEMPAT TUGAS AKHIR '),
            'sk_selesai': ('SURAT KETERANGAN SELESAI DARI TEMPAT TUGAS AKHIR '),
            'lembar_penilaian': ('LEMBAR PENILAIAN (KHUSUS TAM) '),
            'kepemilikan_usaha': ('BUKTI KEPEMILIKAN USAHA (KHUSUS TAW) '),
            'bukti_mou_spk': ('BUKTI MoU ATAU SPK '),
            'ijazah_terakhir': ('BUKTI UJAZAH TERAKHIR '),
            'akte_kelahiran': ('BUKTI AKTE KELAHIRAN '),
            'ktp_kk': ('BUKTI KTP ATAU KK '),
            'foto': ('PAS FOTO HITAM PUTIH (2X3) '),
        }
        
        widgets = {
            'mahasiswa_id': forms.Select({'class':'form-control'}),
            'judul': forms.TextInput({'class':'form-control'}),
            'acc_ujian': forms.FileInput({'class':'form-control'}),
            'bebas_teori': forms.FileInput({'class':'form-control'}),
            'krs': forms.FileInput({'class':'form-control'}),
            'cek_plagiasi': forms.FileInput({'class':'form-control'}),
            'file_tugas_akhir': forms.FileInput({'class':'form-control'}),
            'sk_diterima': forms.FileInput({'class':'form-control'}),
            'sk_selesai': forms.FileInput({'class':'form-control'}),
            'lembar_penilaian': forms.FileInput({'class':'form-control'}),
            'kepemilikan_usaha': forms.FileInput({'class':'form-control'}),
            'bukti_mou_spk': forms.FileInput({'class':'form-control'}),
            'ijazah_terakhir': forms.FileInput({'class':'form-control'}),
            'akte_kelahiran': forms.FileInput({'class':'form-control'}),
            'ktp_kk': forms.FileInput({'class':'form-control'}),
            'foto': forms.FileInput({'class':'form-control'}),
        }
        
class FormValidasiDospem(ModelForm):
    class Meta:
        model = Tugasakhir
        fields = [
            'status_validasi_dospem',
            ]
        
        labels = {
            'status_validasi_dospem': ('STATUS VALIDASI DOSEN PEMBIMBING '),
        }
        
        widgets = {
            'status_validasi_dospem': forms.Select({'class':'form-control'}),
        }

class FormValidasiAkademik(ModelForm):
    class Meta:
        model = Tugasakhir
        fields = [
            'status_validasi_akademik',
            ]
        
        labels = {
            'status_validasi_akademik': ('STATUS VALIDASI AKADEMIK '),
        }
        
        widgets = {
            'status_validasi_akademik': forms.Select({'class':'form-control'}),
        }

class FormValidasiKeuangan(ModelForm):
    class Meta:
        model = Tugasakhir
        fields = [
            'status_validasi_keuangan',
            ]
        
        labels = {
            'status_validasi_keuangan': ('STATUS VALIDASI KEUANGAN '),
        }
        
        widgets = {
            'status_validasi_keuangan': forms.Select({'class':'form-control'}),
        }

class StudentForm(forms.Form):  
    file      = forms.FileField() # for creating file input  
    
class FormBeritaAcaraMahasiswa(forms.Form):
    KETERANGAN_CHOICES = [
        ('lulus', 'Lulus'),
        ('tidak_lulus', 'Tidak Lulus')
    ]
    nama_mahasiswa = forms.CharField(
        label='Nama Mahasiswa', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    npm = forms.CharField(
        label='NPM', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    judul_ta = forms.CharField(
        label='Judul Tugas Akhir Penelitian', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    keterangan = forms.ChoiceField(
        label='Keterangan Lulus',
        choices=KETERANGAN_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tanggal = forms.CharField(
        label='Tanggal', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_penguji = forms.CharField(
        label='Nama Penguji', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_pembimbing = forms.CharField(
        label='Nama Pembimbing', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class FormBeritaAcara(forms.Form):
    no_surat = forms.CharField(
        label='Nomor Surat', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_mahasiswa = forms.CharField(
        label='Nama Mahasiswa', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    npm = forms.CharField(
        label='NPM', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jurusan = forms.CharField(
        label='Jurusan', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    judul_ta = forms.CharField(
        label='Judul Tugas Akhir Penelitian', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tanggal = forms.CharField(
        label='Tanggal', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_penguji1 = forms.CharField(
        label='Nama Penguji I', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jabatan_tim1 = forms.CharField(
        label='Jabatan Dalam Tim', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jabatan_akademik1 = forms.CharField(
        label='Jabatan Akademik', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_penguji2 = forms.CharField(
        label='Nama Penguji II', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jabatan_tim2 = forms.CharField(
        label='Jabatan Dalam Tim', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jabatan_akademik2 = forms.CharField(
        label='Jabatan Akademik', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_pembimbing = forms.CharField(
        label='Nama Pembimbing', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nilai = forms.CharField(
        label='Nilai', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
class FormPresensi(forms.Form):
    nama_mahasiswa = forms.CharField(
        label='Nama Mahasiswa', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nim_mahasiswa = forms.CharField(
        label='NIM', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    prodi = forms.CharField(
        label='Program Studi', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    hari_ujian = forms.CharField(
        label='Hari', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tanggal_ujian = forms.DateField(
        label='Tanggal Ujian', 
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control',
            },
            format='%d-%m-%Y'  # Mengatur format output ke 'dd-mm-yyyy'
        ),
        input_formats=['%d-%m-%Y', '%Y-%m-%d']  # Mendukung input dalam format 'dd-mm-yyyy' dan 'yyyy-mm-dd'
    )
    waktu_ujian = forms.CharField(
        label='Pukul', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tempat_ujian = forms.CharField(
        label='Tempat Ujian', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ketua_sidang = forms.CharField(
        label='Ketua Sidang', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_penguji1 = forms.CharField(
        label='Penguji I', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_penguji2 = forms.CharField(
        label='Penguji II', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ketua_jurusan = forms.CharField(
        label='Ketua Jurusan', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
class FormRevisi(forms.Form):
    nama_mahasiswa = forms.CharField(
        label='Nama Mahasiswa', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    npm = forms.CharField(
        label='NPM', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jurusan = forms.CharField(
        label='Jurusan', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    judul_tugas_akhir = forms.CharField(
        label='Judul Tugas Akhir', 
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    penguji1 = forms.CharField(
        label='Penguji I', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    penguji2 = forms.CharField(
        label='Penguji II', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    dosen_pembimbing = forms.CharField(
        label='Dosen Pembimbing Skripsi', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tanggal = forms.CharField(
        label='Tanggal', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    revisi = forms.CharField(
        label='Revisi',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    
class FormYudisium(forms.Form):
    nomor_surat = forms.CharField(
        label='Nomor Surat', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nama_mahasiswa = forms.CharField(
        label='Nama Mahasiswa', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    npm = forms.CharField(
        label='NPM', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jurusan = forms.CharField(
        label='Jurusan', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tanggal = forms.CharField(
        label='Tanggal', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
class FormRekapitulasiPenilaian(forms.Form):
    nama_mahasiswa = forms.CharField(
        label='Nama Mahasiswa', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    npm = forms.CharField(
        label='NPM', 
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    jurusan = forms.CharField(
        label='Jurusan', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ketua_penguji = forms.CharField(
        label='Ketua Penguji', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    anggota = forms.CharField(
        label='Anggota', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tanggal = forms.CharField(
        label='Tanggal', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nilai_perancangan_kegiatan = forms.CharField(
        label='Nilai Perancangan Kegiatan', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nilai_penelitian_lapangan = forms.CharField(
        label='Nilai Penelitian Lapangan', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nilai_laporan_penelitian = forms.CharField(
        label='Nilai Laporan Penelitian', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nilai_seminar_hasil_penelitian = forms.CharField(
        label='Nilai Seminar Hasil Penelitian (Ujian Penelitian)', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nilai_penulisan_publikasi = forms.CharField(
        label='Nilai Penulisan Publikasi Penelitian', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )