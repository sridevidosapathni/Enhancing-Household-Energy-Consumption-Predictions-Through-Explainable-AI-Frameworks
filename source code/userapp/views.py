from django.shortcuts import render,redirect
import urllib.parse   #for send SMS
import urllib.request #for send SMS
import time
import random
from userapp.models import *
from django.conf import settings
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd


from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

from django.contrib import messages
import pickle
from adminapp.models import *



def user_about(request):
    return render(request,'user/about.html')

def user_admin(request):
    admin_email= "admin@gmail.com"
    admin_password="admin"
    if request.method=="POST":
        admin_e=request.POST.get("admin_email")
        admin_p=request.POST.get("admin_password")
        if (admin_e==admin_email and admin_p==admin_password):
            messages.success(request,'login successfull')
            return redirect("admin_dashboard")
        else:
            messages.error(request,"login credentials was incorrect....")
            return redirect("user_admin")
    
    return render(request,'user/admin.html')
   

def user_contact(request):
    return render(request,'user/contact.html')

def user_dashboard(request):
    prediction_count =  UserDetails.objects.all().count()
    user_id = request.session["user_id"]
    user = UserDetails.objects.get(user_id = user_id)
    return render(request,'user/user-dashboard.html', {'predictions' : prediction_count, 'la' : user})



