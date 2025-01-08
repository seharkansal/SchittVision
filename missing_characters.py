from bs4 import BeautifulSoup
import requests
import csv

# List of URLs for episodes
urls = [
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16052',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16053',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16149',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16303',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16387',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16482',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16608',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16675',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16808',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=16932',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=17308',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=17490',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=17593',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=24677',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=24678',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=24813',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=24923',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=25032',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=25128',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=25272',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=25579',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=25694',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=25848',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=26044',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=26193',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=26305',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=30495',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=30613',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=30709',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=30810',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=30910',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=31039',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=31192',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32780',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32799',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32800',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32820',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32821',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32822',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33122',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33123',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33124',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33125',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33126',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33127',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33128',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33129',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33130',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33131',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33132',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33133',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33208',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32702',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32701',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32700',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32699',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32771',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32830',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32872',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=32955',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33034',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33100',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33262',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33315',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33362',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=33403',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35645',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35684',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35723',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35775',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35812',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35857',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35936',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=35982',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=36022',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=36057',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=36099',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=36165',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=36211',
    'https://transcripts.foreverdreaming.org/viewtopic.php?t=36236']

all_dialogues = []

# Loop through each URL
for url in urls:
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")

        # Initialize variables
        character = "unknown"  # Default character when no <strong> tag
        dialogues = []  # Store dialogues for the current episode

        # Loop through all elements in the HTML and find dialogues
        current_dialogue = []
        for element in soup.find_all(True):  # Find all tags
            if element.name == 'strong' and element.get('class') == ['text-strong']:
                # If it's a <strong> tag, we have a character name
                if current_dialogue:
                    # Add all previous dialogues as separate entries
                    for dialogue in current_dialogue:
                        dialogues.append((character, dialogue.strip()))
                # Set the new character
                character = element.text.strip()
                current_dialogue = []  # Reset current dialogue list for the new character
            elif element.name == 'br':
                # If it's a <br> tag, check if the previous element had text
                if element.previous_sibling and isinstance(element.previous_sibling, str):
                    text = element.previous_sibling.strip()
                    if text:  # Only add non-empty text
                        current_dialogue.append(text)

        # After the loop, ensure to save any remaining dialogue
        if current_dialogue:
            for dialogue in current_dialogue:
                if dialogue.strip():  # Only append non-empty dialogues
                    dialogues.append((character, dialogue.strip()))

        # Add the dialogues for this episode to the all_dialogues list
        all_dialogues.extend(dialogues)

    else:
        print(f"Failed to retrieve the page: {url}. Status code: {response.status_code}")

# Save the dialogues to a CSV file
with open('schitts_creek_combined_dialogues.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Character', 'Dialogue'])  # Write header

    # Write the collected dialogues
    for character, text in all_dialogues:
        writer.writerow([character, text])

print("Dialogues have been saved to schitts_creek_combined_dialogues.csv.")
