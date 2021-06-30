from django.shortcuts import render, redirect
from .models import Test

# Index Page
def index(request):
    return render(request,'index.html')


# Game Function
def game(request):
    if request.method == 'POST':

        # For Only Question No 1
        if request.POST.get('qno') == "Q1":

            user_name = request.POST.get('username')
            
            return render(request, 'gamepage.html',{'name':user_name.replace(" ","")})

        # For Only Question No 2
        elif request.POST.get('qno') == "Q2":
            user_name = request.POST.get('username')
            best_cricketer = request.POST.get('bestCricketer')
            
          
            return render(request, 'gamepage2.html',{'name':user_name,'ans1':best_cricketer})
        
        # For Only Question No 3
        elif request.POST.get('qno') == "Q3":

            # Finally getting all the value i.e username and answer1 viz passed from previous pages and answer2 in same page
            # saving all that at a time in Database 
            user_name = request.POST.get('username')
            best_cricketer = request.POST.get('answer1')
            flag_color = request.POST.getlist('flagColor')
            flag_color = str(flag_color).replace("[","").replace("]","").replace("'","")

            

            # Saving the Data of Test in Test Model Class (Database)
            test = Test(name = user_name, first_question= "Who is the best cricketer in the world?", first_answers=best_cricketer,second_question="What are the colors in the Indian national flag?",second_answers=flag_color)
            test.save()

            # After Saving The data Redirecting it to Summary Function i.e Result Page
            return redirect(summary,user_name)

    return render(request,'homepage.html')


# Result Page Function
def summary(request,user_name):
    test = Test.objects.filter(name=user_name).last()
    print(test.datetime)
    return render(request,'result.html',{'test':test})


# History Page Function
def history(request):
    test = Test.objects.filter()
    print(test)
    return render(request,'history.html',{'tests':test})