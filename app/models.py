from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_clients():
        return Client.objects.all()

    def update_email(self, email):
        self.email = email
        self.save()

    def update_phone_number(self, phone_number):
        self.phone_number = phone_number
        self.save()

    def update_address(self, address):
        self.address = address
        self.save()

    def get_all_client_orders(self):
        return Order.objects.filter(client=self.id)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def search_products_by_name(name):
        return Product.objects.filter(name__icontains=name)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Заказ клиента {self.client.name} от {self.order_date}"

    def get_products(self):
        return self.products.all()

    def calculate_total_order_amount(self):
        total_amount = sum(product.price * product.quantity for product in self.products.all())
        return total_amount

    @staticmethod
    def get_all_orders():
        return Order.objects.all()

    @staticmethod
    def get_orders_by_client(client):
        return Order.objects.filter(client=client)
