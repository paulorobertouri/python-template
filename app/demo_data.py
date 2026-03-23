from datetime import date

from pydantic import BaseModel


class DemoData(BaseModel):
    id: int
    name: str
    birth_date: date | None = None

    def is_birth_date_today(self):
        if self.birth_date is None:
            return False
        return self.birth_date == date.today()
