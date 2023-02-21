import numpy as np
import pandas as pd
from pandas import ExcelFile
import matplotlib as mpl
import matplotlib.pyplot as plt

#importing csv files using read_csv
Daily_Activity = pd.read_csv('dailyActivity_merged.csv')
Daily_Calories = pd.read_csv('dailyCalories_merged.csv')
Daily_Intensities = pd.read_csv('dailyIntensities_merged.csv')
Daily_Steps = pd.read_csv('dailySteps_merged.csv')
Heartrate_Seconds = pd.read_csv('heartrate_seconds_merged.csv')
Hourly_Calories = pd.read_csv('hourlyCalories_merged.csv')
Hourly_Intensities = pd.read_csv('hourlyIntensities_merged.csv')
Hourly_Steps = pd.read_csv('hourlySteps_merged.csv')
Minute_Calories_Narrow = pd.read_csv('minuteCaloriesNarrow_merged.csv')
Minute_Calories_Wide = pd.read_csv('minuteCaloriesWide_merged.csv')
Minute_Intensities_Narrow = pd.read_csv('minuteIntensitiesNarrow_merged.csv')
Minute_Intensities_Wide = pd.read_csv('minuteIntensitiesWide_merged.csv')
Minute_METs_Narrow = pd.read_csv('minuteMETsNarrow_merged.csv')
Minute_Sleep = pd.read_csv('minuteSleep_merged.csv')
Minute_Steps_Narrow = pd.read_csv('minuteStepsNarrow_merged.csv')
Minute_Steps_Wide = pd.read_csv('minuteStepsWide_merged.csv')
Sleep_Day = pd.read_csv('sleepDay_merged.csv')
Weight_Log_Info = pd.read_csv('weightLogInfo_merged.csv')