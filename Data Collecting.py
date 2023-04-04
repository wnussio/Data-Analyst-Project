import pandas as pd
from serpapi import GoogleSearch
from datetime import date

# Important thing at the beggining - SERP API is offering 100 data pulls mothly per one account ( 1 email )

# In my case i was looking for 'data analyst','data scientist' in country 'Poland' - i found different job offers
search_term = "[NAME OF JOB]"
search_location = "[COUNTRY]"

jobs=pd.DataFrame()

# API is generating only 10 offers per search. I was downloading data daily, so i didn't need to catch more than 100 ( 'date_posted:today' ).

# Unfortunatelly engine - google_jobs wasn't conneted to 'pracuj.pl' and 'olx.pl' which are very popular in Poland
for num in range(10):
    start = num * 10
    params = {
                "api_key": "[UNIQUE SERP API KEY]",
                "device": "desktop",
                "engine": "google_jobs",
                "google_domain": "google.com",
                "q": search_term,
                "location": search_location,
                "chips": "date_posted:today",
                "start": start,
            }

    search = GoogleSearch(params)
    results = search.get_dict()


    try:
        if results['error'] == "Google hasn't returned any results for this query.":
            break
    except KeyError:
            print(f"Getting SerpAPI data for page: {start}")
    else:
            continue

    x=pd.DataFrame(results['jobs_results'])
    jobs=pd.concat([jobs, x], axis=0)

# Part that saves data in raports, it is returning 'https://serpapi.com/search' in terminal - that's weird but working correctly
jobs.to_csv(f'C:/[LOCATION]/DataScientist{date.today()}.csv')