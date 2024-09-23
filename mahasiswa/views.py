import locale
from django.shortcuts import render, redirect
from mahasiswa.models import *
from mahasiswa.forms import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse  
from mahasiswa.functions.functions import handle_uploaded_file  

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Dibuat! ")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }

        return render(request, 'registration/signup.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request, 'home.html')

# Dosen Pembimbing
def data_dospem(request):
    dospem = DosenPembimbing.objects.all()
    context = {
        'dospem':dospem
    }
    return render(request, 'templates_kaprodi/daftar-dospem.html', context)

def daftar_dospem(request):
    dospem = DosenPembimbing.objects.all()
    context = {
        'dospem':dospem
    }
    return render(request, 'daftar-dospem.html', context)

def tambah_dospem(request):
    if request.POST:
        form = FormDospem(request.POST)
        if form.is_valid():
            form.save()
            message = "Dosen Pembimbing Berhasil ditetapkan"
            form = FormDospem()
            
            context = {
                'form':form,
                'message':message,
            }
            return render(request, 'tambah-dospem.html', context)
    else:
        form = FormDospem()
        
        context = {
            'form':form
        }
    
    return render(request, 'tambah-dospem.html', context)

def ubah_dosen_pembimbing(request, id_dosenpembimbing):
    dosenpembimbing = DosenPembimbing.objects.get(id=id_dosenpembimbing)
    template = 'ubah-data-dospem.html'
    if request.POST:
        form = FormDospem(request.POST, instance=dosenpembimbing)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah!")
            return redirect('ubah_dospem', id_dosenpembimbing=id_dosenpembimbing)
    else:
        form = FormDospem(instance=dosenpembimbing)
        context = {
            'form':form,
            'dosenpembimbing':dosenpembimbing,
        }
    return render(request, template, context)

def hapus_dosen_pembimbing(request, id_dosenpembimbing):
    dosenpembimbing = DosenPembimbing.objects.filter(id=id_dosenpembimbing)
    dosenpembimbing.delete()
    
    return redirect('data_dospem')

# Mahasiswa
def mahasiswa(request):
    mhs = Mahasiswa.objects.all()
    context = {
        'mhs':mhs
    }
    return render(request, 'mahasiswa.html', context)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            message = "Data berhasil disimpan!"
            form = FormMahasiswa()
            
            context = {
                'form':form,
                'message':message,
            }
            return render(request, 'tambah-mahasiswa.html', context)
    else:
        form = FormMahasiswa()
        
        context = {
            'form':form
        }
    
    return render(request, 'tambah-mahasiswa.html', context)


def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah!")
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        context = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, context)

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()
    
    return redirect('mahasiswa')

# Upload TA
def upload(request):
    ta = Tugasakhir.objects.all()
    context = {
        'ta':ta
    }
    return render(request, 'data-upload.html', context)

