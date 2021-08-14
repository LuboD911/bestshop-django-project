from django.urls import path

from bestshop.footer.views import Contacts,FAQ,AboutUs,FollowUs,Career,Sponsors

urlpatterns = (
    path('contacts/',Contacts.as_view(),name = 'contacts'),
    path('FAQ/',FAQ.as_view(),name = 'FAQ'),
    path('about_us/',AboutUs.as_view(),name = 'about us'),
    path('follow_us/',FollowUs.as_view(),name = 'follow us'),
    path('career/',Career.as_view(),name = 'career'),
    path('sponsors/',Sponsors.as_view(),name = 'sponsors'),

)