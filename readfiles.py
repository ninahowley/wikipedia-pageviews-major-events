import requests
from io import StringIO
import pandas as pd

from bs4 import BeautifulSoup
import db

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = "https://analytics.wikimedia.org/published/datasets/country_project_page/"

def get_dates() -> list[str]:
    """
    Visits the main webpages, which contains the list of all files names.
    Extracts the date from each file name to create a list of all possible dates
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        dates = [tr.text[:14] for tr in soup.find_all("tr") if '.tsv' in tr.text[:14]]
        return dates
    except Exception as e:
        print(e)
        return []

def top_1000(date: str) -> pd.DataFrame:
    """
    Retrieves the .tsv file for date given in the parameter
    Converts files into Pandas Dataframe and collects top 1000 articles in the US
    """
    try:
        response = requests.get(f"{url}/{date}", headers=headers)
        response.raise_for_status()
        tsv_content = StringIO(response.text)
        df = pd.read_csv(tsv_content, sep="\t", header=None)
        us_data = df[df.iloc[:,1] == "US"]
        return (us_data.sort_values(df.columns[-1], ascending=False)).head(1000)
    except Exception as e:
        print(e)
        return

def process_date(date: str) -> None:
    """
    Retrieves data and inserts into database
    """
    print(date)
    try:
        top = top_1000(date)
        for _, r in top.iterrows():
            search_key = r[4].encode('latin1').decode('utf-8')
            db.insert_pageview_data(date[:10], r[3], search_key, r[6])
    except Exception as e:
        print(e)
        return

# if __name__ == "__main__":
    # db.init_pageviews()
    # dates = get_dates()
    # for date in dates:
    #     process_date(date)