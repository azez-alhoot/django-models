from django.urls import path
from .views import PostView,PostDetailsView

urlpatterns = [
    # path('',HomeView.as_view(),name='blog-home'),
    path('',PostView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailsView.as_view(), name='post-details'),
]
