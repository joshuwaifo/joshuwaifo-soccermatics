# Import the Sbopen class from the mplsoccer library to open the Statsbomb data
from mplsoccer import Sbopen

# Create a parser object using the Sbopen class to open the data
parser = Sbopen()

# Explore competition data to find the competition of interest, which is identified by competition_id and season_id.
# The competition method returns a dataframe containing information about each competition, such as its name and ID.
df_competition = parser.competition()

# Display information about the competition dataframe
df_competition.info()

# Explore match data to find the match of interest, which is identified by competition_id and season_id.
# The match method returns a dataframe containing information about each match, such as the teams that played and their IDs.
df_match = parser.match(competition_id=72, season_id=30)

# Display information about the match dataframe
df_match.info()

# Explore lineup data to see the players who played in a specific match, identified by game_id.
# The lineup method returns a dataframe containing information about each player who played, such as their team and jersey number.
# NOTE: This section of code is currently commented out due to a change in data format.
# df_lineup = parser.lineup(69301)
# df_lineup.info()

# Explore event data to see the events that occurred in a specific match, identified by game_id.
# The event method returns several dataframes, including one for the events themselves, one for related events, 
# one for player tactics, and one for frozen frames with player position at the moment of shots.
df_event, df_related, df_freeze, df_tactics = parser.event(69301)
df_event.info()

# Explore 360 data, which includes the location of players during an event in addition to the location of the event itself.
# The frame method returns a dataframe with information on player positions during the event, and the visible method 
# returns information on the part of the pitch that was tracked during the event.
df_frame, df_visible = parser.frame(3788741)
df_frame.info()

# Encourage the user to explore the dataframes before beginning any project or analysis
# to become more familiar with the data.


