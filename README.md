# code-review-demo

Proyek sederhana untuk mendemonstrasikan penggunaan Pylint sebagai alat Automated Code Review dalam proyek Python.

## Struktur Folder

```
code-review-demo/
├── src/
│   └── main.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── code-review.yml
└── README.md
```

## Cara Menjalankan Pylint Secara Lokal

```bash
pip install -r requirements.txt
pylint src/
```

## Integrasi GitHub Actions

File `code-review.yml` akan menjalankan Pylint setiap kali ada push atau pull request ke repository ini.
