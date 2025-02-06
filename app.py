import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt

# Dummy user credentials for validation
USER_CREDENTIALS = {
    'user1': 'password123',
    'admin': 'adminpass',
}

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Habit Buddy - Login')
        self.setGeometry(100, 100, 600, 400)
        self.setFixedSize(1200, 800)

        # Background image
        self.background_label = QLabel(self)
        pixmap = QPixmap('background.jpeg')  # Ensure you have 'background.jpg' in the same directory or provide the correct path
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.resize(1200, 800)

        # Transparent overlay widget for form
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet("background-color: rgba(255, 255, 255, 180); border-radius: 15px;")
        self.overlay.setGeometry(100, 50, 400, 300)

        # Title label
        self.title_label = QLabel('Welcome to Habit Buddy!', self.overlay)
        self.title_label.setFont(QFont('Verdana', 12, QFont.Bold))
        self.title_label.setStyleSheet("color: #2E8B57;")  # SeaGreen color
        self.title_label.setAlignment(Qt.AlignCenter)

        # Username label and input
        self.username_label = QLabel('Username:', self.overlay)
        self.username_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        self.username_input = QLineEdit(self.overlay)
        self.username_input.setStyleSheet("padding: 8px; border: 2px solid #2E8B57; border-radius: 8px;")

        # Password label and input
        self.password_label = QLabel('Password:', self.overlay)
        self.password_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        self.password_input = QLineEdit(self.overlay)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("padding: 8px; border: 2px solid #2E8B57; border-radius: 8px;")

        # Login button
        self.login_button = QPushButton('Login', self.overlay)
        self.login_button.setStyleSheet(
            "background-color: #2E8B57; color: white; padding: 12px; border-radius: 8px; font-weight: bold;"
        )
        self.login_button.clicked.connect(self.validate_login)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addSpacing(20)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addSpacing(20)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.overlay.setLayout(layout)

    def validate_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            QMessageBox.information(self, 'Login Successful', f'Welcome, {username}! Ready to build new habits!')
        else:
            QMessageBox.warning(self, 'Login Failed', 'Oops! Invalid username or password.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
