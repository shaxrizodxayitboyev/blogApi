from django.urls import path
from blog import views

urlpatterns = [
    # fbw
    path('blogs/search/', views.search_blogs, name='search-blogs'),

    # cbw
    path('cbw/blogs/', views.BlogListCreateAPIView.as_view(), name='cbw-blogs-list-create'),
    path('cbw/blogs/<int:pk>/', views.BlogRetriveUpdateDetailAPIView.as_view(), name='cbw-blogs-delete-retrive-update')
]
