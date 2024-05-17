from django.db import models

class CCTV(models.Model):
    '''
    행정지역명 번호	관리기관명	소재지도로명주소	소재지지번주소	설치목적구분	카메라대수	카메라화소수	촬영방면정보	보관일수	설치연월	관리기관전화번호	WGS84위도	WGS84경도	데이터기준일자
    '''
    area_code = models.CharField(max_length=100)  # 행정지역명
    number = models.IntegerField()  # 번호
    managing_agency = models.CharField(max_length=100)  # 관리기관명
    address_road = models.CharField(max_length=200)  # 소재지도로명주소
    address_jibun = models.CharField(max_length=200, null=True, blank=True)  # 소재지지번주소
    purpose = models.CharField(max_length=100)  # 설치목적구분
    camera_count = models.IntegerField()  # 카메라대수
    resolution = models.CharField(max_length=100, null=True, blank=True)  # 카메라화소수
    direction_info = models.CharField(max_length=200, null=True, blank=True)  # 촬영방면정보
    retention_period = models.IntegerField(null=True, blank=True)  # 보관일수
    installation_date = models.DateField(null=True, blank=True)  # 설치연월
    managing_agency_phone = models.CharField(max_length=20)  # 관리기관전화번호
    latitude = models.FloatField()  # WGS84위도
    longitude = models.FloatField()  # WGS84경도
    data_standard_date = models.DateField()  # 데이터기준일자


    def __str__(self):
        return f"행정지역 : {self.area_code} CCTV 번호: {self.number}, 소재지: {self.address_road} ({self.latitude}, {self.longitude})"
    
    