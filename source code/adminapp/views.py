from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from userapp.models import*
from django.contrib import messages
from django.conf import settings
from django.contrib import messages
from userapp.models import *
from adminapp.models import *
import urllib.request
import urllib.parse
import pandas as pd

from django.core.paginator import Paginator

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential

from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential


# Create your views here.
def admin_dashboard(request):
    all_users_count =  UserDetails.objects.all().count()
    pending_users_count = UserDetails.objects.filter(user_status = 'pending').count()
    rejected_users_count = UserDetails.objects.filter(user_status = 'Rejected').count()
    accepted_users_count = UserDetails.objects.filter(user_status = 'Accepted').count()
    datasets_count = UserDetails.objects.all().count()
    no_of_predicts = UserDetails.objects.all().count()
    messages.success(request,"login Successful")
    return render(request,'admin/admin-dashboard.html', {'a' : pending_users_count, 'b' : all_users_count, 'c' : rejected_users_count, 'd' : accepted_users_count, 'e' : datasets_count, 'f' : no_of_predicts})
 

def pending_users(request):
    users=UserDetails.objects.filter(user_status="pending")
    context={"u":users}
    return render(request,'admin/admin-pendingusers.html',context)
 
def all_users(request):
    a = UserDetails.objects.all()
    paginator = Paginator(a, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin-allusers.html',{'all':post})
 
 
def accept_user(request, id):
    return redirect(request, id,'admin/pending_users')
 
def reject_user(request, id):
    return redirect(request,id,'requestpending_users')
 
def delete_user(request, id):
    return redirect(request,id,'all_users')
 
 
def LGBMR(request):
    return render(request,'admin/Lgbmr.html')
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from lightgbm import LGBMRegressor
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from lightgbm import LGBMRegressor

from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from lightgbm import LGBMRegressor
from lightgbm import early_stopping, log_evaluation

def lgbmr_btn(request):
    # Step 1: Load Dataset
    file_path = "G:/House_Hold_Energy/dataset/household_energy_dataset.csv"  # Replace with your actual dataset path
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        return render(request, 'admin/LGBMR.html', {"error": "Dataset file not found."})

    # Step 2: Handle Missing 'Power' Column
    if "Time" in data.columns:
        data["Time"] = pd.to_datetime(data["Time"])  # Convert 'Time' to datetime
        data.drop("Time", axis=1, inplace=True)  # Drop 'Time' column

    # Check if 'Power' column exists; if not, calculate it
    if "Power" not in data.columns:
        if "Current" in data.columns and "Voltage" in data.columns:
            data["Power"] = data["Current"] * data["Voltage"]
        else:
            return render(request, 'admin/LGBMR.html', {"error": "Missing 'Current' or 'Voltage' column to compute 'Power'."})

    # Step 3: Define Features and Target
    feature_columns = ["Current", "Voltage", "Power", "Inst_energy_t-1", "Hour_interval", "Day"]
    target_column = "Inst_energy"

    # Check for missing columns
    missing_columns = [col for col in feature_columns if col not in data.columns]
    if missing_columns:
        return render(request, 'admin/LGBMR.html', {"error": f"Missing columns in dataset: {missing_columns}"})

    X = data[feature_columns]
    y = data[target_column]

    # Add random noise to the target variable to simulate real-world noise
    np.random.seed(42)
    y = y + np.random.normal(0, 0.1, size=y.shape)

    # Scale the features to the range [0, 1]
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 4: Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # Step 5: Train the Model
    model = LGBMRegressor(
        objective="regression",
        metric="rmse",
        learning_rate=0.1,
        num_leaves=31,
        feature_fraction=0.8,
        bagging_fraction=0.8,
        bagging_freq=5
    )

    # Use callbacks for early stopping
    callbacks = [
        early_stopping(stopping_rounds=10, verbose=False),
        log_evaluation(0)  # Suppress evaluation log output
    ]

    model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        eval_metric="rmse",
        callbacks=callbacks
    )

    # Step 6: Predictions and Evaluation
    y_pred = model.predict(X_test)

    # Calculate Metrics
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    # Pass metrics to the template
    context = {
        "r2": f"{r2:.5f}",
        "rmse": f"{rmse:.5f}",
        "mse": f"{mse:.5f}",
        "mae": f"{mae:.5f}",
    }
    return render(request, 'admin/LGBMR.html', context)

    





