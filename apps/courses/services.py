import requests
import schedule

from django.conf import settings

from apps.courses.models import Payment


def create_product(product):
    url = 'https://api.stripe.com/v1/products'
    headers = {
        'Authorization': f'Bearer {settings.STRIPE_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'name': f'Course: {product}',
    }
    response = requests.post(url, headers=headers, params=params)
    return response.json()['id']


def create_price(product, price):
    url = 'https://api.stripe.com/v1/prices'
    headers = {
        'Authorization': f'Bearer {settings.STRIPE_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'currency': 'USD',
        'product': create_product(product),
        'unit_amount': price
    }
    response = requests.post(url, headers=headers, params=params)
    return response.json()['id']


def get_pay_link(obj):
    url = 'https://api.stripe.com/v1/checkout/sessions'
    headers = {
        'Authorization': f'Bearer {settings.STRIPE_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'line_items[0][price]': create_price(obj.course_name, obj.price),
        'line_items[0][quantity]': 1,
        'mode': 'payment',
        'success_url': 'https://example.com/success',
    }
    response = requests.post(url, headers=headers, params=params)
    return response.json()


def get_payment_status(payment_id):
    url = f'https://api.stripe.com/v1/checkout/sessions/{payment_id}'
    headers = {
        'Authorization': f'Bearer {settings.STRIPE_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json()['status']
    except KeyError:
        print(f'There is no payment with id {payment_id}')
        return None


def create_payment_object(obj, data):
    pay_data = {
        'user': obj.user,
        'course': obj.course,
        'sum': data['amount_total'],
        'method': 'card',
        'payment_id': data['id'],
        'payment_status': get_payment_status(data['id'])
    }

    Payment.objects.create(**pay_data)


def check_payment_status():
    payments = Payment.objects.all()
    for payment in payments:
        status = get_payment_status(payment.payment_id)
        payment.payment_status = status
        payment.save()
        print(status)


def run_schedule():
    """Run a schedule"""
    schedule.every(1).hours.do(check_payment_status)
