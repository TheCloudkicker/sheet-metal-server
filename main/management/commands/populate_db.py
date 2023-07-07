from django.core.management.base import BaseCommand
from ...models.customer import Customer
from ...models.job import Job


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Populating database")

        customer1 = Customer.objects.create(name="Customer 1")
        customer2 = Customer.objects.create(name="Customer 2")

        jobs = []
        for customer in [customer1, customer2]:
            for i in range(20):
                jobs.append(Job(customer=customer, name=f"Job {customer.id}-{i}"))

        Job.objects.bulk_create(jobs)

        print("********************************************")
        print(f"Customers: {Customer.objects.all().count()}")
        print(f"Jobs: {Job.objects.all().count()}")
        print("********************************************")
