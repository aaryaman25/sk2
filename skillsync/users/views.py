from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Skill


def profile_view(request):
    # Get or create profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    skills = profile.skills.all()

    # Handle search query
    query = request.GET.get('q')  # Get the search query from the request
    all_skills = Skill.objects.all()  # Get all skills for the dropdown menu

    if query:
        all_skills = all_skills.filter(name__icontains=query)  # Filter skills based on search query

    if request.method == 'POST':
        # Check if the form contains LinkedIn URL
        if 'linkedin_url' in request.POST:
            profile.linkedin_url = request.POST['linkedin_url']  # Update LinkedIn URL

        # Check if the form contains a file
        if 'resume' in request.FILES:
            profile.resume = request.FILES['resume']
        
        # Handle skills selection
        selected_skills = request.POST.getlist('skills')  # Get selected skills from the form
        profile.skills.set(selected_skills)  # Update the user's skills

        profile.save()  # Save changes to the profile
        return redirect('profile')  # Redirect to the profile page after saving

    context = {
        'profile': profile,
        'skills': skills,
        'all_skills': all_skills,  # Pass all available skills to the template
        'query': query
    }

    return render(request, 'profile.html', context)


def search_skills_view(request):
    query = request.GET.get('q')  # Get the search query from the request
    skills = Skill.objects.all()  # Default to all skills

    if query:
        skills = skills.filter(name__icontains=query)  # Filter skills based on the search query

    return render(request, 'search_skills.html', {
        'skills': skills,
        'query': query
    })
