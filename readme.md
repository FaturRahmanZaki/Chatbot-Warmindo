# 🤖 Chatbot Warmindo

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/)

> Asisten virtual cerdas untuk Warung Makan Indomie (Warmindo) yang membantu pelanggan dengan pemesanan dan informasi menu menggunakan Natural Language Processing.

![Warmindo Chatbot Demo](./assets/demo.gif)

## ✨ Fitur Utama

- 🧠 **Natural Language Understanding (NLU)**
  - Pemahaman konteks percakapan
  - Deteksi intent otomatis
  - Dukungan Bahasa Indonesia
  
- 💬 **Kemampuan Percakapan**
  - Respon cerdas dan kontekstual
  - Informasi menu dan harga
  - Bantuan pemesanan
  - FAQ otomatis

- 🌐 **Antarmuka Web Modern**
  - Desain responsi
  - Tampilan mobile-friendly

## 🚀 Quickstart

### Prasyarat

```bash
# Python 3.8 atau lebih tinggi
python --version

# Install dependensi
pip install -r requirements.txt
```

### Instalasi

1. Clone repositori
```bash
git clone https://github.com/FaturRahmanZaki/Chatbot-Warmindo
cd chatbot-warmindo
```

2. Setup environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

3. Install dependensi
```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi
```bash
python app.py
```

5. Buka browser dan akses `http://localhost:5000`

## 🏗️ Arsitektur Sistem

```mermaid
graph LR
    A[User Input] --> B[Flask Server]
    B --> C[NLP Processor]
    C --> D[TensorFlow Model]
    D --> E[Intent Classifier]
    E --> F[Response Generator]
    F --> B
    B --> G[User Response]
```

## 📁 Struktur Proyek

```
chatbot-warmindo/
├── assets/
│   ├── demo.gif
├── dataset/
│   ├── data.json
│   ├── classes.pkl
│   ├── chatbot_model.h5
│   ├── model.ipynb
│   └── words.pkl
├── templates/
│   └── index.html
├── app..py
└── README.md
```

## 🛠️ Teknologi yang Digunakan

- **Backend**
  - [Flask](https://flask.palletsprojects.com/) - Web framework
  - [TensorFlow](https://www.tensorflow.org/) - Machine learning
  - [NLTK](https://www.nltk.org/) - Natural language processing
  - [NumPy](https://numpy.org/) - Komputasi numerik

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - [Socket.IO](https://socket.io/) - Real-time communication

## 💡 Penggunaan

### Contoh Interaksi

```python
# Inisialisasi chatbot
from app.models.chatbot_model import WarmindoBot

bot = WarmindoBot()

# Contoh penggunaan
response = bot.get_response("Berapa harga mie goreng?")
print(response)
# Output: "Mie goreng kami dibanderol dengan harga Rp12.000"
```

### API Endpoints

| Endpoint | Metode | Deskripsi |
|----------|--------|-----------|
| `/` | GET | Halaman utama chatbot |
| `/api/chat` | POST | Endpoint untuk menerima pesan |
| `/api/menu` | GET | Mendapatkan daftar menu |

## 🧪 Testing

```bash
# Menjalankan unit tests
python -m pytest tests/

# Menjalankan dengan coverage report
pytest --cov=app tests/
```

## 📝 Konfigurasi

Salin `.env.example` ke `.env` dan sesuaikan:

```env
FLASK_ENV=development
DEBUG=True
SECRET_KEY=your-secret-key
MODEL_PATH=path/to/model
```

## 🔄 Workflow Pengembangan

1. Fork repositori
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request



## 🤝 Kontribusi

Kontribusi membuat komunitas open source menjadi tempat yang luar biasa untuk belajar, menginspirasi, dan berkreasi. Setiap kontribusi yang Anda berikan **sangat dihargai**.

1. Fork proyek ini
2. Buat branch fitur Anda
3. Commit perubahan Anda
4. Push ke branch
5. Buka Pull Request

Lihat [panduan kontribusi](./CONTRIBUTING.md) untuk detail lebih lanjut.

## 📄 Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat [LICENSE](./LICENSE) untuk informasi lebih lanjut.


## 📬 Kontak

Fatur Rahman Zaki - [@ftrrahmanzk](https://x.com/FaturZaki) - email@example.com

Project Link: [https://github.com/FaturRahmanZaki/Chatbot-Warmindo](https://github.com/FaturRahmanZaki/Chatbot-Warmindo)

## 🙏 Pengakuan

- [Flask Documentation](https://flask.palletsprojects.com/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [NLTK Documentation](https://www.nltk.org/)

---

⭐️ Star repo ini jika membantu proyek Anda!
