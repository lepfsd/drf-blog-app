from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view()),
    path('<post_slug>', PostDetailView.as_view()),
    path('category/<category_id>', BlogListCategoryView.as_view()),
    path("search/<str:search_term>",SearchBlogView.as_view()),
]