def upload_syarat(request):
    if request.POST:
        form = FormTugasAkhir(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Data berhasil disimpan!"
            form = FormTugasAkhir()
            
            context = {
                'form':form,
                'message':message,
            }
            return render(request, 'upload.html', context)
    else:
        form = FormTugasAkhir()
        
        documents = Tugasakhir.objects.all()
        context = {
            'form':form,
            'documents':documents,
        }
    
    return render(request, 'upload.html', context)

def ubah_ta(request, id_tugasakhir):
    tugasakhir = Tugasakhir.objects.get(id=id_tugasakhir)
    template = 'ubah-data-upload.html'
    if request.POST:
        form = FormTugasAkhir(request.POST, request.FILES, instance=tugasakhir)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah!")
            return redirect('ubah_tugasakhir', id_tugasakhir=id_tugasakhir)
    else:
        form = FormTugasAkhir(instance=tugasakhir)
        context = {
            'form':form,
            'tugasakhir':tugasakhir,
        }
    return render(request, template, context)

def hapus_ta(request, id_tugasakhir):
    tugasakhir = Tugasakhir.objects.filter(id=id_tugasakhir)
    tugasakhir.delete()
    
    messages.success(request, 'Data berhasil dihapus!')
    return redirect('data_upload')

def detail_tugas_akhir(request, id_tugasakhir):
    tugasakhir = Tugasakhir.objects.get(id=id_tugasakhir)
    context = {
        'tugasakhir':tugasakhir,
    }
    return render(request, 'detail-ta.html', context)

# Jadwal Ujian

def jadwal_ujian(request):
    jdwl = JadwalUjian.objects.all()
    context = {
        'jdwl':jdwl
    }
    return render(request, 'jadwal-ujian-sidang.html', context)

def daftar_jadwal_ujian(request):
    jdwl = JadwalUjian.objects.all()
    context = {
        'jdwl':jdwl
    }
    return render(request, 'templates_kaprodi/jadwal-ujian-sidang.html', context)

def tambah_jadwal_ujian(request):
    if request.POST:
        form = FormJadwalUjian(request.POST)
        if form.is_valid():
            form.save()
            message = "Jadwal Baru Berahasil Ditambahkan"
            form = FormJadwalUjian()
            
            context = {
                'form':form,
                'message':message,
            }
            return render(request, 'tambah-jadwal-ujian.html', context)
    else:
        form = FormJadwalUjian()
        
        context = {
            'form':form
        }
    
    return render(request, 'tambah-jadwal-ujian.html', context)

def ubah_jadwal_ujian(request, id_jadwalujian):
    jadwalujian = JadwalUjian.objects.get(id=id_jadwalujian)
    template = 'ubah-jadwal-ujian.html'
    if request.POST:
        form = FormJadwalUjian(request.POST, instance=jadwalujian)
        if form.is_valid():
            form.save()
            messages.success(request, "Jadwal berhasil diubah!")
            return redirect('ubah_jadwal_ujian', id_jadwalujian=id_jadwalujian)
    else:
        form = FormJadwalUjian(instance=jadwalujian)
        context = {
            'form':form,
            'jadwalujian':jadwalujian,
        }
    return render(request, template, context)

def hapus_jadwal_ujian(request, id_jadwalujian):
    jadwalujian = JadwalUjian.objects.filter(id=id_jadwalujian)
    jadwalujian.delete()
    
    messages.success(request, 'Jadwal berhasil dihapus!')
    return redirect('daftar_jadwal_ujian')

# Validasi

def data_validasi(request):
    data_validasi = Tugasakhir.objects.all()
    context = {
        'data_validasi':data_validasi
    }
    return render(request, 'data-validasi.html', context)

def validasi_dosen_pembimbing(request):
    validasi_dospem = Tugasakhir.objects.all()
    context = {
        'validasi_dospem':validasi_dospem
    }
    return render(request, 'templates_dospem/validasi-dospem.html', context)

def ubah_validasi_dospem(request, id_validasi_dospem):
    validasi_dospem = Tugasakhir.objects.get(id=id_validasi_dospem)
    template = 'templates_dospem/edit-validasi.html'
    if request.POST:
        form = FormValidasiDospem(request.POST, instance=validasi_dospem)
        if form.is_valid():
            form.save()
            messages.success(request, "Validasi Berhasil")
            return redirect('ubah_validasi_dospem', id_validasi_dospem=id_validasi_dospem)
    else:
        form = FormValidasiDospem(instance=validasi_dospem)
        context = {
            'form':form,
            'validasi_dospem':validasi_dospem,
        }
    return render(request, template, context)

def validasi_keuangan(request):
    validasi_keuangan = Tugasakhir.objects.all()
    context = {
        'validasi_keuangan':validasi_keuangan
    }
    return render(request, 'templates_keuangan/validasi-keuangan.html', context)

def ubah_validasi_keuangan(request, id_validasi_keuangan):
    validasi_keuangan = Tugasakhir.objects.get(id=id_validasi_keuangan)
    template = 'templates_keuangan/edit-validasi.html'
    if request.POST:
        form = FormValidasiKeuangan(request.POST, instance=validasi_keuangan)
        if form.is_valid():
            form.save()
            messages.success(request, "Validasi Berhasil")
            return redirect('ubah_validasi_keuangan', id_validasi_keuangan=id_validasi_keuangan)
    else:
        form = FormValidasiKeuangan(instance=validasi_keuangan)
        context = {
            'form':form,
            'validasi_keuangan':validasi_keuangan,
        }
    return render(request, template, context)

def validasi_akademik(request):
    validasiakademik = Tugasakhir.objects.all()
    context = {
        'validasiakademik':validasiakademik
    }
    return render(request, 'templates_akademik/validasi-akademik.html', context)

def detail_validasi_akademik(request, id_validasi_akademik):
    validasiakademik = Tugasakhir.objects.get(id=id_validasi_akademik)
    context = {
        'validasiakademik':validasiakademik,
    }
    return render(request, 'templates_akademik/detail-validasi-akademik.html', context)

def ubah_validasi_akademik(request, id_validasi_akademik):
    validasiakademik = Tugasakhir.objects.get(id=id_validasi_akademik)
    template = 'templates_akademik/edit-validasi.html'
    if request.POST:
        form = FormValidasiAkademik(request.POST, instance=validasiakademik)
        if form.is_valid():
            form.save()
            messages.success(request, "Validasi Berhasil")
            return redirect('ubah_validasi_akademik', id_validasi_akademik=id_validasi_akademik)
    else:
        form = FormValidasiAkademik(instance=validasiakademik)
        context = {
            'form':form,
            'validasiakademik':validasiakademik,
        }
    return render(request, template, context)

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    return render(request, 'bebas-pustaka.html')

@login_required(login_url=settings.LOGIN_URL)
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"bebas-pustaka.html",{'form':student}) 
    