def random(request):
    return render(request,'admin/randomforest.html')
 
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

def randomforest_btn(request):
    # Step 1: Load Dataset
    file_path = "G:/House_Hold_Energy/dataset/household_energy_dataset.csv"  # Replace with your actual dataset path
    data = pd.read_csv(file_path)

    # Convert 'Time' column to datetime (if not already done)
    data["Time"] = pd.to_datetime(data["Time"])

    # Step 2: Handle Missing 'Power' Column
    if "Power" not in data.columns:
        data["Power"] = data["Current"] * data["Voltage"]

    # Step 3: Preprocessing
    data.drop("Time", axis=1, inplace=True)  # Drop the 'Time' column

    # Define feature columns and target column
    feature_columns = ["Current", "Voltage", "Power", "Inst_energy_t-1", "Hour_interval", "Day"]
    target_column = "Inst_energy"

    # Ensure all feature columns exist
    missing_columns = [col for col in feature_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"Missing columns in dataset: {missing_columns}")

    X = data[feature_columns]
    y = data[target_column]

    # Scale the features to range [0, 1]
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 4: Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # Step 5: Model Training with RandomForestRegressor
    model = RandomForestRegressor(
        n_estimators=100, random_state=42, max_depth=None, min_samples_split=2, min_samples_leaf=1
    )
    model.fit(X_train, y_train)

    # Step 6: Model Prediction
    y_pred = model.predict(X_test)

    # Step 7: Model Evaluation
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    # Pass metrics to the template
    context = {
        "r2": r2,
        "rmse": rmse,
        "mse": mse,
        "mae": mae
    }
    return render(request, 'admin/randomforest.html', context)


 
   

 

 

 

 

def Admin_Reject_Btn(request, x):
    user=UserDetails.objects.get(user_id=x)
    user.user_status="Rejected"
    messages.success(request,"Status Changed  Successfully")
 
    user.save()
    messages.warning(request,"rejected")
 
    return redirect("admin_pendingusers")
 
def Admin_Accept_Button(request,x):
    user=UserDetails.objects.get(user_id=x)
    user.user_status="Accepted"
    messages.success(request,"Status Changed Successfully")
 
    user.save()
    messages.warning(request,"Accepted")
 
    return redirect("pending_users")
 
def Change_Status(request,id):
    # user_id=req.session["User_id"]
    user=UserDetails.objects.get(user_id=id)
    if user.user_status=="Accepted":
        user.user_status=="Rejected"
        user.save()
        messages.success(request,"Status Changed Successfully")
 
        return redirect("all_users")
   
    else:
        user.user_status="Accepted"
        user.save()
        messages.success(request,"Status Successfully Changed")
 
        return redirect("all_users")
   
def delete_User(request,id):
    UserDetails.objects.get(user_id=id).delete()
    messages.info(request,"Deleted")
 
    return redirect("all_users")
 
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render

def graph(request):
    # Data for the graph
    models = ['Random Forest', 'LGBM']
    scores = [0.9999999937043277, 0.00010]

    # Plotting the graph
    plt.figure(figsize=(8, 6))
    plt.bar(models, scores, color=['blue', 'orange'])
    plt.ylabel('R² Score', fontsize=12)
    plt.ylim(0, 1)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Annotating the bars
    for i, score in enumerate(scores):
        plt.text(i, score + 0.02, f"{score:.8f}", ha='center', fontsize=10)

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close()

    # Pass the image to the template
    return render(request, 'admin/admin-graph.html', {'graph_image': image_base64})
