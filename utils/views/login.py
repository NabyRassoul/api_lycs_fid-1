# from django.shortcuts import render
# from utils.forms import LoginForm
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.shortcuts import redirect

# def sign_in(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request,'dashboard/login.html', {'form': form})
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=username,password=password)
#             if user:
#                 login(request, user)
#                 messages.success(request,f'Hi {username}, welcome back!')
#                 return redirect('')
        
#         # form is not valid or user is not authenticated
#         messages.error(request,f'Invalid username or password')
#         return render(request,'users/login.html',{'form': form})
