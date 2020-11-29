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




