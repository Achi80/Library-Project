from ninja import NinjaAPI
from .models import Book, Customer, Worker
from .schemas import BookIn, BookOut, CustomerIn, CustomerOut, WorkerIn, WorkerOut
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.get("/books", response=list[BookOut])
def list_books(request):
    return Book.objects.all()

@api.post("/books", response=BookOut)
def create_book(request, data: BookIn):
    return Book.objects.create(**data.dict())

@api.get("/customers", response=list[CustomerOut])
def list_customers(request):
    return Customer.objects.all()

@api.post("/customers", response=CustomerOut)
def create_customer(request, data: CustomerIn):
    return Customer.objects.create(**data.dict())

@api.get("/workers", response=list[WorkerOut])
def list_workers(request):
    return Worker.objects.all()

@api.post("/workers", response=WorkerOut)
def create_worker(request, data: WorkerIn):
    return Worker.objects.create(**data.dict())