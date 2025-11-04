import mercadopago

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}
def create_payment():
    sdk = mercadopago.SDK("APP_USR-6265344500157766-110113-472cd137d3e3d5e7dbde8c8e7c17dfec-2959473393")
    payment_data = {
        "items": [
        {
            "id": "1",
            "title": "Ebook",
            "quantity": 1,
           "currency_id": "BRL",
            "unit_price": 2.99,
        }
        ],
        "back_urls":{
            "success": "https://120.0.0.1:5000/download.html",
            "failure": "https://120.0.0.1:5000/compraerrada.html",
        },
        "auto_return": "all"
}
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link = payment["init_point"]
    print(payment)
    return link
    
