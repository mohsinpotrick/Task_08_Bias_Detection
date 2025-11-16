import pandas as pd

# ---------------------------
# PERIOD STATS
# ---------------------------
period_data = {
    "Period": ["1st", "2nd", "3rd", "4th", "OT1", "OT2"],
    "Goals_Syr": [74, 65, 48, 47, 0, 1],
    "Goals_Opp": [64, 52, 45, 59, 1, 0],
    "Saves_Syr": [43, 42, 37, 39, 1, 0],
    "Saves_Opp": [39, 48, 40, 39, 2, 0],
    "Shots_Syr": [145, 147, 129, 114, 2, 1],
    "Shots_Opp": [154, 143, 115, 138, 2, 0],
    "SOG_Syr": [113, 113, 88, 86, 2, 1],
    "SOG_Opp": [107, 94, 82, 98, 2, 0],
}

period_df = pd.DataFrame(period_data)

# ---------------------------
# PLAYER STATS
# ---------------------------
player_data = [
    ["Emma Ward",19,30,46,76,77,1,6,0,41,2],
    ["Caroline Trinkaus",19,32,11,43,72,4,6,8,16,5],
    ["Emma Muchnick",19,34,7,41,71,2,27,13,31,9],
    ["Gracie Britton",19,20,10,30,41,0,8,1,16,0],
    ["Alexa Vogelman",19,21,6,27,46,0,25,31,27,13],
    ["Mileena Cotter",19,21,2,23,50,1,11,24,26,10],
    ["Joely Caramelli",19,16,4,20,46,0,24,39,8,11],
    ["Molly Guzik",19,14,5,19,34,0,15,13,14,8],
    ["Ashlee Volpe",12,14,2,16,31,0,5,0,10,1],
    ["Olivia Adamson",3,10,6,16,18,1,2,5,7,1],
    ["Others",0,0,0,0,0,0,0,0,0,0], # shorten rest for sanity
]

player_df = pd.DataFrame(player_data, columns=[
    "Player","GP","G","A","Pts","Sh","Gw","GB","DC","TO","CT"
])

# ---------------------------
# TEAM STATS
# ---------------------------
team_stats = {
    "Goals_For": 235,
    "Goals_Against": 221,
    "Shots_For": 538,
    "Shots_Against": 552,
    "SOG_For": 403,
    "SOG_Against": 383,
    "GroundBalls": 295,
    "Turnovers": 270,
    "DrawControls": 240,
}

team_df = pd.DataFrame([team_stats])

