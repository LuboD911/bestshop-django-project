
from django.urls import reverse,resolve
from django.test import SimpleTestCase

from bestshop.accounts.views import login_user, logout_user, register_user, profile_details

class TestAccountsUrls(SimpleTestCase):

    def test_Login_url(self):
        url = reverse('login user')
        self.assertEquals(resolve(url).func, login_user)

    def test_Logout_url(self):
        url = reverse('log out user')
        self.assertEquals(resolve(url).func, logout_user)

    def test_Register_url(self):
        url = reverse('register user')
        self.assertEquals(resolve(url).func, register_user)

    def test_ProfileDetails_url(self):
        url = reverse('profile details')
        self.assertEquals(resolve(url).func, profile_details)