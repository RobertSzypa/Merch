from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QLineEdit,
    QFormLayout,
    QDateEdit
)

from PySide6.QtCore import QDate

from services.data_service import DataService


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.data_service=DataService()

        self.setWindowTitle("System wypożyczeń")
        self.resize(900,500)

        layout=QVBoxLayout()

        title=QLabel("System wypożyczeń")
        layout.addWidget(title)

        self.table=QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(
            [
                "Person",
                "Thing",
                "Rented",
                "Return",
                "Status"
            ]
        )

        layout.addWidget(self.table)

        # refresh btn
        refresh_btn=QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_data)

        layout.addWidget(refresh_btn)

        # add btn
        add_btn = QPushButton("Dodaj")

        add_btn.clicked.connect(
            self.open_add_dialog
        )

        layout.addWidget(add_btn)


        self.setLayout(layout)

        self.load_data()

    def load_data(self):

        data=self.data_service.get_all()

        self.table.setRowCount(len(data))

        for row,item in enumerate(data):

            self.table.setItem(
                row,0,
                QTableWidgetItem(item["person"])
            )

            self.table.setItem(
                row,1,
                QTableWidgetItem(item["thing"])
            )

            self.table.setItem(
                row,2,
                QTableWidgetItem(item["rented"])
            )

            self.table.setItem(
                row,3,
                QTableWidgetItem(item["return"])
            )

            self.table.setItem(
                row,4,
                QTableWidgetItem(item["status"])
            )

    def open_add_dialog(self):

        dialog = AddDialog()

        if dialog.exec():

            data = dialog.get_data()

            self.data_service.add(data)

            self.load_data()

class AddDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nowe wypożyczenie")

        layout = QFormLayout()

        self.person = QLineEdit()
        self.thing = QLineEdit()

        self.rented = QDateEdit()
        self.rented.setDate(QDate.currentDate())

        self.return_date = QDateEdit()
        self.return_date.setDate(QDate.currentDate())

        save_btn = QPushButton("Zapisz")

        save_btn.clicked.connect(self.accept)

        layout.addRow("Person:", self.person)
        layout.addRow("Thing:", self.thing)
        layout.addRow("Rented:", self.rented)
        layout.addRow("Return:", self.return_date)

        layout.addWidget(save_btn)

        self.setLayout(layout)

    def get_data(self):

        return {
            "person": self.person.text(),
            "thing": self.thing.text(),
            "rented":
                self.rented.date().toString("yyyy-MM-dd"),
            "return":
                self.return_date.date().toString("yyyy-MM-dd"),
            "status":"Wypożyczone"
        }