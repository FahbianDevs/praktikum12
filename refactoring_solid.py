import logging
from typing import Protocol

# [Pastikan import logging ada di awal file]

# Konfigurasi dasar: Semua log level INFO ke atas akan ditampilkan
# Format: Waktu - Level - Nama Kelas/Fungsi - Pesan
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
# Tambahkan logger untuk kelas yang akan kita gunakan
LOGGER = logging.getLogger('Checkout')

# Placeholder for IPaymentProcessor
class IPaymentProcessor(Protocol):
    def process(self, order: 'Order') -> bool:
        pass

# Placeholder for INotificationService
class INotificationService(Protocol):
    def send(self, order: 'Order') -> None:
        pass

# Placeholder for Order class
class Order:
    def __init__(self, customer_name: str, total_price: float):
        self.customer_name = customer_name
        self.total_price = total_price
        self.status = "pending"


class CheckoutService:
    """
    Kelas high-level untuk mengkoordinasi proses transaksi pembayaran.

    Kelas ini memisahkan logika pembayaran dan notifikasi (memenuhi SRP).
    """

    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        """
        Menginisialisasi CheckoutService dengan dependensi yang diperlukan.

        Args:
            payment_processor (IPaymentProcessor): Implementasi interface pembayaran.
            notifier (INotificationService): Implementasi interface notifikasi.
        """
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order) -> bool:
        """
        Menjalankan proses checkout dan memvalidasi pembayaran.

        Args:
            order (Order): Objek pesanan yang akan diproses.

        Returns:
            bool: True jika checkout sukses, False jika gagal.
        """
        # Logging alih-alih print()
        LOGGER.info(f"Memulai checkout untuk {order.customer_name}. Total: {order.total_price}")

        payment_success = self.payment_processor.process(order)

        if payment_success:
            order.status = "paid"
            self.notifier.send(order)
            LOGGER.info("Checkout Sukses. Status pesanan: PAID.")
            return True
        else:
            # Gunakan level ERROR/WARNING untuk masalah
            LOGGER.error("Pembayaran gagal. Transaksi dibatalkan.")
            return False

if __name__ == "__main__":
    # Example implementation of the interfaces
    class PaymentProcessor(IPaymentProcessor):
        def process(self, order: Order) -> bool:
            return order.total_price <= 100  # Example logic: approve if total is <= 100

    class NotificationService(INotificationService):
        def send(self, order: Order) -> None:
            LOGGER.info(f"Notifikasi dikirim ke {order.customer_name} untuk pesanan {order.status}.")

    # Create instances of the services
    payment_processor = PaymentProcessor()
    notifier = NotificationService()

    # Create an instance of CheckoutService
    checkout_service = CheckoutService(payment_processor, notifier)

    # Create a sample order
    sample_order = Order(customer_name="John Doe", total_price=50)

    # Run the checkout process
    success = checkout_service.run_checkout(sample_order)

    # Print the result
    print("Checkout berhasil" if success else "Checkout gagal")