import pathlib
import os
import pandas as pd
import json


def read_data(file_path):
    """Read data from a JSON file and save it in a dataframe"""
    with open(file_path) as f:
        data = json.load(f)
    return pd.DataFrame(data)


def main():
    # Define file paths
    data_dir = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout')
    competition_file = os.path.join(data_dir, 'competitions.json')
    matches_file = os.path.join(data_dir, 'matches_England.json')
    players_file = os.path.join(data_dir, 'players.json')
    events_files = [os.path.join(data_dir, f'events_England_{i+1}.json') for i in range(13)]

    # Read data into dataframes
    df_competitions = read_data(competition_file)
    df_matches = read_data(matches_file)
    df_players = read_data(players_file)
    df_events = pd.concat([read_data(f) for f in events_files])

    # Print information about the dataframe structure
    print("Competitions dataframe:")
    df_competitions.info()

    print("\nMatches dataframe:")
    df_matches.info()

    print("\nPlayers dataframe:")
    df_players.info()

    print("\nEvents dataframe:")
    df_events.info()

if __name__ == '__main__':
    main()



# Before refactoring:
# # Import necessary libraries
# import pathlib
# import os
# import pandas as pd
# import json

# # This code snippet is using the Wyscout dataset to get information about competitions, matches, players, and events that occurred
# # during the 2017/18 Premier League season. It then saves this information into Pandas dataframes and provides some basic information
# # about the structure of the data.

# ##############################################################################
# # Competition data
# # ----------------------------
# # Read information about competitions from a JSON file and save it in a dataframe.
# # The path to the data file is specified as an absolute path using the Python pathlib module.

# path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'competitions.json')
# with open(path) as f:
#     data = json.load(f)
# df_competitions = pd.DataFrame(data)

# # Print information about the dataframe structure
# df_competitions.info()

# ##############################################################################
# # Match data
# # ----------------------------
# # Read information about matches from a JSON file and save it in a dataframe.

# path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'matches_England.json')
# with open(path) as f:
#     data = json.load(f)
# df_matches = pd.DataFrame(data)

# # Print information about the dataframe structure
# df_matches.info()

# ##############################################################################
# # Player data
# # ----------------------------
# # Read information about players from a JSON file and save it in a dataframe.

# path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'players.json')
# with open(path) as f:
#     data = json.load(f)
# df_players = pd.DataFrame(data)

# # Print information about the dataframe structure
# df_players.info()

# ##############################################################################
# # Event data
# # ----------------------------
# # Read information about events from multiple JSON files and concatenate them into a single dataframe.

# df_events = pd.DataFrame()
# for i in range(13):
#     file_name = 'events_England_' + str(i+1) + '.json'
#     path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', file_name)
#     with open(path) as f:
#         data = json.load(f)
#     df_events = pd.concat([df_events, pd.DataFrame(data)])

# # Print information about the dataframe structure
# df_events.info()

# ##############################################################################
# # Before you start
# # ----------------------------
# # Run these lines in Spyder/Jupyter notebook and explore dataframes 
# # to get more familiar before you start working on the course.