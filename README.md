# Yapay Zeka Destekli Kayıp Eşya Eşleştirme Sistemi

**🎥 Proje Demo Videosu:** https://drive.google.com/file/d/136mAj8jA4T3BYrB5yI9hiVeJgDN5S2-b/view?usp=sharing

## 📌 Problem
Kampüs içerisinde veya geniş alanlarda kaybedilen eşyaların, bulan kişiler tarafından geleneksel yöntemlerle (WhatsApp grupları, panolar vb.) asıl sahibine ulaştırılmasının zorluğu ve bu süreçteki zaman kaybı.

## 💡 Çözüm
Kayıp ve bulunan eşya ilanlarının sisteme girilmesi ve Doğal Dil İşleme (NLP) modelleri kullanılarak bu ilanların anlamsal olarak eşleştirilmesi. Böylece kelimeler birebir aynı olmasa bile yapay zeka sayesinde doğru eşyalar birbirini bulabilmektedir.

## 🤖 Yapay Zekâyı Nasıl Kullandık?
**1. Ürün İçindeki Yapay Zeka:** Eşya tanımlarının anlamsal eşleşmesi için Hugging Face üzerinden `sentence-transformers` modelini (açık kaynak) yerel olarak Docker içinde kullandık. Hiçbir harici bulut API'si kullanılmamıştır.
**2. Geliştirme Sürecindeki Yapay Zeka Asistanı:** Kodların yazılması, Docker yapılandırmasının oluşturulması ve hata ayıklama süreçlerinde Gemini yapay zeka asistanından destek aldım. Özellikle "CORS hatalarının çözümü" ve "Backend/Frontend Docker port yönlendirmeleri" gibi konularda spesifik istemler (promptlar) kullanarak çözüm mimarileri ürettim. Asistanın ürettiği şablon kodları, kendi proje yapıma ve şartname gereksinimlerine uygun şekilde manuel olarak düzenleyip entegre ettim.

## 🚀 Çalıştırma Adımları
Proje klasör yapısı (backend/, frontend/ ve kök dizinde docker-compose.yml) şartnameye uygun hazırlanmış ve tamamen Dockerize edilmiştir. Çalıştırmak için proje dizininde terminale şu komutu girmeniz yeterlidir:

```bash
docker-compose up --build