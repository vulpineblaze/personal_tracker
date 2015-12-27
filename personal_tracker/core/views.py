from django.shortcuts import render, render_to_response, get_object_or_404

from django.http import HttpResponse

from django.template import RequestContext

from core.forms import *

from django.core.exceptions import ValidationError, ObjectDoesNotExist


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def home(request):
    """ """
    context = {}
    return render(request, 'core/home.html', context)

@login_required
def index(request):
    
    # basepage =  BasePage.objects.order_by('?')[0]
    goal_list = Goal.objects.filter(user=request.user).order_by('short_name')

    goal_tuple = tuple(goal.id for goal in goal_list)

    entry_list = Entry.objects.filter(goal__in=goal_tuple).order_by('-pub_date')
    # product_list = Product.objects.filter(is_active=True,
    #                                  #frontpage=True,
    #                                  brand__is_active=True,
    #                                  ).order_by('-priority','-created')

    context = {'entry_list': entry_list,'goal_list':goal_list}
    return render(request, 'core/index.html', context)

@login_required
def goal_index(request):
    
    # basepage =  BasePage.objects.order_by('?')[0]
    goal_list = Goal.objects.filter(user=request.user).order_by('short_name') 
    # product_list = Product.objects.filter(is_active=True,
    #                                  #frontpage=True,
    #                                  brand__is_active=True,
    #                                  ).order_by('-priority','-created')

    context = {'goal_list': goal_list}
    return render(request, 'core/goal_index.html', context)


@login_required
def entry_index(request, goal_id):
    
    # basepage =  BasePage.objects.order_by('?')[0]
    entry_list = Entry.objects.filter(goal=goal_id).order_by('-pub_date')
    # product_list = Product.objects.filter(is_active=True,
    #                                  #frontpage=True,
    #                                  brand__is_active=True,
    #                                  ).order_by('-priority','-created')

    context = {'entry_list': entry_list}
    return render(request, 'core/entry_index.html', context)






  
def register(request):
    """
    Non-Class-based view for registering new users
    """
    # Like before, get the request's context.
    context = RequestContext(request)
    context['display_type']="Register"
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() :
            # Save the user's form data to the database.
            user_is_unique = False
            try:
                username = User.objects.get(username=user_form.cleaned_data['username'])
            except ObjectDoesNotExist:
                user_is_unique = True
                
            if user_is_unique   : 
                user = user_form.save()
                #user = user_form.save()
                user.is_active = True
                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                # profile = profile_form.save(commit=False)
                # profile.user = user

                # Did the user provide a profile picture?
                # If so, we need to get it from the input form and put it in the UserProfile model.
                # if 'picture' in request.FILES:
                #     profile.picture = request.FILES['picture']

                # # Now we save the UserProfile model instance.
                # profile.save()

                # Update our variable to tell the template registration was successful.
                registered = True
            else:
                # user_form._errors["username"] = ErrorList([u"User with that name already exists!"])
                pass
                
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'core/register.html',
            {'user_form': user_form, 'registered': registered},
            context)
            
            



            
def user_login(request):
    """
    Non-Class-based view for User log in
    """
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    context['display_type']="Login"
    
    
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                response_text = "<h1><a href='/'>Your SnapNode account is not enabled. </a></h1>"
                response_text += "<BR> Please contact the SnapNode administrator."
                return HttpResponse(response_text)
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("<a href='/'>Invalid login details supplied for "+username+".</a>")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return render_to_response('core/login.html', {}, context)



# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    """
    Non-Class-based view for User log out
    """
    # Since we know the user is logged in, we can now just log them out. ###
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
