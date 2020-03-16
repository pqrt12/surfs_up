# surfs_up

# challenge
With Oahu historical weather data in position, this challenge is to analyze the Oahu June and December weather statistics. See [challenge.ipynb](https://github.com/pqrt12/surfs_up/blob/master/challenge.ipynb).

After reflecting on the tables, the "measurement" table size is queried to be about 19550 (per "date" column), a small table. Get the whole "measurement" table into pandas DataFrame.

The weather data range from 2010-01-01 to 2017-08-23. It includes daily precipitation and temperature records from several stations.

Cross all stations, the June weather data statistics are given by two DataFrame.descibe().  
There are 1574 precipitation records, mean is 0.13 inches, standard deviation is 0.33 inches.  
There are 1700 temperature records, mean is 74.9&deg;F, standard deviation is 3.3&deg;F. The lowest is 64.0&deg;F, the highest is 85&deg;F. The 25% quartile is 73.0&deg;F, 50% quartile is 75.0&deg;F, 75% quartile is 77.0&deg;F. Nice temperature. 

In December, there are 1405 precipitation records. The mean is 0.21 inches, standard deviation is 0.54 inches.  
There are total 1517 temperature records. The mean is 71.0&deg;F, the standard deviation is 3.7&deg;F. The lowest is 56.0&deg;F, the highest is 83&deg;F. The 25% quartile is 69.0&deg;F, 50% quartile is 71.0&deg;F, the 75% quartile is 74.0&deg;F. 

From precipitation box-and-whisker plot, both June and December are typically without rains. While both June and December have heavy raining days, the heaviest rainfall happens in December.  
![Fig 1](https://github.com/pqrt12/surfs_up/blob/master/Fig_1.png)  
The June temperature is great for beach going in Oahu. Average temperature is about 3.9&deg;F higher than in December. The "chilly" day temperature records in June are much closer to the box. There are a lot more extreme "chilly" days in December.  
![Fig_2](https://github.com/pqrt12/surfs_up/blob/master/Fig_2.png)  

The precipitation is analyzed per rainfall, it would have been more meaningful in terms of days when the rainfall exceeds a certain threshold, for example half an inch.  
While both temperature and precipitation are analyzed across all stations, it would be more precise if we focus on the data from the nearby stations.  

