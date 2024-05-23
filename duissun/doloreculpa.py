import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
