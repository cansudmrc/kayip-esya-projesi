# Yapay Zeka Destekli Kayıp Eşya Eşleştirme Sistemi

Merhabalar! Bu proje, kaybedilen eşyaların, yapay zeka metin analiz modelleri kullanılarak bulunan eşyalarla eşleştirilmesini sağlamak amacıyla geliştirilmiştir. 

Projeyi geliştirirken ana odak noktam; sistemin sorunsuz çalışması, şartname kurallarına birebir uyması ve Docker ile herkesin tek tıkla çalıştırabileceği bir yapıda olmasıydı.

## 🛠️ Kullanılan Teknolojiler
- **Yapay Zeka:** `sentence-transformers` (Eşya tanımlarını anlamsal olarak karşılaştırmak için)
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, Vanilla JavaScript, Nginx
- **Altyapı:** Docker & Docker Compose

## ✅ Şartname Uygunluk Kontrol Listesi
Proje, yarışma şartnamesindeki teknik gereksinimlere tam uygun şekilde paketlenmiştir:

- **1. Konteyner Mimarisi:** Proje tamamen Dockerize edilmiştir. `docker-compose.yml` üzerinden hem frontend hem backend ayağa kalkmaktadır.
- **2. Port Yönlendirmeleri:** Frontend (Arayüz) `http://localhost:3000`, Backend (API) `http://localhost:8000` portunda çalışmaktadır.
- **3. Health Check (Sağlık Kontrolü):** Sistemin API'yi test edebilmesi için `http://localhost:8000/health` uç noktası oluşturulmuş ve aktiftir.
- **4. CORS Güvenliği:** Backend tarafında CORS ayarları yapılmış, sadece frontend'in çalıştığı `http://localhost:3000` adresine izin verilmiştir.

## 🚀 Projeyi Nasıl Çalıştırabilirsiniz?

Bilgisayarınızda Docker Desktop'ın açık olduğundan emin olun. Ardından terminalde proje dizinindeyken şu komutu çalıştırmanız yeterlidir:

```bash
docker compose up --build