# Form Berita Ujian Mahasiswa
def berita_acara_mahasiswa(request):
    if request.method == 'POST':
        form = FormBeritaAcaraMahasiswa(request.POST)
        if form.is_valid():
            context = {
                'nama_mahasiswa': form.cleaned_data['nama_mahasiswa'],
                'npm': form.cleaned_data['npm'],
                'judul_ta': form.cleaned_data['judul_ta'],
                'keterangan': form.cleaned_data['keterangan'],
                'tanggal': form.cleaned_data['tanggal'],
                'nama_penguji': form.cleaned_data['nama_penguji'],
                'nama_pembimbing': form.cleaned_data['nama_pembimbing'],
            }
            return render(request, 'print_berita_acara_mahasiswa.html', context)
    else:
        form = FormBeritaAcaraMahasiswa()
    return render(request, 'berita_acara_mahasiswa.html', {'form': form})

# Form Berita Ujian
def berita_acara(request):
    if request.method == 'POST':
        form = FormBeritaAcara(request.POST)
        if form.is_valid():
            context = {
                'no_surat': form.cleaned_data['no_surat'],
                'nama_mahasiswa': form.cleaned_data['nama_mahasiswa'],
                'npm': form.cleaned_data['npm'],
                'jurusan': form.cleaned_data['jurusan'],
                'judul_ta': form.cleaned_data['judul_ta'],
                'tanggal': form.cleaned_data['tanggal'],
                'nama_penguji1': form.cleaned_data['nama_penguji1'],
                'jabatan_tim1': form.cleaned_data['jabatan_tim1'],
                'jabatan_akademik1': form.cleaned_data['jabatan_akademik1'],
                'nama_penguji2': form.cleaned_data['nama_penguji2'],
                'jabatan_tim2': form.cleaned_data['jabatan_tim2'],
                'jabatan_akademik2': form.cleaned_data['jabatan_akademik2'],
                'nama_pembimbing': form.cleaned_data['nama_pembimbing'],
                'nilai': form.cleaned_data['nilai'],
            }
            return render(request, 'print_berita_acara.html', context)
    else:
        form = FormBeritaAcara()
    return render(request, 'berita_acara.html', {'form': form})

# Form Presensi Kehadiran
def presensi_kehadiran(request):
    if request.method == 'POST':
        form = FormPresensi(request.POST)
        if form.is_valid():
            context = {
                'nama_mahasiswa': form.cleaned_data['nama_mahasiswa'],
                'nim_mahasiswa': form.cleaned_data['nim_mahasiswa'],
                'prodi': form.cleaned_data['prodi'],
                'hari_ujian': form.cleaned_data['hari_ujian'],
                'tanggal_ujian': form.cleaned_data['tanggal_ujian'],
                'waktu_ujian': form.cleaned_data['waktu_ujian'],
                'tempat_ujian': form.cleaned_data['tempat_ujian'],
                'ketua_sidang': form.cleaned_data['ketua_sidang'],
                'nama_penguji1': form.cleaned_data['nama_penguji1'],
                'nama_penguji2': form.cleaned_data['nama_penguji2'],
                'ketua_jurusan': form.cleaned_data['ketua_jurusan'],
            }
            return render(request, 'print_presensi_kehadiran.html', context)
    else:
        form = FormPresensi()
    return render(request, 'presensi_kehadiran.html', {'form': form})

