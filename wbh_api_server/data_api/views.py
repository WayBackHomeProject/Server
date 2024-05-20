from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CCTV, ConvenienceStore, PoliceStation
import math

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


@api_view(['GET'])
def cctv_coordinates_in_radius(request):
    """
    현재 좌표(lat, lng)을 기반으로 반경 5km 내의 cctv 좌표를 
    CCTV모델(data_api_cctv 테이블)에서 찾아서 조건에 일치하는 레이블들을
    json 형식으로 반환하는 함수
    """
    try:
        # Get latitude and longitude from request parameters
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        radius_km = float(request.GET.get('radius_km'))
    except (TypeError, ValueError):
        return Response({'error': 'Invalid or missing lat/lng parameters'}, status=400)
    
    

    # Retrieve all CCTV records
    cctvs = CCTV.objects.all()
    results = []

    # Filter CCTV coordinates within the radius
    for cctv in cctvs:
        distance = haversine(lat, lng, cctv.latitude, cctv.longitude)
        if distance <= radius_km:
            results.append({
                'area_code': cctv.area_code,
                'number': cctv.number,
                'managing_agency': cctv.managing_agency,
                'address_road': cctv.address_road,
                'address_jibun': cctv.address_jibun,
                'purpose': cctv.purpose,
                'camera_count': cctv.camera_count,
                'resolution': cctv.resolution,
                'direction_info': cctv.direction_info,
                'retention_period': cctv.retention_period,
                'installation_date': cctv.installation_date,
                'managing_agency_phone': cctv.managing_agency_phone,
                'latitude': cctv.latitude,
                'longitude': cctv.longitude,
                'data_standard_date': cctv.data_standard_date,
            })

    return Response(results)

@api_view(['GET'])
def conveniencestore_coordinates_in_radius(request):
    """
    현재 좌표(lat, lng)을 기반으로 반경 5km 내의 cctv 좌표를 
    ConvenienceStore모델(data_api_convenience_store 테이블)에서 찾아서 조건에 일치하는 레이블들을
    json 형식으로 반환하는 함수
    """
    try:
        # Get latitude and longitude from request parameters
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        radius_km = float(request.GET.get('radius_km'))
    except (TypeError, ValueError):
        return Response({'error': 'Invalid or missing lat/lng parameters'}, status=400)
    
    

    # Retrieve all CCTV records
    convenience_stores = ConvenienceStore.objects.all()
    results = []

    # Filter CCTV coordinates within the radius
    for store in convenience_stores:
        distance = haversine(lat, lng, store.latitude, store.longitude)
        if distance <= radius_km:
            results.append({
                'type': store.type,
                'sr_nm' : store.sr_nm,
                'adres': store.adres,
                'tel_no': store.tel_no,
                'latitude': store.latitude,
                'longitude': store.longitude,
                'detail_adr': store.detail_adr,
                'sigungu' : store.sigungu,
                'sido' : store.sido,
                'umd' : store.umd
            })

    return Response(results)


@api_view(['GET'])
def policestation_coordinates_in_radius(request):
    """
    현재 좌표(lat, lng)을 기반으로 반경 5km 내의 cctv 좌표를 
    ConvenienceStore모델(data_api_convenience_store 테이블)에서 찾아서 조건에 일치하는 레이블들을
    json 형식으로 반환하는 함수
    """
    try:
        # Get latitude and longitude from request parameters
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        radius_km = float(request.GET.get('radius_km'))
    except (TypeError, ValueError):
        return Response({'error': 'Invalid or missing lat/lng parameters'}, status=400)
    
    

    # Retrieve all CCTV records
    police_stations = PoliceStation.objects.all()
    results = []

    # Filter CCTV coordinates within the radius
    for station in police_stations:
        distance = haversine(lat, lng, station.latitude, station.longitude)
        if distance <= radius_km:
            results.append({
                'number': station.type,
                'sido' : station.sido,
                'policestation': station.policestation,
                'department': station.department,
                'type' : station.type,
                'tel_no': station.tel_no,
                'address' : station.address,
                'latitude': station.latitude,
                'longitude': station.longitude,
            })

    return Response(results)




def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
    r = 6371 # Radius of earth in kilometers
    return c * r
