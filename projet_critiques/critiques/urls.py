from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.list_tickets, name='list_tickets'),
    path('ticket/new/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/edit/', views.update_ticket, name='update_ticket'),
    path('ticket/<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
    path('reviews/', views.list_reviews, name='list_reviews'),
    path('review/new/', views.create_review, name='create_review'),
    path('review/<int:review_id>/edit/', views.update_review, name='update_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('posts/', views.user_posts, name='posts'),
    path('follows/', views.user_follows, name='follows'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('review/create/<int:ticket_id>/', views.create_review_with_ticket, name='create_review_with_ticket'),
]