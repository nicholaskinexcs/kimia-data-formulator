import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


event_df = pd.read_csv('sample_event_gio')
position_df = pd.read_csv('sample_position_gio')

# Create a new DF for position containing only columns 0, 1
position_df_sliced = position_df.iloc[:, [0, 1]]

# Convert time stamps to list
event_time_stamp_string_list = event_df["timestamp"].tolist()
event_time_stamp_list = [dt.datetime.strptime(time_stamp_string, '%Y-%m-%d %H:%M:%S.%f').date() for time_stamp_string in event_time_stamp_string_list]
position_time_stamp_string_list = position_df["timestamp"].tolist()
position_time_stamp_list = [dt.datetime.strptime(time_stamp_string, '%Y-%m-%d %H:%M:%S.%f').date() for time_stamp_string in position_time_stamp_string_list]

# Convert minROM to list
min_ROM_list = event_df["minROM"].tolist()
max_ROM_list = event_df["maxROM"].tolist()

# position values to list
position_values = position_df["eventId"].tolist()

# Plot sample graph
# x axis values
x1 = event_time_stamp_list
x2 = position_time_stamp_list
# corresponding y axis values
y1 = max_ROM_list
y2 = min_ROM_list

# plotting the points
# plt.plot(event_time_stamp_string_list, y1)
# plt.plot(event_time_stamp_string_list, y2)
plt.plot(position_time_stamp_string_list, position_values)

# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('max rom')

# giving a title to my graph
plt.title('Max ROM graph')

# function to show the plot
plt.show()