def user_index(request):
    return render(request,'user/user-index.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        print(email, password,'data')
        try:
            user = UserDetails.objects.get(user_email = email, user_password = password)
            print(user)
            
            if user.user_password ==  password :
                if user.user_status == 'Accepted':
                    
                    messages.success(request,'login successfull')
                    request.session['user_id'] = user.user_id
                    print('login sucessfull')
                    # user.no_of_times_login += 1
                    user.save()
                    return redirect('user_dashboard')
                   
                elif user.user_password ==  password and user.user_status == 'Rejected':
                    messages.warning(request,"you account is rejected")
                else:
                    messages.info(request,"your account is in pending")
            else:
                 messages.error(request,'Login credentials was incorrect...')    
        except:
            
            messages.error(request,'Login credentials was incorrect...')    

            
            return redirect('user_login')
        
    return render(request,'user/user-login.html')




from django.shortcuts import render
from django.conf import settings
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from lightgbm import LGBMRegressor
import shap
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt
import os



# from django.shortcuts import render
# from django.http import JsonResponse
# import pandas as pd
# import numpy as np
# import shap
# import io
# import base64
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler
# from lightgbm import LGBMRegressor
# from lime.lime_tabular import LimeTabularExplainer
# from django.conf import settings

# def user_prediction(request):
#     # Load dataset from settings.py
#     file_path = settings.DATASET_PATH
#     data = pd.read_csv(file_path)

#     # Handle Missing 'Power' Column
#     if "Power" not in data.columns:
#         data["Power"] = data["Current"] * data["Voltage"]

#     # Preprocess Data
#     data.drop("Time", axis=1, inplace=True)

#     feature_columns = ["Current", "Voltage", "Power", "Inst_energy_t-1", "Hour_interval", "Day"]
#     target_column = "Inst_energy"

#     X = data[feature_columns]
#     y = data[target_column]

#     # Train the Model
#     scaler = MinMaxScaler()
#     X_scaled = scaler.fit_transform(X)

#     model = LGBMRegressor(
#         objective="regression",
#         metric="rmse",
#         learning_rate=0.1,
#         num_leaves=31,
#         feature_fraction=0.8,
#         bagging_fraction=0.8,
#         bagging_freq=5,
#         random_state=42
#     )
#     model.fit(X_scaled, y)

#     # Handle form submission for user input
#     if request.method == 'POST':
#         # Get user input from request.POST

#         current = float(request.POST.get('current'))
#         voltage = float(request.POST.get('voltage'))
#         inst_energy_t_1 = float(request.POST.get('inst_energy_t_1'))
#         hour_interval = int(request.POST.get('hour_interval'))
#         day = int(request.POST.get('day'))

#         # Create a new data point for prediction
#         new_data = pd.DataFrame({
#             "Current": [current],
#             "Voltage": [voltage],
#             "Power": [current * voltage],  # Assuming Power = Current * Voltage
#             "Inst_energy_t-1": [inst_energy_t_1],
#             "Hour_interval": [hour_interval],
#             "Day": [day],
#         })
#         new_data_scaled = scaler.transform(new_data)

#         # Make Prediction
#         predicted_inst_energy = model.predict(new_data_scaled)
#         prediction_result = f"Predicted Inst_energy: {predicted_inst_energy[0]}"

#         # Generate SHAP Explanation
#         explainer_shap = shap.TreeExplainer(model)
#         shap_values = explainer_shap.shap_values(X_scaled)

#         # Generate SHAP Summary Plot
#         fig_shap = plt.figure()
#         shap.summary_plot(shap_values, X_scaled, feature_names=feature_columns)
#         shap_buf = io.BytesIO()
#         plt.savefig(shap_buf, format='png')
#         shap_buf.seek(0)
#         shap_encoded = base64.b64encode(shap_buf.read()).decode('utf-8')
#         plt.close(fig_shap)

#         # Generate LIME Explanation
#         explainer_lime = LimeTabularExplainer(
#             X_scaled, 
#             feature_names=feature_columns, 
#             class_names=['Positive', 'Negative'], 
#             mode='regression'
#         )
#         lime_exp = explainer_lime.explain_instance(new_data_scaled[0], model.predict, num_features=6)

#         # Generate LIME HTML Explanation
#         lime_html = lime_exp.as_html()
#         lime_buf = io.BytesIO()
#         lime_buf.write(lime_html.encode('utf-8'))
#         lime_encoded = base64.b64encode(lime_buf.getvalue()).decode('utf-8')
#         lime_buf.close()
        


#         # Render results to the template
#         return render(request, "user/prediction.html", {
#             "prediction_result": prediction_result,
#             "shap_encoded": shap_encoded,
#             "lime_encoded": lime_encoded,
#         })
    
#     # If GET request, just display the form
#     return render(request, "user/prediction.html")




from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
import shap
import io
import base64
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from lightgbm import LGBMRegressor
from lime.lime_tabular import LimeTabularExplainer
from django.conf import settings

def user_prediction(request):
    # Load dataset from settings.py
    file_path = settings.DATASET_PATH
    data = pd.read_csv(file_path)

    # Handle Missing 'Power' Column
    if "Power" not in data.columns:
        data["Power"] = data["Current"] * data["Voltage"]

    # Preprocess Data
    data.drop("Time", axis=1, inplace=True)

    feature_columns = ["Current", "Voltage", "Power", "Inst_energy_t-1", "Hour_interval", "Day"]
    target_column = "Inst_energy"

    X = data[feature_columns]
    y = data[target_column]

    # Train the Model
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    model = LGBMRegressor(
        objective="regression",
        metric="rmse",
        learning_rate=0.1,
        num_leaves=31,
        feature_fraction=0.8,
        bagging_fraction=0.8,
        bagging_freq=5,
        random_state=42
    )
    model.fit(X_scaled, y)

    # Handle form submission for user input
    if request.method == 'POST':
        # Get user input from request.POST

        current = float(request.POST.get('current'))
        voltage = float(request.POST.get('voltage'))
        inst_energy_t_1 = float(request.POST.get('inst_energy_t_1'))
        hour_interval = int(request.POST.get('hour_interval'))
        day = int(request.POST.get('day'))

        # Create a new data point for prediction
        new_data = pd.DataFrame({
            "Current": [current],
            "Voltage": [voltage],
            "Power": [current * voltage],  # Assuming Power = Current * Voltage
            "Inst_energy_t-1": [inst_energy_t_1],
            "Hour_interval": [hour_interval],
            "Day": [day],
        })
        new_data_scaled = scaler.transform(new_data)

        # Make Prediction
        predicted_inst_energy = model.predict(new_data_scaled)
        prediction_result = f"Predicted Inst_energy: {predicted_inst_energy[0]}"

        


        # Render results to the template
        return render(request, "user/prediction.html", {
            "prediction_result": prediction_result,
            "shap_image_path": os.path.join(settings.MEDIA_URL, 'shap_summary_plot.png'),

            "lime_plot_path": os.path.join(settings.MEDIA_URL, 'lime_explanation_plot.png')

                
        })
    
    # If GET request, just display the form
    return render(request, "user/prediction.html")











from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User  # Assuming this is a custom user model; change if using Django's built-in User
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        address = request.POST.get('address')

        profile_picture = request.FILES.get('profile_picture')  # Handle file upload

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        user = User(name=name, mobile=mobile, email=email, password=password, age=age, address=address)

        if profile_picture:
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)
            user.profile_picture = filename

        user.save()

        messages.success(request, 'Registration successful! Please login.')
        return redirect('user_login')

    return render(request, 'user/register.html')

      

def userlogout(request):
    view_id = request.session["user_id"]
    user = UserDetails.objects.get(user_id = view_id)
    t = time.localtime()
    user.last_login_time = t
    current_time = time.strftime('%H:%M:%S', t)
    user.last_login_time = current_time
    current_date = time.strftime('%Y-%m-%d')
    user.last_login_date = current_date
    user.save()
    messages.info(request, 'You are logged out..')
    # print(user.Last_Login_Time)
    # print(user.Last_Login_Date)
    return redirect('user_login')



