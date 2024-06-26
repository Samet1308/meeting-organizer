# Meeting Organizer

Meeting Organizer, müşteriler ile yapılacak toplantıların kaydedilebileceği, güncellenebileceği ve silinebileceği bir tek sayfa uygulamasıdır.

## Proje Tanımı

Bu proje, kullanıcıların toplantı bilgilerini yönetebileceği bir web uygulamasıdır. Kullanıcılar toplantı ekleyebilir, güncelleyebilir ve silebilirler. Uygulama, Django framework'ü kullanılarak geliştirilmiştir.

## Özellikler

- Toplantı Kayıt Formu: Kullanıcıların toplantıya ait bilgileri girebilecekleri ara yüz.
- Toplantı Güncelleme Formu: Kullanıcıların toplantı bilgilerini güncelleyebilecekleri ara yüz.
- Toplantı Listesi: Kullanıcıların eklenen toplantıları görüntüleyebilecekleri, düzenleyebilecekleri ve silebilecekleri arayüz.

## Kullanılan Teknolojiler

- Python
- Django
- HTML
- CSS

## Kurulum

1.  git clone https://github.com/kullanici/meeting-organizer.git
    cd meeting-organizer


2. **Gerekli Paketleri Yükleyin**:
    ```
    pip install -r requirements.txt
    ```

3. **Veritabanını Oluşturun**:
    ```bash
    python manage.py migrate
    ```

4. **Sunucuyu Başlatın**:
    ```bash
    python manage.py runserver
    ```

5. **Web Tarayıcınızda Uygulamayı Açın**:
    ```bash
    http://127.0.0.1:8000
    ```
