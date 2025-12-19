# Refactoring SOLID Principles

## Deskripsi
Proyek ini adalah implementasi sederhana dari prinsip SOLID dalam Python, dengan fokus pada pemisahan tanggung jawab (Single Responsibility Principle) dan penggunaan dependency injection. Kode ini mensimulasikan proses checkout untuk sebuah pesanan, termasuk validasi pembayaran dan pengiriman notifikasi.

## Struktur Kode
- **`Order`**: Kelas yang merepresentasikan pesanan, dengan atribut seperti nama pelanggan, total harga, dan status.
- **`IPaymentProcessor`**: Interface untuk memproses pembayaran.
- **`INotificationService`**: Interface untuk mengirim notifikasi.
- **`CheckoutService`**: Kelas utama yang mengkoordinasikan proses checkout, memisahkan logika pembayaran dan notifikasi.

## Fitur
1. **Logging**: 
   - Menggunakan modul `logging` untuk mencatat informasi proses checkout.
   - Log mencakup level `INFO` untuk keberhasilan dan `ERROR` untuk kegagalan.
2. **Dependency Injection**:
   - `CheckoutService` menerima `IPaymentProcessor` dan `INotificationService` sebagai dependensi, memungkinkan fleksibilitas dalam implementasi.
3. **Contoh Implementasi**:
   - `PaymentProcessor`: Implementasi sederhana dari `IPaymentProcessor` yang menyetujui pembayaran jika total harga ≤ 100.
   - `NotificationService`: Implementasi sederhana dari `INotificationService` yang mencatat pengiriman notifikasi.

## Cara Kerja
1. **Proses Checkout**:
   - Membuat instance `CheckoutService` dengan implementasi `PaymentProcessor` dan `NotificationService`.
   - Membuat objek `Order` dengan nama pelanggan dan total harga.
   - Menjalankan metode `run_checkout` untuk memproses pesanan.
2. **Hasil**:
   - Jika pembayaran berhasil, status pesanan diubah menjadi "paid" dan notifikasi dikirim.
   - Jika pembayaran gagal, log error dicatat.

## Contoh Penggunaan
Kode berikut menunjukkan cara menjalankan proses checkout:

```python
# Membuat instance layanan
payment_processor = PaymentProcessor()
notifier = NotificationService()

# Membuat instance CheckoutService
checkout_service = CheckoutService(payment_processor, notifier)

# Membuat pesanan contoh
sample_order = Order(customer_name="John Doe", total_price=50)

# Menjalankan proses checkout
success = checkout_service.run_checkout(sample_order)

# Menampilkan hasil
print("Checkout berhasil" if success else "Checkout gagal")
```

## Prinsip SOLID yang Diterapkan
1. **Single Responsibility Principle (SRP)**:
   - `CheckoutService` hanya bertanggung jawab untuk mengkoordinasikan proses checkout.
   - Logika pembayaran dan notifikasi dipisahkan ke dalam interface masing-masing.
2. **Dependency Inversion Principle (DIP)**:
   - `CheckoutService` bergantung pada abstraksi (`IPaymentProcessor` dan `INotificationService`), bukan implementasi konkret.

## Log Output
Berikut adalah contoh log output dari proses checkout:

```
2025-12-19 10:00:00 - INFO - Checkout - Memulai checkout untuk John Doe. Total: 50
2025-12-19 10:00:01 - INFO - Checkout - Notifikasi dikirim ke John Doe untuk pesanan paid.
2025-12-19 10:00:02 - INFO - Checkout - Checkout Sukses. Status pesanan: PAID.
```

## Kesimpulan
Kode ini menunjukkan bagaimana prinsip SOLID dapat diterapkan untuk membuat kode yang modular, mudah diuji, dan fleksibel. Dengan memisahkan tanggung jawab dan menggunakan dependency injection, kode menjadi lebih mudah untuk diperluas dan dirawat.