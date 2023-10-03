from home.models import *
import unittest
from django.contrib.auth.admin import User
import random
import string

# Helper Methods
def user_name_generator():
    letters = string.ascii_lowercase
    random_user_name = ''.join(random.choice(letters) for i in range(10))

    return random_user_name

class Test_Home_Models_Str (unittest.TestCase):

    #TM-01
    def test_user_profile_str(self):
        user = User.objects.create(username=user_name_generator())
        testing_username = User_Profile.objects.create(user=user)
        self.assertEqual(str(testing_username), str(user.username))

    #TM-02
    def test_parity_mode_str(self):

        parity_mode_desc = Parity_Mode.objects.create(parity_mode_desc="parity test")
        self.assertEqual(str(parity_mode_desc), "parity test")

    #TM-03
    def test_pop_trend_str(self):

        pop_trend_status = Pop_Trend.objects.create(pop_trend_status="pop trend test")
        self.assertEqual(str(pop_trend_status), "pop trend test")

    #TM-04
    def test_iucn_str(self):

        iucn_status = IUCN.objects.create(iucn_status="iucn test")
        self.assertEqual(str(iucn_status), "iucn test")
    
    #TM-05
    def test_order_taxon_str(self):

        order_taxon_name = Order_Taxon.objects.create(order_taxon_name="order test")
        self.assertEqual(str(order_taxon_name), "order test")

    #TM-06
    def test_family_str(self):

        dummy_order = Order_Taxon.objects.create(order_taxon_name='Test Order Taxon')
        family_name = Family.objects.create(family_name="family test", order_id=dummy_order.order_id)
        self.assertEqual(str(family_name), "family test")

    #TM-07
    def test_genus_str(self):

        dummy_order = Order_Taxon.objects.create(order_taxon_name='Test Order Taxon')
        dummy_family = Family.objects.create(family_name='Dummy Family Name', order=dummy_order)
        genus_name = Genus.objects.create(genus_name="genus test", family=dummy_family)

        self.assertEqual(str(genus_name), "genus testfamily")

    #TM-08
    def test_species_str(self):
        
        species_name_latin = Species.objects.create(species_name_latin="species test")
        self.assertEqual(str(species_name_latin), "species test")

    #TM-09
    def test_get_absolute_url(self):
        species = Species.objects.get(species_id=1)

        self.assertEqual("/home/search/species/1/", species.get_absolute_url())

    #TM-10
    def test_continent_str(self):

        continent_name = Continent.objects.create(continent_name="continent test")
        self.assertEqual(str(continent_name), "continent test")

    #TM-11
    def test_country_str(self):

        country_name = Country.objects.create(country_name="country test")
        self.assertEqual(str(country_name), "country test")

    #TM-12
    def test_geo_location_str(self):

        region_name = Geo_Location.objects.create(region_name="region test")
        self.assertEqual(str(region_name), "region test")
    
    #TM-13
    def test_nesting_site_str(self):

        nesting_site_desc= Nesting_Site.objects.create(nesting_site_desc ="nesting test")
        self.assertEqual(str(nesting_site_desc), "nesting test")

    #TM-14
    def test_activity_str(self):

        activity_kind = Activity.objects.create(activity_kind ="activity test")
        self.assertEqual(str(activity_kind), "activity test")

    #TM-15
    def test_micro_habitat_str(self):

        micro_habitat_name = Micro_Habitat.objects.create(micro_habitat_name ="habitat test")
        self.assertEqual(str(micro_habitat_name), "habitat test")


    



