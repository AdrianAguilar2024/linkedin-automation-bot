import os
import json
import random
import requests

# This function gets your LinkedIn person URN (your unique ID)
def get_person_urn():
    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    if not access_token:
        print("Error: LINKEDIN_ACCESS_TOKEN not found.")
        return None
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get('https://api.linkedin.com/v2/userinfo', headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            # The URN is usually in the 'sub' field
            person_urn = f"urn:li:person:{user_info['sub']}"
            print(f"Successfully found Person URN: {person_urn}")
            return person_urn
        else:
            print(f"Error fetching user info: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An exception occurred while fetching user info: {e}")
        return None

# This function posts the message to LinkedIn
def post_to_linkedin(person_urn, post_text):
    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }

    post_data = {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post_text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    try:
        response = requests.post(
            "https://api.linkedin.com/v2/ugcPosts",
            headers=headers,
            json=post_data
        )
        if response.status_code == 201:
            print("Success! Post was shared on LinkedIn.")
        else:
            print("Error posting to LinkedIn.")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"An exception occurred during posting: {e}")


# --- MAIN SCRIPT ---

# 1. Load our dictionary of tech terms
try:
    with open("terms.json", "r") as f:
        terms = json.load(f)
except Exception as e:
    print(f"Error reading terms.json: {e}")
    exit()

# 2. Pick a random term
random_term = random.choice(terms)
term = random_term["term"]
definition = random_term["definition"]

# 3. Create the text for our post
post_text = f"""Todays #TechTermOfTheDay is: {term}

{definition}

#Python #Automation #LearnToCode #Coding #Developer #Tech
"""

print(f"Preparing to post: {post_text}")

# 4. Get the user's ID and then post to LinkedIn
person_id = get_person_urn()
if person_id:
    post_to_linkedin(person_id, post_text)
