> ********NOTE********  
> This project is fully functional, but the live automation is currently paused. The LinkedIn API requires apps to be approved for the **"Community Management API"** product before they can post to a Company Page. My application for this access has been submitted, and I am awaiting approval from LinkedIn.
>
> Once approved, the daily posting to my [**Aguilar Software Engineer**](https://www.linkedin.com/company/YOUR_COMPANY_PAGE_URL) page will resume automatically. All code and workflow configurations are complete and correct for when access is granted.
>
> This process has been a valuable lesson in navigating official API documentation, permission scopes, and developer approval queues.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# LinkedIn "Tech Term of the Day" Automation Bot

![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![GitHub Actions Status](https://github.com/AdrianAguilar2024/linkedin-automation-bot/actions/workflows/linkedin-poster.yml/badge.svg)

This project is a fully automated Python script that posts a "Tech Term of the Day" to a designated LinkedIn Company Page every day. It is designed to consistently build a professional presence and demonstrate practical skills in API integration, automation, and secure credential management.

The live bot posts daily to my LinkedIn page: [**Adrian's Coding Projects**](https://www.linkedin.com/company/YOUR_COMPANY_PAGE_URL) <!-- Optional: Add a link to your company page! -->

---

## Why This Project?

As an aspiring developer, I wanted to create a hands-on project that went beyond simple scripts. This bot was the perfect opportunity to learn and showcase a variety of real-world skills:

*   **API Integration:** Interacting with the complex LinkedIn API, including handling authentication and sending data.
*   **Authentication (OAuth 2.0):** Navigating the entire OAuth 2.0 authorization flow to securely obtain API access tokens. This involved a significant amount of debugging and problem-solving to understand scopes, permissions, and request formats.
*   **Automation with GitHub Actions:** Writing a CI/CD workflow from scratch to run the script on a daily schedule, completely hands-free.
*   **Secure Credential Management:** Using GitHub Secrets to store and access sensitive API keys and tokens, following security best practices.
*   **Resilience and Debugging:** Working through multiple API errors (`403`, `422`, `401`), analyzing error messages, and adapting the approach to find a working solution.

This project demonstrates my ability to take an idea from concept to a fully functional, automated, and reliable final product.

## How It Works

The automation process is straightforward and efficient:

1.  **Scheduled Trigger:** A GitHub Actions workflow (`.github/workflows/linkedin-poster.yml`) is set to run on a daily `cron` schedule.
2.  **Environment Setup:** The workflow sets up a virtual environment, installs Python, and installs the necessary `requests` library.
3.  **Script Execution:** The main Python script, `post_to_linkedin.py`, is executed.
4.  **Content Selection:** The script reads from a simple `terms.json` file and randomly selects a tech term and its definition.
5.  **API Authentication:** The script retrieves the secure `LINKEDIN_ACCESS_TOKEN` from GitHub Secrets.
6.  **Post Creation:** It constructs the post content and sends it to the LinkedIn API's `/ugcPosts` endpoint, specifying the Company Page as the author.
7.  **Success or Failure:** The script logs the outcome of the API call, which can be viewed in the GitHub Actions run history.

## Technology Stack

*   **Language:** Python 3.10
*   **Key Libraries:** `requests`
*   **Platform:** GitHub
*   **Automation Engine:** GitHub Actions
*   **API:** LinkedIn API v2

---

## Setup and Installation

To run this project yourself, you will need to follow these steps.

### Prerequisites

*   A GitHub Account
*   A LinkedIn Account
*   Python 3.x installed locally (for testing, if desired)

### 1. Set Up the LinkedIn Application

This was the most challenging part of the project and requires careful setup.

1.  **Create a LinkedIn Company Page:** The API requires a Company Page to post on behalf of.
2.  **Create a LinkedIn Developer App:** Go to the [LinkedIn Developer Portal](https://developer.linkedin.com/home) and create a new app, linking it to your Company Page.
3.  **Add Required Products:** In your app's **"Products"** tab, you must request and be granted access to:
    *   **`Share on LinkedIn`**
    *   **`Community Management API`** (This is essential for posting as a company)
4.  **Generate an Access Token:**
    *   This project requires an OAuth 2.0 Access Token with the **`w_organization_social`** scope.
    *   You can use a tool like [Postman](https://www.postman.com/) or LinkedIn's own OAuth 2.0 tool to complete the 3-legged authorization flow and generate a token with this specific scope.

### 2. Configure Your GitHub Repository

1.  **Clone or Fork this Repository:**
    ```bash
    git clone https://github.com/AdrianAguilar2024/linkedin-automation-bot.git
    ```
2.  **Set Up GitHub Secrets:** For the automation to work, you must store your credentials securely. In your GitHub repository, go to **Settings > Secrets and variables > Actions** and create the following secrets:
    *   `LINKEDIN_ACCESS_TOKEN`: The powerful token with the `w_organization_social` scope you just generated.
    *   `LINKEDIN_CLIENT_ID`: Your app's Client ID.
    *   `LINKEDIN_CLIENT_SECRET`: Your app's Client Secret.
3.  **Update the Company URN:**
    *   In the `post_to_linkedin.py` file, find the `COMPANY_URN` variable.
    *   Replace the placeholder with your own Company Page's numeric ID (found in the URL of your Company Page).

### 3. Run the Workflow

The project is now configured! The workflow will run automatically on its schedule. To test it immediately, go to the **"Actions"** tab in your repository, select the **"Post Tech Term to LinkedIn"** workflow, and run it manually.

## Project Status

**Complete and Operational.** The bot is running on a daily schedule. Future improvements could include adding image support or expanding the list of tech terms.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
