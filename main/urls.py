from django.urls import path

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('service/', views.ServicesView.as_view(), name='service_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('market/', views.MarketView.as_view(), name='market_page'),
    path('order/', views.OrderView.as_view(), name='order_page'),
    path('contact/', views.ContactView.as_view(), name='contact_page'),
]
