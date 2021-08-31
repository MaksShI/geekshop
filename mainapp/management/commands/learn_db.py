from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from datetime import timedelta
from django.db import connection
from django.db.models import Q, F, When
from adminapp.views import db_profile_by_type
from ordersapp.models import OrderItem
from django.db.models import IntegerField
from django.db.models import F, When, Case, DecimalField, IntegerField
from datetime import timedelta

class Command(BaseCommand):
    def handle(self, *args, **options):
        action_1 = 1
        action_2 = 2
        action_3 = 3

        action_1_time_delta = timedelta(hours=12)
        action_2_time_delta = timedelta(days=1)

        action_1_discount = 0.3
        action_2_discount = 0.15
        action_3_discount = 0.05

        action_1_condition = Q(order__updated__lte=F('created') + action_1_time_delta)
        action_2_condition = Q(order__updated__lte=F('created') + action_2_time_delta) & Q(order__updated__lte=F('created') + action_1_time_delta)

        action_3_condition = Q(order__updated__gt=F('created') + action_2_time_delta)

        action_1_order = When(action_1_condition, then=action_1)
        action_2_order = When(action_2_condition, then=action_2)
        action_3_order = When(action_3_condition, then=action_3)

        action_1_price = When(action_1_condition, then=F('product__price') * F('quantity') * action_1_discount)
        action_2_price = When(action_2_condition, then=F('product__price') * F('quantity') * action_2_discount)
        action_3_price = When(action_3_condition, then=F('product__price') * F('quantity') * action_3_discount)

        order_item_list = OrderItem.objects.annotate(
            action_order=Case(
                action_1_order,
                action_2_order,
                action_3_order,
                output_field=IntegerField()
            )
        ).annotate(
            total_price=Case(
                action_1_price,
                action_2_price,
                action_3_price,
                output_field=DecimalField()
            )
        ).order_by('action_order', 'total_price').select_related()

        for order_item in order_item_list:
            print(f'{order_item.action_order:2}: order #: {order_item.pk:4}: '
                  f'product: {order_item.product.name:20}: discount: {order_item.total_price:6.2f}'
                  f'{order_item.order.update - order_item.order.created}')

