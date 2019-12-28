from django.urls import path
from .import views

urlpatterns = [
    path('',                                      views.banners,               name='home'),
    path('publisher/register/',                   views.register,              name='publisher-register'),
    path('publisher/login/',                      views.login,                 name='publisher-login'),
    path('publisher/logout/',                     views.logout,                name='publisher-logout'),
    path('publisher/update/<int:id>',             views.update_user_details,   name='user-update'),

    path('publisher/admin-panel/',                views.admin_panel,           name='publisher-admin-panel'),
    path('publisher/addbannerdetails/',           views.banner_details,        name='publisher-addbannerdetails'),

    path('publisher/bannerslist/',                views.banners_current_user, name='publisher-bannerlist'),
    path('publisher/all-bannerslist/<int:id>',    views.banners_publisherwise, name='allpublisher-bannerlist'),
    path('publisher/bannerslist/update/<int:id>', views.update_banner_details, name='banner-update'),
    path('publisher/bannerslist/delete/<int:id>', views.delete_baanner,        name='banner-del'),
]