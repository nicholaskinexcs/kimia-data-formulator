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


event_df = pd.read_csv('giovanni_event')

# Convert time stamps to list
position_time_stamp_string_list = event_df["timestamp"].tolist()

# Convert position type enum to descriptive string
position_enum_list = event_df["eventId"].tolist()
position_string_list = [ enum_switch(enum) for enum in position_enum_list]

# Get Max and Min Angles
maxROM_list = event_df["maxROM"].tolist()
minROM_list = event_df["minROM"].tolist()

outPutList = []
for time,event,maxROM,minROM in zip(position_time_stamp_string_list, position_string_list,maxROM_list,minROM_list):
    outPutList.append((time,event,maxROM,minROM))

output_df = pd.DataFrame(outPutList, columns=["Time", "Event", "maxROM", "minROM"])
output_df.to_csv("event_output_csv", index=False)


