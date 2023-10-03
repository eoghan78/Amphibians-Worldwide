# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models
from django.contrib.auth.admin import User
from django.urls import reverse
from django.core.exceptions import ValidationError


#Validator to ensure correct data value range is input
def validate_negative(value):
    if value < 0:
        raise ValidationError( ('%(value) is a negative number'), params={'value': value},)

#users
class User_Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    educational_institution = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    bio = models.TextField(blank=True, null = True)
    university_profile = models.CharField(max_length=200, null=True, blank=True)
    linked_in = models.CharField(max_length=200, null=True, blank=True)
    academia_publication = models.CharField(max_length=200, null=True, blank=True)
    publication_1 = models.CharField(max_length=200, null=True, blank=True)
    publication_2 = models.CharField(max_length=200, null=True, blank=True)
    publication_3 = models.CharField(max_length=200, null=True, blank=True)
    publication_4 = models.CharField(max_length=200, null=True, blank=True)
    publication_5 = models.CharField(max_length=200, null=True, blank=True)
    permission_to_display_contact_information = models.BooleanField(default = False, blank=False, null=False)
    permission_to_display_publications = models.BooleanField(default = False, blank=False, null=False)


    def __str__(self):
        return self.user.username

#One to Many
class Parity_Mode(models.Model):
    parity_mode_id = models.AutoField(primary_key=True)
    parity_mode_desc = models.CharField(max_length=200)

    def __str__(self) :
        return self.parity_mode_desc

    class Meta:
        managed = False
        db_table = 'parity_mode'

class Pop_Trend(models.Model):
    pop_trend_id = models.AutoField(primary_key=True)
    pop_trend_status = models.CharField(max_length=200)

    def __str__(self) :
        return self.pop_trend_status

    class Meta:
        managed = False
        db_table = 'pop_trend'

class IUCN(models.Model):
    iucn_id = models.AutoField(primary_key=True)
    iucn_status = models.CharField(max_length=200)

    def __str__(self) :
        return self.iucn_status

    class Meta:
        managed = False
        db_table = 'iucn'

#Taxonomy Structure
class Order_Taxon(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_taxon_name = models.CharField(max_length=200)

    def __str__(self) :
        return self.order_taxon_name

    class Meta:
        managed = False
        db_table = 'order_taxon'

class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=200)
    order = models.ForeignKey(Order_Taxon, on_delete=models.CASCADE)

    def __str__(self) :
        return self.family_name

    class Meta:
        managed = False
        db_table = 'family'

class Genus(models.Model):
    genus_id = models.AutoField(primary_key=True)
    genus_name = models.CharField(max_length=200)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    def __str__(self) :
        return self.genus_name

    class Meta:
        managed = False
        db_table = 'genus'

# Species Structure
class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    species_name_common = models.CharField(max_length=200, blank=True, null=True)
    species_name_latin = models.CharField(max_length=200, blank=True, null=True)
    size_max_male = models.FloatField(blank=True, null=True, validators=[validate_negative])
    size_max_female = models.FloatField(blank=True, null=True, validators=[validate_negative])
    size_max_record = models.FloatField(blank=True, null=True, validators=[validate_negative])
    longevity = models.FloatField(blank=True, null=True, validators=[validate_negative])
    clutch_min = models.IntegerField(blank=True, null=True, validators=[validate_negative])
    clutch_max = models.IntegerField(blank=True, null=True, validators=[validate_negative])
    clutch_avg = models.FloatField(blank=True, null=True, validators=[validate_negative])
    egg_diameter = models.FloatField(blank=True, null=True, validators=[validate_negative])
    range_size = models.FloatField(blank=True, null=True, validators=[validate_negative])
    elevation_min = models.IntegerField(blank=True, null=True)
    elevation_max = models.FloatField(blank=True, null=True)
    elevation_avg = models.FloatField(blank=True, null=True)
    img_uri_male = models.ImageField(null=True, blank=True, upload_to="images/")
    img_uri_female = models.ImageField(null=True, blank=True, upload_to="images/")
    verif_status = models.BooleanField(default = True, blank=False, null=False)
    

#Foreign Keys for Species Model
    parity_mode = models.ForeignKey(Parity_Mode, on_delete=models.DO_NOTHING, blank=True, null=True)
    pop_trend = models.ForeignKey(Pop_Trend, on_delete=models.DO_NOTHING, blank=True, null=True)
    iucn = models.ForeignKey(IUCN, on_delete=models.DO_NOTHING, blank=True, null=True)
    genus = models.ForeignKey(Genus, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User,  default='3', on_delete=models.DO_NOTHING)

    def __str__(self) :
        return self.species_name_latin

    @property
    def find_ssd (self):
        return self.size_max_male-self.size_max_female

    def get_absolute_url(self):
        return reverse('home:species_detail', args=(self.species_id,))
        
    class Meta:
        managed = True
        db_table = 'species'

#Geographic Location Structure
class Continent(models.Model):
    continent_id = models.AutoField(primary_key=True)
    continent_name = models.CharField(max_length=200)

    def __str__(self) :
        return self.continent_name

    class Meta:
        managed = False
        db_table = 'continent'

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=200)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) :
        return self.country_name

    class Meta:
        managed = False
        db_table = 'country'

class Geo_Location(models.Model):
    geo_location_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    species_locations = models.ManyToManyField(Species, through='Geo_Location_Species', through_fields=('geo_location', 'species'))

    def __str__(self) :
        return self.region_name

    class Meta:
        managed = False
        db_table = 'geo_location'

class Geo_Location_Species(models.Model):
    geo_location_species_id = models.AutoField(primary_key=True)
    geo_location = models.ForeignKey(Geo_Location, on_delete=models.CASCADE, blank=True, null=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_location_species'

#Many to Many
class Nesting_Site(models.Model):
    nesting_site_id = models.AutoField(primary_key=True)
    nesting_site_desc = models.CharField(max_length=200)
    species_sites = models.ManyToManyField(Species, through='Nesting_Site_Species', through_fields=('nesting_site', 'species'))

    def __str__(self) :
        return self.nesting_site_desc

    class Meta:
        managed = False
        db_table = 'nesting_site' 
        
class Nesting_Site_Species(models.Model):
    nesting_site_species_id = models.AutoField(primary_key=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    nesting_site = models.ForeignKey(Nesting_Site, on_delete=models.CASCADE)
    def __int__(self) :
        return self.species + self.nesting_site
        
    class Meta:
        managed = False
        db_table = 'nesting_site_species'

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_kind = models.CharField(max_length=200)
    species_activities = models.ManyToManyField(Species, through='Activity_Species', through_fields=('activity', 'species'))

    def __str__(self) :
        return self.activity_kind

    class Meta:
        managed = False
        db_table = 'activity'

class Activity_Species(models.Model):
    activity_species_id = models.AutoField(primary_key=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'activity_species'

class Micro_Habitat(models.Model):
    micro_habitat_id = models.AutoField(primary_key=True)
    micro_habitat_name = models.CharField(max_length=200)
    species_micro_habitats = models.ManyToManyField(Species, through='Micro_Habitat_Species', through_fields=('micro_habitat', 'species'))

    def __str__(self) :
        return self.micro_habitat_name

    class Meta:
        managed = False
        db_table = 'micro_habitat'

class Micro_Habitat_Species(models.Model):
    micro_habitat_species_id = models.AutoField(primary_key=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=True, null=True)
    micro_habitat = models.ForeignKey(Micro_Habitat, on_delete=models.CASCADE, blank=True, null=True)
    micro_habitat_pref_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'micro_habitat_species'
