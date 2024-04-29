import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_team_players(team_url, player_data):
    r = requests.get(team_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all <li> elements containing player information
    player_elements = soup.find_all('li', class_='dys-box-color ih-pcard1')

    # Iterate through each player element to extract information
    for player in player_elements:
        
        player_name = player.find('div', class_='ih-p-name').find('h2').text.strip()
        player_photo = player.find('div', class_='ih-p-img').find('img')['data-src']
        team_name = player.find('a')['data-team_name']

        # Append data to the player_data list
        player_data.append({'Player Name': player_name, 'Player Photo': player_photo, 'Team Name': team_name})

# List to store URLs of IPL teams
team_urls = [
    "https://www.iplt20.com/teams/chennai-super-kings",
    "https://www.iplt20.com/teams/delhi-capitals",
    "https://www.iplt20.com/teams/gujarat-titans",
    "https://www.iplt20.com/teams/kolkata-knight-riders",
    "https://www.iplt20.com/teams/lucknow-super-giants",
    "https://www.iplt20.com/teams/mumbai-indians",
    "https://www.iplt20.com/teams/punjab-kings",
    "https://www.iplt20.com/teams/rajasthan-royals",
    "https://www.iplt20.com/teams/royal-challengers-bangalore",
    "https://www.iplt20.com/teams/sunrisers-hyderabad"
]

# List to store player data
all_player_data = []

for url in team_urls:
    scrape_team_players(url, all_player_data)

# Create a DataFrame from the scraped data
df = pd.DataFrame(all_player_data)

# Save the DataFrame to a CSV file
df.to_csv('ipl_player_images.csv', index=False)

print("Data scraped and saved to 'ipl_player_images.csv'.")
