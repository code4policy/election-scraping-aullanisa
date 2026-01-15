# Elections scraping 
Let's use an LLM to create a scraper for the Massachusetts state electios website.

## Setup

### Set up your project environment
1. First, clone this repo
2. Set up your python virtual environment
    1. Just in case your virtual environemnt from yesterday is still active, run `deactivate`. If doing so gives you an error, don't worry!
    2. Create a new Python virtual environment: 
        ```sh
        python3 -m venv scrape_env
        ```
    3. Activate the new virtual environment: 
        ```sh 
        source ./scrape_env/bin/activate 
        ```
    4. Install the `lxml`, `requests`, and `BeautifulSoup` python libraries:
        ```sh
        pip install lxml requests beautifulsoup4
        ```

### Task instructions
1. Visit the website: https://electionstats.state.ma.us/elections/search/year_from:2024/year_to:2025
2. Inspect the page to identify the table where election data is stored:
    1. Right-click anywhere on the page > Click "Inspect" > find the table with election data
4. Check `robots.txt`: Visit https://electionstats.state.ma.us/robots.txt
5. Modify the IMDB scraper example to scrape the elections website. It should collect election data and save to elections.json. Feel free to vibe code this. 
6. Adjust your scraper to only grab 2025 elections. Hint: try manually adjusting the the year filters on the elections website. Does the URL change? 
7. Extract additional data fields!

