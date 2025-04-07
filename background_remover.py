import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from rembg import remove
import os

class BGRemoverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arka Plan Kaldırıcı")
        self.setGeometry(100, 100, 300, 150)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Bir görsel seçin:\nArka plan otomatik olarak kaldırılacak", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Görsel Seç", self)
        self.button.clicked.connect(self.select_image)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Seç", "", "Görseller (*.png *.jpg *.jpeg)")
        if file_path:
            try:
                with open(file_path, "rb") as f:
                    input_data = f.read()
                    output_data = remove(input_data)

                output_name = os.path.splitext(os.path.basename(file_path))[0] + "_no_bg.png"
                output_path = os.path.join(os.path.dirname(file_path), output_name)

                with open(output_path, "wb") as out:
                    out.write(output_data)

                QMessageBox.information(self, "Başarılı", f"Arka plan kaldırıldı:\n{output_path}")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Hata oluştu:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BGRemoverApp()
    window.show()
    sys.exit(app.exec_())
