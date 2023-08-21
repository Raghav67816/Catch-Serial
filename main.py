# Import dependencies
import sys
import serial
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from interface.app_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from utils import (
    read_stylesheet, get_com_port, SetFieldWindow,
    PortReader, export_data
)

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        self.fields_dialog = None
        self.active_ports = None

        self.serial_worker = None
        self.serial_worker_state = False

        # Setup interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.setShortcut("Alt+F4")

        # Window Properties
        self.setWindowTitle("Catch Serial")
        self.setWindowIcon(QIcon("interface/icons/terminal.png"))
        # Apply stylesheet
        self.setStyleSheet(read_stylesheet("config/themes/dark.css"))

        # Bind actions
        self.ui.actionApperance.triggered.connect(self.show_set_field_window)
        self.ui.recordingLoopBtn.clicked.connect(self.handle_start_stop)
        self.ui.actionData_Collection.triggered.connect(self.export_to_file)

        self.set_ports()

    # Set ports
    def set_ports(self):
        self.active_ports = get_com_port()
        for i in range(0, len(self.active_ports)):
            self.ui.portBox.addItem(str(self.active_ports[i]))

    def handle_start_stop(self):
        if self.serial_worker_state == False:
            self.ui.recordingLoopBtn.setText("Stop Recording")
            self.start_reading()

        else:
            self.ui.recordingLoopBtn.setText("Start Recording")
            self.stop_reading()

    def export_to_file(self):
        print(self.ui.terminal.toPlainText())
        data = self.ui.terminal.toPlainText().split("\n")
        export_data(data)

    @Slot()
    def start_reading(self):
        if self.serial_worker is None:
            port = "COM3"  # Replace with the selected port
            baud_rate = self.ui.baudRateInput.text()  # Replace with the selected baud rate
            self.serial_worker = PortReader(port, baud_rate)
            self.serial_worker.data_rec.connect(self.update_text)
            self.serial_worker_state = True
            self.serial_worker.start()


    @Slot()
    def stop_reading(self):
        if self.serial_worker:
            self.serial_worker.stop()
            self.serial_worker.wait()
            self.serial_worker = None

    @Slot(str)
    def update_text(self, data):
        self.ui.terminal.append(data)


    # Show SetFieldsWindow
    def show_set_field_window(self):
        self.fields_dialog = SetFieldWindow()
        self.fields_dialog.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())
