import requests
from django.conf import settings

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
    response_get = requests.get(f'{url}/{response.json()["id"]}', headers=headers)
    print(response_get.json()['payment_status'])
    return response.json()['url']

