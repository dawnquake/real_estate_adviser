from django.db import models

class Postcode(models.Model):

    # db needs a default
    postcode = models.CharField(max_length=100, unique=True, primary_key=True, default="DUMMY")  # Postcode (e.g., "SW1A 1AA")
    postcodenospace = models.CharField(max_length=100, default="DUMMY")
    # in_use = models.CharField(max_length=10)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    easting = models.CharField(max_length=100, null=True)
    northing = models.CharField(max_length=100, null=True)
    # grid_ref = models.CharField(max_length=10)
    county = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    ward = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    # parish = models.CharField(max_length=100)
    # national_park = models.CharField(max_length=100)
    population = models.CharField(max_length=100, null=True)
    households = models.CharField(max_length=100, null=True)
    # built_up_area = models.CharField(max_length=100)
    rural_urban = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    altitude = models.CharField(max_length=100, null=True)
    london_zone = models.CharField(max_length=100, null=True)
    nearest_station = models.CharField(max_length=100, null=True)
    distance_to_station = models.CharField(max_length=100, null=True)
    postcode_area = models.CharField(max_length=100, null=True)
    postcode_district = models.CharField(max_length=100, null=True)
    police_force = models.CharField(max_length=100, null=True)
    water_company = models.CharField(max_length=100, null=True)
    average_income = models.CharField(max_length=100, null=True)
    sewage_company = models.CharField(max_length=100, null=True)
    travel_to_work_area = models.CharField(max_length=100, null=True)
    distance_to_sea = models.CharField(max_length=100, null=True)
    property_type = models.CharField(max_length=100, null=True)
    roads = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.postcode} ({self.latitude}, {self.longitude})"
