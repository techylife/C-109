import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("C-109_project.csv")
data = df["math score"].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)
first_stdev_limit_lower, first_stdev_limit_upper = mean-stdev, mean+stdev
second_stdev_limit_lower, second_stdev_limit_upper = mean-2*stdev, mean+2*stdev
third_stdev_limit_lower, third_stdev_limit_upper = mean-3*stdev, mean+3*stdev
first_stdev = [result for result in data if result > first_stdev_limit_lower and result < first_stdev_limit_upper]
third_stdev = [result for result in data if result > second_stdev_limit_lower and result < second_stdev_limit_upper]
second_stdev = [result for result in data if result > third_stdev_limit_lower and result < third_stdev_limit_upper]

percentage_first_stdev = round(len(first_stdev)/len(data)*100,1)
percentage_second_stdev = round(len(second_stdev)/len(data)*100,1)
percentage_third_stdev = round(len(third_stdev)/len(data)*100,1)

print(f"The mean of the math scores is {mean}\nThe median of the math score data is {median}\nThe mode of the math score data is {mode}\nThe standard deviation of the math score data is {stdev}\n\n")

print(f"There lies {percentage_first_stdev}% of the data within the first standarad deviation\nThere lies {percentage_second_stdev}% of the data within the second standard deviation\nThere lies {percentage_third_stdev}% of data within the third standard deviaiton")