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
    
    
class ConvenienceStore(models.Model):
    '''
    TYPE	SR_NM	ADRES	TEL_NO	LA	LO	DETAIL_ADR	SIGUNGU	SIDO	UMD	LEGALDONG_	LEGALDON_1    
    '''
    num = models.CharField(max_length=100)  # [여성안전지킴이집, 아동안전지킴이집, 편의점]
    sr_nm = models.CharField(max_length=100)  # [씨유 동인천역 점, 부평 경찰서]
    adres = models.CharField(max_length=100)  # [인천광역시 중구 참외전로 117-9,..]
    tel_no = models.CharField(max_length=50, null=True, blank=True)   # [전화번호]
    latitude = models.FloatField()  # WGS84위도
    longitude = models.FloatField()  # WGS84경도  
    detail_adr = models.CharField(max_length=100)  # [인천광역시 중구 참외전로 117-9,..]
    sigungu = models.CharField(max_length=100) # 시군구[인천, 대전, 충남, ..]
    sido = models.CharField(max_length=100)  # [중구, 부평구, ]
    umd = models.CharField(max_length=100)  # [인현동]

    def __str__(self):
        return f"TYPE : {self.type} 이름 : {self.sr_nm}, 소재지: {self.adres} ({self.latitude}, {self.longitude})"
    
    
class PoliceStation(models.Model):
    '''
    연번	시도청	경찰서	관서명	구분	전화번호	주소	Lat	Lng
    '''
    number = models.IntegerField()  # 번호
    sido = models.CharField(max_length=100)  # 시도청 [서울청, ]
    policestation = models.CharField(max_length=100)  # 경찰서 [서울마포]
    department = models.CharField(max_length=100)  # 관서명 [종로2가]
    type = models.CharField(max_length=100)  # 구분 [지구대]
    tel_no = models.CharField(max_length=50, null=True, blank=True)   # 전화번호 [02-...]
    address = models.CharField(max_length=100)  # 주소 [서울특별시 중구  을지로 234..]
    latitude = models.FloatField()  # 위도
    longitude = models.FloatField()  # 경도

    def __str__(self):
        return f"이름 : {self.department} {self.type}, 소재지: {self.address} ({self.latitude}, {self.longitude})"
    

