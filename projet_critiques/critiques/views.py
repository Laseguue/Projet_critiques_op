from .forms import TicketForm, ReviewForm
from .models import Ticket, Review, UserFollows
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django import forms


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('list_tickets')
    else:
        form = TicketForm()
    return render(request, 'ticket_form.html', {'form': form})

@login_required
def list_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('list_tickets')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticket_form.html', {'form': form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        ticket.delete()
        return redirect('list_tickets')
    return render(request, 'ticket_confirm_delete.html', {'ticket': ticket})


@login_required
def create_review(request):
    ticket_form = TicketForm(request.POST or None, request.FILES or None)
    review_form = ReviewForm(request.POST or None, request.FILES or None)

    if ticket_form.is_valid() and review_form.is_valid():
        ticket = ticket_form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        
        review = review_form.save(commit=False)
        review.user = request.user
        review.ticket = ticket
        review.save()
        
        return redirect('list_reviews')
    
    return render(request, 'review_form.html', {'ticket_form': ticket_form, 'review_form': review_form})

@login_required
def list_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('list_reviews')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_form.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.delete()
        return redirect('list_reviews')
    return render(request, 'review_confirm_delete.html', {'review': review})

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow != request.user:
        UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)
    return redirect('some_view_name')  # Remplacez 'some_view_name' par le nom de la vue vers laquelle rediriger après avoir suivi un utilisateur.

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.filter(followed_user=user_to_unfollow).delete()
    return redirect('some_view_name')  # Remplacez 'some_view_name' par le nom de la vue vers laquelle rediriger après avoir arrêté de suivre un utilisateur.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connecter l'utilisateur après l'inscription
            login(request, user)
            return redirect('login')  # Redirigez vers la vue de votre choix après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    # Obtenir les utilisateurs suivis par l'utilisateur connecté
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)

    # Obtenir les billets des utilisateurs suivis et de l'utilisateur connecté
    tickets = (Ticket.objects.filter(user__in=followed_users) | Ticket.objects.filter(user=request.user)).prefetch_related('review_set')
    
    # Récupérer les IDs des billets pour pouvoir les exclure des critiques générales
    ticket_ids = tickets.values_list('id', flat=True)

    # Obtenir les critiques des utilisateurs suivis et de l'utilisateur connecté qui ne sont pas déjà associées aux billets
    reviews = (Review.objects.filter(user__in=followed_users) | Review.objects.filter(user=request.user)).exclude(ticket__in=ticket_ids)

    context = {
        'tickets': tickets,
        'reviews': reviews,
    }

    return render(request, 'home.html', context)

def user_posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(request, 'user_posts.html', context)

def user_follows(request):
    if request.method == "POST":
        username_to_follow = request.POST.get("username_to_follow")
        try:
            user_to_follow = User.objects.get(username=username_to_follow)
            if user_to_follow != request.user:  # L'utilisateur ne peut pas se suivre lui-même
                follow, created = UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)
                if created:
                    messages.success(request, f"Vous suivez maintenant {user_to_follow.username}!")
                else:
                    messages.warning(request, f"Vous suivez déjà {user_to_follow.username}.")
            else:
                messages.warning(request, "Vous ne pouvez pas vous suivre vous-même.")
        except User.DoesNotExist:
            messages.error(request, "Cet utilisateur n'existe pas.")

    followed_users = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    context = {
        'followed_users': followed_users,
        'followers': followers
    }
    return render(request, 'user_follows.html', context)

def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
        UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
        messages.success(request, f"Vous avez arrêté de suivre {user_to_unfollow.username}!")
    except User.DoesNotExist:
        messages.error(request, "Cet utilisateur n'existe pas.")

    return redirect(reverse('follows'))

@login_required
def create_review_with_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('list_reviews')
    else:
        form = ReviewForm(initial={'ticket': ticket})
        form.fields['ticket'].widget = forms.HiddenInput()

    return render(request, 'review_form.html', {'review_form': form, 'ticket': ticket})