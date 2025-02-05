from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .utils import digit_sum,is_armstrong,is_perfect,is_prime


class ClassifyNumberView(APIView):
  def get(self,request):
    number_param = request.query_params.get('number')
    if not number_param:
      return Response({"number":None,"error":True},status=status.HTTP_400_BAD_REQUEST)
    try:
      number = int(number_param)
    except ValueError:
      return Response({"number":number_param,"error":True},status=status.HTTP_400_BAD_REQUEST)
    properties =[]
    if is_armstrong(number):
      properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")
    try:
      response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=3)
      fun_fact = response.json().get("text","") if response.ok else ""
    except requests.RequestException:
      fun_fact=""
    
    return Response({
      "number":number,
      "is_prime": is_prime(number),
      "is_perfect": is_perfect(number),
      "properties": properties,
      "digit_sum":digit_sum(number),
      "fun_fact": fun_fact,
    })