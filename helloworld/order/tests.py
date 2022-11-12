from django.contrib.auth.models import User
from django.test import TestCase
from .models import Order, OrderItem


class OrderTests(TestCase):
    def setUp(self):
        User.objects.create(
            email="emre@gmail.com",
            username="emre",
            password="123"
        )
        user = User.objects.get(
            username="emre"
        )
        Order.objects.create(
            user=user
        )

    def test_order(self):
        user = User.objects.get(username="emre")
        order = Order.objects.get(user=user)
        self.assertEqual(order.user.email, "emre@gmail.com")
