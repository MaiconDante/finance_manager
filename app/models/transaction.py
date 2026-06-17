from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    date: date
    description: str
    value: float
    category: str
    transaction_type: str
    payment_method: str


@dataclass
class Transaction:

    date: date

    description: str

    value: float

    category: str

    transaction_type: str

    payment_method: str

    id: int = None