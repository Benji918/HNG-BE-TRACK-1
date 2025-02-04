from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .utils import is_armstrong, get_fun_fact



class ClassifyNumAPIView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        number = request.query_params.get('number')

        if not number.isdigit() or not number:
            return Response(status=400, data={'number': number, 'error': True})

        number = int(number)
        properties = ['odd' if number % 2 !=0 else 'even']

        if is_armstrong(number):
            properties.insert(0, 'armstrong')

        response_data = {
            'number': number,
            'is_prime': self.is_prime(number),
            'is_perfect': self.is_perfect(number),
            'properties': properties,
            'digit_sum': sum(int(d) for d in str(number)),
            'fun_fact': get_fun_fact(number)

        }
        return Response(status=200, data=response_data)


    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_perfect(self, num):
        return num == sum(i for i in range(1, num) if num % i == 0)