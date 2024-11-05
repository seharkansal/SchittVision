from bs4 import BeautifulSoup
import requests
import csv

url = 'https://transcripts.foreverdreaming.org/viewtopic.php?t=16052'

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, features="html.parser")

    # Find all dialogue elements
    dialogues = soup.find_all('strong', class_='text-strong')

    # Dictionary to hold dialogues for each character
    character_dialogues = {}
    #print(dialogues)
    # Loop through each dialogue
    for dialogue in dialogues:
        character = dialogue.text.strip()
        # Get the next text node after the character name
        next_node = dialogue.next_sibling
        print(character, next_node)
        #print(next_node)

        # Initialize list for the character if not already done
        if character not in character_dialogues:
            character_dialogues[character] = []

        # Loop through until we find a new character name or reach the end
        while next_node is not None:
            # Check if next_node is a <strong> (indicating a new character) or is None
            if next_node.name == 'strong':
                break
            
            # If next_node is a <br/> tag, skip it
            if next_node.name == 'br':
                next_node = next_node.next_sibling
                continue  # Skip <br/> tags

            # Only process if next_node is not None and is not a <br/>
            if next_node is not None and isinstance(next_node, str):
                # Check for non-empty text
                if next_node.strip():  # If there's text, append it
                    character_dialogues[character].append(next_node.strip())

            # Move to the next sibling
            next_node = next_node.next_sibling

     # Save the dialogues to a CSV file
    with open('schitts_creek_dialogues.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Character', 'Dialogue'])  # Write header

        # Write each character's dialogues
        for character, texts in character_dialogues.items():
            for text in texts:
                writer.writerow([character, text])  # Write character and dialogue

    print("Dialogues have been saved to schitts_creek_dialogues.csv.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")        