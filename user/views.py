from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from order.models import Order, OrderProduct
from product.models import Category, Comment
from user.forms import SignUpForm, UserUpdeteForm, ProfileUpdeteForm
from user.models import UserProfile, Releve, ProfilePro

# Create your views here.


@login_required(login_url='/login')
def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)


def login_form(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user=request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Error !! username or Password is incorrect")
            return HttpResponseRedirect('/login')
            # Return an 'invalid login' error message.
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'login_form.html',context)


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #Save user form data to user table
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password) #login after registration
            login(request, user)

            # CREATE DATA IN PROFILE TABLE FOR USER
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()

            # CREATE DATA IN PROFILE PROFESSIONNEL TABLE FOR USER
            current_user = request.user
            data = ProfilePro()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created !, veuillez remplir votre profile.')

            return HttpResponseRedirect('/user/update')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')

    category = Category.objects.all()
    form = SignUpForm()
    context = {'category': category,
               'form': form
               }
    return render(request, 'signup_form.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdeteForm(request.POST, instance=request.user)
        profile_form = ProfileUpdeteForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid ():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile was successfully updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdeteForm(instance=request.user)
        profile_form = ProfileUpdeteForm(instance=request.user.userprofile)
    context = {'category': category,
               'user_form': user_form,
               'profile_form': profile_form,
               }
    return render(request, 'user_update.html', context)

@login_required(login_url='/login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        category = Category.objects.all()
    context = {'category': category,
               'form':form,
               }
    return render(request, "user_password.html",context)


@login_required(login_url='/login')
def user_orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
        'category':category,
        'orders' : orders
                }
    return render(request,'user_orders.html', context)

@login_required(login_url='/login')
def user_orderdetail(request,id):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        'category': category,
        'order': order,
        'orderitems': orderitems
    }
    return render(request, 'user_order_detail.html', context)

@login_required(login_url='/login')
def user_order_product(request):
    category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id).order_by('product_id','-create_at')
    context = {
        'category': category,
        'order_product': order_product,
            }
    return render(request, 'user_order_product.html', context)

@login_required(login_url='/login')
def user_order_product_detail(request,id,oid):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    context = {
        'category': category,
        'order': order,
        'orderitems': orderitems
            }
    return render(request, 'user_order_detail.html', context)

@login_required(login_url='/login')
def user_comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'comments' : comments
                }
    return render(request,'user_comments.html', context)

@login_required(login_url='/login')
def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request,'Comment deleted..')
    return HttpResponseRedirect('/user/comments')


def faq(request):
    return HttpResponse('FAQ PAGE')

@login_required(login_url='/login')
def releve(request):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user
    profile_pro = ProfilePro.objects.filter(user_id=current_user.id)

    if profile_pro :
        for rs in profile_pro:
            if rs.releve is False :
                messages.warning(request, "Vous n'êtes pas autorisé à accéder au relevé.")
                return HttpResponseRedirect(url)
            else:
                rlv = Releve.objects.filter(compte_id=current_user.id)
                sld = 0
                for rs in rlv:
                    sld += rs.solde

    else :
        messages.warning(request, "Profile professionnel doit être rempli.")
        return HttpResponseRedirect(url)

    context = {'rlv': rlv,
               'sld':sld,
               'profile_pro':profile_pro,
               }
    return render(request, 'user_releve.html', context)

@login_required(login_url='/login')
def profile_pro(request):
    current_user = request.user
    profile_pro = ProfilePro.objects.filter(user_id=current_user.id)

    context = {'profile_pro': profile_pro,
               }
    return render(request, 'user_profile_pro.html', context)

