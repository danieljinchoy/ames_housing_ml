library(dplyr)
library(ggplot2)
library(lubridate)
library(tidyverse)

housing = read.csv('Ames_HousePrice.csv', header = TRUE)
real_estate = read.csv('data/Ames_Real_Estate_Data.csv')
