import os
import subprocess
import requests

def jalankan_pylint():
    """Menjalankan pylint pada direktori proyek."""
    try:
        hasil = subprocess.run(
            ['pylint', 'src/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        hasil.check_returncode()  # Menambahkan pengecekan untuk memastikan perintah berhasil
        return hasil.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error menjalankan pylint: {e}"

def buat_github_issue(laporan):
    """Membuat issue di GitHub dengan laporan pylint."""
    github_token = os.getenv('GITHUB_TOKEN')  # Pastikan sudah set env variable GITHUB_TOKEN
    if not github_token:
        print("GITHUB_TOKEN tidak ditemukan.")
        return

    pemilik_repo = "Wafi09"
    nama_repo = "code-review-demo1"
    
    url = f"https://api.github.com/repos/{pemilik_repo}/{nama_repo}/issues"
    
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    data_issue = {
        "title": "Laporan Review Kode Otomatis",
        "body": laporan,
        "labels": ["code review", "automated"]
    }

    try:
        response = requests.post(url, headers=headers, json=data_issue)
        response.raise_for_status()  # Menambahkan pengecekan untuk status code
        print("Issue berhasil dibuat di GitHub.")
    except requests.exceptions.RequestException as e:
        print("Gagal membuat issue:", e)

def main():
    """Fungsi utama untuk menjalankan proses review kode."""
    print("Menjalankan Pylint untuk review kode...")
    laporan_pylint = jalankan_pylint()
    print("Review kode selesai.")
    
    print("Membuat issue di GitHub dengan laporan...")
    buat_github_issue(laporan_pylint)
    print("Selesai!")

if __name__ == "__main__":
    main()
