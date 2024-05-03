import pandas as pd

def clean_data(data):
    
    #Drop duplicates
    # data = data.drop_duplicates()
    
    #Calculate the mean of lat. and long.
    meanX = data[data["X"]>100000].dropna(subset="X")['X'].mean()
    meanY = data[data["Y"]>100000].dropna(subset="Y")['Y'].mean()
    
    #Set outliers to mean value.
    #We think that this is reasonable to do (for now) because discarding all of the offence against a person data feels wrong, at least for counting related tasks.
    #We'll exclude the offence against a person when we deal with anything featuring location. 
    data.loc[data['X'] < 100000, "X"] = meanX
    data.loc[data['Y'] < 100000, "Y"] = meanY
    
    #convert the date columns to a proper datetime. It's actually surprisingly performant.
    data = data.reset_index(drop=True)
    #include this column to make sorting through the data easier. Time and Location are 'offset' when it is an offence against a person,
    #and so must be discarded/accounted for when trying to make calculations that involve either of these.
    data['isOffset'] = (data.HUNDRED_BLOCK == "OFFSET TO PROTECT PRIVACY")
    data['date'] = pd.to_datetime(data.YEAR.astype(str) + data.MONTH.astype(str).apply(lambda x : x.zfill(2)) + data.DAY.astype(str).apply(lambda x : x.zfill(2)) + \
    data.HOUR.astype(str).apply(lambda x : x.zfill(2)) + data.MINUTE.astype(str).apply(lambda x : x.zfill(2)), format="%Y%m%d%H%M")
    
    
    return data
