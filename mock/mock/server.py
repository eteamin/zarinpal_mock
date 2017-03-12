from pyws.server import SoapServer
from pyws.functions.register import register

server = SoapServer(
    service_name='zarinpal_mock',
    tns='http://example.com',
    location='http://localhost:9393'
)


@register()
def PaymentRequest(**kwargs):
    # Assuming inputs are valid cause we are not testing zarinpal itself!!!
    return {
        'Authority': 100,
        'Status': 100
    }


@register()
def PaymentVerification(**kwargs):
    return {
        'RefID': 100,
        'Status': 100
    }

