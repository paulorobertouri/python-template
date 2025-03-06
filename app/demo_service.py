from typing import Optional

from app.demo_data import DemoData


class DemoService:
    def __init__(self) -> None:
        self.repository: list[DemoData] = []

    def add_data(self, data: DemoData) -> None:
        self.repository.append(data)

    def get_data(self, id: int) -> Optional[DemoData]:
        for data in self.repository:
            if data.id == id:
                return data
        return None

    def get_data_birth_date_today(self):
        return [data for data in self.repository if data.is_birth_date_today()]
