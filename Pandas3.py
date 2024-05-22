# Sample input data
data = {
    'Team A': ['Ind', 'Aus', 'Afg', 'SL', 'Aus'],
    'Team B': ['Pak', 'SL', 'Pak', 'Afg', 'SA'],
    'Winner': ['Ind', 'Aus', 'Pak', 'Afg', 'No result']
}

# Create the input DataFrame
input_df = pd.DataFrame(data)

# Get the list of unique team names
team_names = list(set(input_df['Team A'].tolist() + input_df['Team B'].tolist()))
no_of_teams = len(team_names)

# Initialize the result DataFrame
res = pd.DataFrame({'Team': team_names, 'Win': [0]*no_of_teams, 'Loss': [0]*no_of_teams, 'Draw': [0]*no_of_teams})

# Populate the result DataFrame
for name in team_names:
    res.loc[res['Team'] == name, 'Win'] = len(input_df[input_df['Winner'] == name])
    res.loc[res['Team'] == name, 'Loss'] = len(input_df[((input_df['Team A'] == name) | (input_df['Team B'] == name)) & (input_df['Winner'] != name) & (input_df['Winner'] != 'No result')])
    res.loc[res['Team'] == name, 'Draw'] = len(input_df[((input_df['Team A'] == name) | (input_df['Team B'] == name)) & (input_df['Winner'] == 'No result')])

# Print the result DataFrame
print(res)

'''
Output:
Team Win Loss Draw
Ind	1	0	0
Pak	1	1	0
Aus	1	0	1
SL	0	2	0
SA	0	0	1
Afg	1	1	0
'''
