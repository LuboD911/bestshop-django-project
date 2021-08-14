from django.urls import reverse,resolve
from django.test import SimpleTestCase

from bestshop.footer.views import Contacts,FAQ,AboutUs,FollowUs,Career,Sponsors

class TestFooterUrls(SimpleTestCase):

    def test_Contacts_url(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func.view_class, Contacts)

    def test_FAQ_url(self):
        url = reverse('FAQ')
        self.assertEquals(resolve(url).func.view_class, FAQ)

    def test_AboutUs_url(self):
        url = reverse('about us')
        self.assertEquals(resolve(url).func.view_class, AboutUs)

    def test_FollowUs_url(self):
        url = reverse('follow us')
        self.assertEquals(resolve(url).func.view_class, FollowUs)

    def test_Career_url(self):
        url = reverse('career')
        self.assertEquals(resolve(url).func.view_class, Career)

    def test_Sponsors_url(self):
        url = reverse('sponsors')
        self.assertEquals(resolve(url).func.view_class, Sponsors)