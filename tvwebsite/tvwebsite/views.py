from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPrediction(brand, size, disp, condition):
    import pickle
    import pandas as pd
    model = pickle.load(open("model.sav", "rb"))

    x_point = {'Brand': brand, 'Screen Size': int(size), 'Display Technology': disp, 'Condition': condition}
    x_df = pd.DataFrame([x_point])

    prediction = model.predict(x_df)
    
    return prediction



# result page view
def result(request):
    brand = request.GET['brand']
    size = request.GET['size']
    disp = request.GET['disp']
    condition = request.GET['condition']

    result = round(getPrediction(brand, int(size), disp, condition)[0], 2)
    
    return render(request, 'result.html', {'result': result})