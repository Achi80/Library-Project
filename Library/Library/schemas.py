from ninja import Schema

class BookIn(Schema):
    title: str
    author: str
    year: int

class BookOut(BookIn):
    id: int

class CustomerIn(Schema):
    name: str
    email: str

class CustomerOut(CustomerIn):
    id: int

class WorkerIn(Schema):
    name: str
    position: str

class WorkerOut(WorkerIn):
    id: int