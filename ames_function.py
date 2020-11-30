import matplotlib.dates as dates
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def is_outlier(points, thresh=3.5):
    """
    Returns a boolean array with True if points are outliers and False 
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor. 
    """
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh




def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d




def dist_from_coordinates(lat1, lon1, lat2, lon2):
  R = 6371  # Earth radius in km

  #conversion to radians
  d_lat = np.radians(lat2-lat1)
  d_lon = np.radians(lon2-lon1)

  r_lat1 = np.radians(lat1)
  r_lat2 = np.radians(lat2)

  #haversine formula
  a = np.sin(d_lat/2.) **2 + np.cos(r_lat1) * np.cos(r_lat2) * np.sin(d_lon/2.)**2

  haversine = 2 * R * np.arcsin(np.sqrt(a))

  return haversine


def neighborhood_mutate (row):
   if row['Neighborhood'] == 'Blmngtn':
      return 'Gilbert'
   if row['Neighborhood'] == 'Blueste':
      return 'Lincoln Way / State Ave'
   if row['Neighborhood'] == 'BrDale':
      return 'Grand Ave / 30th St'
   if row['Neighborhood'] == 'BrkSide':
      return 'E 13th St / Duff Ave'
   if row['Neighborhood'] == 'ClearCr':
      return 'Ontario'
   if row['Neighborhood'] == 'CollgCr':
      return 'Lincoln Way / 500th Ave'
   if row['Neighborhood'] == 'Crawfor':
      return 'S Duff Ave / E Lincoln Way'
   if row['Neighborhood'] == 'Edwards':
      return 'Woodland St / West St'
   if row['Neighborhood'] == 'Gilbert':
      return 'Gilbert'
   if row['Neighborhood'] == 'IDOTRR' :
      return 'S Duff Ave / E Lincoln Way'
   if row['Neighborhood'] == 'MeadowV':
      return 'S Duff Ave / Airport Rd'
   if row['Neighborhood'] == 'Mitchel':
      return 'S Duff Ave / Airport Rd'
   if row['Neighborhood'] == 'NAmes':
      return 'City Center'
   if row['Neighborhood'] == 'NoRidge':
      return 'Gilbert'
   if row['Neighborhood'] == 'NPkVill':
      return 'Grand Ave / 30th St'
   if row['Neighborhood'] == 'NridgHt':
      return 'Gilbert'
   if row['Neighborhood'] == 'NWAmes':
      return '24th St / Grand Ave'
   if row['Neighborhood'] == 'OldTown':
      return 'E 13th St / Duff Ave'
   if row['Neighborhood'] == 'SWISU':
      return 'Lincoln Way / State Ave'
   if row['Neighborhood'] == 'Sawyer':
      return 'Ontario'
   if row['Neighborhood'] == 'SawyerW':
      return 'Ontario'
   if row['Neighborhood'] == 'Somerst' :
      return 'Grand Ave / 30th St'
   if row['Neighborhood'] == 'StoneBr':
      return 'Grand Ave / 30th St'
   if row['Neighborhood'] == 'Timber':
      return 'S Duff Ave / Airport Rd'
   if row['Neighborhood'] == 'Veenker':
      return 'Stange Rd / Pammel Ct'
   if row['Neighborhood'] == 'Greens':
      return 'Stange Rd / Pammel Ct'

def feature_eng(df):
    # calculate age of building
    df['BldgAge'] = df['YrSold'] - df['YearBuilt']

    # binarize YearRemodAdd
    df['Remodeled'] = np.where(df['YearRemodAdd'] == df['YearBuilt'], 0, 1)

    # binarize MSSubClass to PUD or not PUD
    df['IsPUD'] = np.where(df['MSSubClass'].isin(['120','150','160','180']), 1, 0)
    
    # binarize LotShape to Reg/not Reg
    df['LotIsReg'] = np.where(df['LotShape']=='Reg', 1, 0)
    
    # binarize LandContour to HLS and Low vs not HLS or Low
    df['HillORDepr'] = np.where(df['LandContour'].isin(['HLS','Low']), 1, 0)
    
    # binarize Condition1/2 to positive feature or no positive feature
    df['PosFeat'] = np.where(df['Condition1'].isin(['PosN','PosA'])|df['Condition2'].isin(['PosN','PosA']), 1, 0)

    # combine exterior material 1/2 to one column
    df['ExtMatl'] = np.where((df['Exterior1st']==df['Exterior2nd']),df['Exterior1st'], 'Mixed')
    
    # covnert Electrical to circuit breakers/
    #df['SBrkrElecOnly']=np.where(df['Electrical']=='SBrkr',1,0)
    
    # simply qual/cond features
    for col in ['ExterQual','BsmtQual','KitchenQual','FireplaceQu','GarageQual','ExterCond',\
                'BsmtCond','GarageCond','HeatingQC']:
        df[col+'_num'] = df[col].replace(['Ex','Gd','TA','Fa','Po','None'],[10,8,6,4,2,0])

    # sum up porch area
    df['Total_porch_sf'] = df['OpenPorchSF'] + df['3SsnPorch'] + df['EnclosedPorch'] +\
                                df['ScreenPorch'] + df['WoodDeckSF']
    
    # binarize fences
    df['HasFence'] = np.where(df['Fence']=='None', 0, 1)

    # simplify Functional to 3 classes
    df['Funct_3'] = df['Functional'].replace(['Maj1', 'Maj2', 'Min1', 'Min2', 'Mod', 'Sal', 'Typ'],\
                                             ['ModToSev','ModToSev','Minor','Minor','ModToSev','ModToSev','Normal'])
    
    # binarize sale condition to normal sale condition or not sale condition
    #df['NormalSaleCond'] = np.where(df['SaleCondition']=='Normal', 1, 0)
    
    # drop the original columns or unused columns
    df = df.drop(['MSSubClass','YearBuilt','YearRemodAdd','LotFrontage','LotArea','LotConfig','LandSlope',\
                  'Condition1','Condition2','Exterior1st','Exterior2nd','LotShape','LandContour',\
                  'OpenPorchSF','3SsnPorch','EnclosedPorch','ScreenPorch','WoodDeckSF',\
                  'Fence','Functional','ExterQual','BsmtQual','KitchenQual','FireplaceQu',\
                  'GarageQual','ExterCond','BsmtCond','GarageCond','HeatingQC',\
                  'GarageCars','RoofMatl','RoofStyle','KitchenAbvGr','MSZoning'],\
                 axis = 1)
    return df


