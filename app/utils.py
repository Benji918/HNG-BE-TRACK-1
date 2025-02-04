import requests

def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    n = len(digits)
    return sum(d ** n for d in digits)

def get_fun_fact(number):
    try:
        response = requests.get(url=f'http://numbersapi.com/{number}/math')
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return "Could not retrieve fun fact."