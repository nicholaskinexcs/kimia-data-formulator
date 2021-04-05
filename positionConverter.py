import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

""" Converts raw S3 CSV to a list of (datetime, position) pair"""

def enum_switch(argument):
    switcher = {
        0: "Walk",
        1: "Jog",
        2: "Squat",
        3: "Lie down",
        4: "Sit",
        5: "Stand Up",
        6: "Ice Knee starts",
        7: "Ice Knee finished",
        8: "Device removed",
        9: "Device placed",
        10: "Buffer finished",
        11: "Ice knee",
        12: "Elevated lie down",
        13: "Elevated Sit",
        14: "Moving",
        15: "Flex/Ext",
        16: "Temperature Change"
    }
    return switcher[argument]


position_df = pd.read_csv('giovanni_position')

# Create a new DF for position containing only columns 0, 1
position_df_sliced = position_df.iloc[:, [0, 1]]

# Convert time stamps to list
position_time_stamp_string_list = position_df["timestamp"].tolist()
position_time_stamp_list = [dt.datetime.strptime(time_stamp_string, '%Y-%m-%d %H:%M:%S.%f').date() for time_stamp_string in position_time_stamp_string_list]

# Convert position type enum to descriptive string
position_enum_list = position_df["eventId"].tolist()
position_string_list = [ enum_switch(enum) for enum in position_enum_list]

outPutList = []
for time,event in zip(position_time_stamp_string_list, position_string_list):
    outPutList.append((time,event))

output_df = pd.DataFrame(outPutList, columns=["Time", "Event"])
output_df.to_csv("Output_csv", index=False)


