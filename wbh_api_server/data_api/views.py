from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET'])
def coord_tester(request):
    if request.method == 'GET':
        # GET 요청에서 lat와 lng 값을 가져옵니다.
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')

        # lat와 lng 값이 제대로 전달되었는지 확인합니다.
        if lat is None or lng is None:
            # lat 또는 lng 값이 누락된 경우에는 오류 응답을 반환합니다.
            return JsonResponse({'error': 'Latitude and longitude parameters are required.'}, status=400)

        # 여기서는 간단히 예시로 받은 좌표 값을 그대로 반환합니다.
        response_data = {
            'latitude': lat,
            'longitude': lng,
            'message': 'Received latitude and longitude values successfully.'
        }
        return JsonResponse(response_data)
    else:
        # GET 요청이 아닌 경우에는 오류 응답을 반환합니다.
        return JsonResponse({'error': 'Only GET method is allowed.'}, status=405)

