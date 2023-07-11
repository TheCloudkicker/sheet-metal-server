from django.core.management.base import BaseCommand
from ...models import Customer, Job, PurchaseOrder


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Populating database")

        num = Customer.objects.count()
        customer = Customer.objects.create(name=f"Customer {num + 1}")

        jobs = []
        for i in range(20):
            jobs.append(Job(customer=customer, name=f"Job {customer.id}-{i}"))

        Job.objects.bulk_create(jobs)

        purchase_orders = []
        for i in range(20):
            purchase_orders.append(PurchaseOrder(name=f"Purchase Order - {i}"))
        PurchaseOrder.objects.bulk_create(purchase_orders)

        print("********************************************")
        print(f"Customers: {Customer.objects.all().count()}")
        print(f"Jobs: {Job.objects.all().count()}")
        print(f"PurchaseOrders: {PurchaseOrder.objects.all().count()}")
        print("********************************************")
