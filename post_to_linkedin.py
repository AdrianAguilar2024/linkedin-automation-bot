import os
import json
import random
import requests

# --- CONFIGURATION ---
# The numeric ID of your LinkedIn Company Page that you found in the URL.
# IMPORTANT: Replace the text inside the quotes with YOUR actual Company Page ID.
COMPANY_URN = "urn:li:company:108093402" 
# --- END CONFIGURATION ---


# This function posts the message to LinkedIn
def post_to_linkedin(company_urn, post_text):
    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    if not access_token:
        print("Error: LINKEDIN_ACCESS_TOKEN secret not found.")
        exit()
    if "REPLACE_WITH_YOUR_COMPANY_ID" in company_urn:
        print("Error: Please replace 'REPLACE_WITH_YOUR_COMPANY_ID' in the COMPANY_URN variable in the Python script.")
        exit()

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }

    post_data = {
        "author": company_urn, # We are now using the Company URN as the author
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

# 4. Post to LinkedIn using the Company ID
post_to_linkedin(COMPANY_URN, post_text)
