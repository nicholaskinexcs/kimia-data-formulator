# kimia-data-formulator

## Event data format:
Event data have the following format when they are fetched as CSV files from S3

2021-03-17 16:49:26.000,15,EF:3D:FC:5F:BC:BB,f1fc0d5b-53a8-4fdc-a593-77243fd8218e,4,14,419.0,4291

Column 1: time stamp when the data is collected by Kimia <br/>
Column 2: Event Type (see below for reference)<br/>
Column 3: Device ID <br/>
Column 4: User ID <br/>
Column 5: Absolute MIN ROM (in degrees)<br/>
Column 6: Absolute MAX ROM (in degrees)<br/>
Column 7: Event count (automatically increments)<br/>
Column 8: Duration <br/>

## Position data format:

2021-03-17 15:40:46.000,10,EF:3D:FC:5F:BC:BB,f1fc0d5b-53a8-4fdc-a593-77243fd8218e

Column 1: time stamp when the data is collected by Kimia <br/>
Column 2: Event Type (see below for reference)<br/>
Column 3: Device ID <br/>
Column 4: User ID <br/>

## Event type enum definition

BE_STEP_WALK = 0; <br>
BE_STEP_JOG = 1; <br>
BE_SQUAT = 2; <br>
LIE_DOWN = 3; <br>
SIT_DOWN = 4; <br>
STAND_UP = 5; <br>
ICE_KNEE_START = 6; <br>
ICE_KNEE_FINISH = 7; <br>
DEVICE_REMOVED = 8; <br>
DEVICE_PLACED = 9; <br>
BUFFER_FINISHED = 10;<br>
ICE_KNEE_FAIL = 11;<br>
ELEVATED_LIE_DOWN = 12;<br>
ELEVATED_SIT_DOWN = 13;<br>
MOVING = 14;<br>
FLEX_EXTENSION = 15;<br>
TEMP_CHANGE = 16;<br>