## 🖼️ Background Remover (Arka Plan Temizleyici)

Basit, modern ve kullanımı kolay bir masaüstü uygulaması.  
Görsellerin arka planını tek tıkla kaldırır ve `.png` formatında çıktı verir.

---

### ⚙️ Özellikler

- `.jpg`, `.jpeg`, `.png` desteği
- Çıktı her zaman **şeffaf arka planlı `.png`**
- Basit ve modern PyQt5 arayüzü
- **Lokalde çalışır**, internet gerekmez
- `rembg` motoru ile yüksek kaliteli arka plan silme

---

### 🚀 Nasıl Kullanılır?

1. Uygulamayı aç
2. "Görsel Seç" butonuna tıkla
3. Arka plan otomatik kaldırılır
4. Aynı klasöre `*_no_bg.png` dosyası olarak kaydedilir

---

### 🛠️ Kurulum (Geliştiriciler için)

```bash
pip install PyQt5 rembg pillow
```

### Çalıştır:

```bash
python background_remover.py
```

---

### 🔨 .EXE Oluşturmak için:

```bash
pyinstaller --onefile --noconsole --hidden-import PyQt5.sip background_remover.py
```

Ya da daha hızlı açılması için:

```bash
pyinstaller --onedir --noconsole --hidden-import PyQt5.sip background_remover.py
```

---

### 📁 Örnek Çıktı

Girdi: `profil.jpg`  
Çıktı: `profil_no_bg.png` (şeffaf arka planlı)

---

### 📌 Gereksinimler

- Python 3.8+
- rembg
- PyQt5
- Pillow