# Form Lembar Revisi
def lembar_revisi(request):
    if request.method == 'POST':
        form = FormRevisi(request.POST)
        if form.is_valid():
            context = {
                'nama_mahasiswa': form.cleaned_data['nama_mahasiswa'],
                'npm': form.cleaned_data['npm'],
                'jurusan': form.cleaned_data['jurusan'],
                'judul_tugas_akhir': form.cleaned_data['judul_tugas_akhir'],
                'penguji1': form.cleaned_data['penguji1'],
                'penguji2': form.cleaned_data['penguji2'],
                'dosen_pembimbing': form.cleaned_data['dosen_pembimbing'],
                'tanggal': form.cleaned_data['tanggal'],
                'revisi': form.cleaned_data['revisi'],
            }
            return render(request, 'print_lembar_revisi.html', context)
    else:
        form = FormRevisi()
    return render(request, 'lembar_revisi.html', {'form': form})

# Form Lembar yudisium
def lembar_yudisium(request):
    if request.method == 'POST':
        form = FormYudisium(request.POST)
        if form.is_valid():
            context = {
                'nomor_surat': form.cleaned_data['nomor_surat'],
                'nama_mahasiswa': form.cleaned_data['nama_mahasiswa'],
                'npm': form.cleaned_data['npm'],
                'jurusan': form.cleaned_data['jurusan'],
                'tanggal': form.cleaned_data['tanggal'],
            }
            return render(request, 'print_lembar_yudisium.html', context)
    else:
        form = FormYudisium()
    return render(request, 'lembar_yudisium.html', {'form': form})

# Form Lembar Rekapitulasi Penilaian
def lembar_rekapitulasi(request):
    if request.method == 'POST':
        form = FormRekapitulasiPenilaian(request.POST)
        if form.is_valid():
            # Dapatkan nilai dari form
            nilai_perancangan_kegiatan = float(form.cleaned_data['nilai_perancangan_kegiatan'])
            nilai_penelitian_lapangan = float(form.cleaned_data['nilai_penelitian_lapangan'])
            nilai_laporan_penelitian = float(form.cleaned_data['nilai_laporan_penelitian'])
            nilai_seminar_hasil_penelitian = float(form.cleaned_data['nilai_seminar_hasil_penelitian'])
            nilai_penulisan_publikasi = float(form.cleaned_data['nilai_penulisan_publikasi'])
            
            # Hitung nilai huruf
            grade_perancangan_kegiatan = show_evaluation_result(nilai_perancangan_kegiatan)
            grade_penelitian_lapangan = show_evaluation_result(nilai_penelitian_lapangan)
            grade_laporan_penelitian = show_evaluation_result(nilai_laporan_penelitian)
            grade_seminar_hasil_penelitian = show_evaluation_result(nilai_seminar_hasil_penelitian)
            grade_penulisan_publikasi = show_evaluation_result(nilai_penulisan_publikasi)
            
            context = {
                'nama_mahasiswa': form.cleaned_data['nama_mahasiswa'],
                'npm': form.cleaned_data['npm'],
                'jurusan': form.cleaned_data['jurusan'],
                'ketua_penguji': form.cleaned_data['ketua_penguji'],
                'anggota': form.cleaned_data['anggota'],
                'tanggal': form.cleaned_data['tanggal'],
                'nilai_perancangan_kegiatan': nilai_perancangan_kegiatan,
                'nilai_penelitian_lapangan': nilai_penelitian_lapangan,
                'nilai_laporan_penelitian': nilai_laporan_penelitian,
                'nilai_seminar_hasil_penelitian': nilai_seminar_hasil_penelitian,
                'nilai_penulisan_publikasi': nilai_penulisan_publikasi,
                'grade_perancangan_kegiatan': grade_perancangan_kegiatan,
                'grade_penelitian_lapangan': grade_penelitian_lapangan,
                'grade_laporan_penelitian': grade_laporan_penelitian,
                'grade_seminar_hasil_penelitian': grade_seminar_hasil_penelitian,
                'grade_penulisan_publikasi': grade_penulisan_publikasi
            }
            return render(request, 'print_rekapitulasi_penilaian.html', context)
    else:
        form = FormRekapitulasiPenilaian()
    return render(request, 'rekapitulasi_penilaian.html', {'form': form})

def show_evaluation_result(nilai):
    nilai = float(nilai)
    if nilai >= 85:
        return 'A'
    elif nilai >= 82.5:
        return 'A-'
    elif nilai >= 80:
        return 'AB'
    elif nilai >= 77.5:
        return 'B+'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 72.5:
        return 'B-'
    elif nilai >= 70:
        return 'BC'
    elif nilai >= 67.5:
        return 'C+'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 60:
        return 'C-'
    elif nilai >= 55:
        return 'CD'
    elif nilai >= 50:
        return 'D+'
    elif nilai >= 45:
        return 'D'
    elif nilai >= 40:
        return 'D-'
    else:
        return 'E'