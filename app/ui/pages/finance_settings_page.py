from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox
)

class FinanceSettingsPage(QWidget):

    def __init__(self, finance_service):

        super().__init__()

        self.finance = finance_service

        self._setup_ui()


    def _setup_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel(
            "⚙ Configurações Financeiras"
        )

        title.setObjectName(
            "pageTitle"
        )

        main_layout.addWidget(title)

        category_title = QLabel(
            "Categorias"
        )

        main_layout.addWidget(
            category_title
        )

        form_layout = QHBoxLayout()

        self.category_input = QLineEdit()

        self.category_input.setPlaceholderText(
            "Nova categoria"
        )

        self.add_category_button = QPushButton(
            "Adicionar"
        )

        self.delete_category_button = QPushButton(
            "Excluir"
        )

        form_layout.addWidget(
            self.category_input
        )

        form_layout.addWidget(
            self.add_category_button
        )

        form_layout.addWidget(
            self.delete_category_button
        )

        main_layout.addLayout(
            form_layout
        )

        self.category_list = QListWidget()

        main_layout.addWidget(
            self.category_list
        )

        self._load_categories()

        self.add_category_button.clicked.connect(
            self._add_category
        )

        self.delete_category_button.clicked.connect(
            self._delete_category
        )

        self.setLayout(
            main_layout
        )
    
    def _load_categories(self):

        self.category_list.clear()

        self.category_list.addItems(
            self.finance.categories
        )

    def _add_category(self):

        category = self.category_input.text().strip()

        if not category:

            QMessageBox.warning(
                self,
                "Atenção",
                "Informe uma categoria."
            )

            return

        success = self.finance.add_category(
            category
        )

        if not success:

            QMessageBox.warning(
                self,
                "Atenção",
                "Categoria já cadastrada."
            )

            return

        self._load_categories()

        self.category_input.clear()

        QMessageBox.information(
            self,
            "Sucesso",
            "Categoria cadastrada com sucesso."
        )

    def _delete_category(self):

        item = self.category_list.currentItem()

        if not item:
            return

        category = item.text()
        

        self.finance.remove_category(
            category
        )

        self._load_categories()