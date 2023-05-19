"""
URL configuration for Afisha project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from movie_app import views

urlpatterns = [
    path('directors/', views.DirectorListAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MovieListAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('reviews/', views.ReviewListApIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('movies/reviews/', views.MovieReviewAPIView.as_view()),
    path('genres/', views.GenreListAPIView.as_view()),
    path('genres/<int:id>/', views.GenreDetailAPIView.as_view()),
]
