from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Pet:
    name: str
    breed: str


@dataclass
class Task:
    name: str
    location: str
    time: datetime
    status: str          # e.g. "pending", "completed", "cancelled"
    description: str
    priority: int = 1    # higher number = higher priority

    def create(self) -> "Task":
        pass

    def edit(self, field: str, value) -> None:
        pass

    def delete(self) -> None:
        pass

    def reschedule(self, new_time: datetime) -> None:
        pass


class Scheduler:
    def __init__(self):
        self.schedule: List[Task] = []
        self.appointments: List[Task] = []

    def book_appointment(self, task: Task) -> None:
        pass

    def prioritize_tasks(self) -> List[Task]:
        pass

    def get_upcoming(self, hours: int) -> List[Task]:
        pass

    def cancel_appointment(self, task: Task) -> None:
        pass


class Owner:
    def __init__(self, name: str, address: str, contact: str):
        self.name: str = name
        self.address: str = address
        self.contact: str = contact
        self.pets: List[Pet] = []
        self.tasks: List[Task] = []
        self.scheduler: Scheduler = Scheduler()

    def do_task(self, task: Task) -> None:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass
