# Lok-Sabha-Elections-2024 

KEY INSIGHTS OF THE GENERAL ELECTIONS 2024
1.	BJP Dominance: The Bharatiya Janata Party (BJP) was the first party, gaining 240 places out of 543 (ECI Results).

2.	Congress Performance: The Indian National Congress (INC) won 99 places, leading it to be the second largest party in the Lok Sabha (ECI Results).

3.	Regional Parties' Influence: The public should remember that the SP got 37 seats, AITC got 29 seats, and DMK got 22 seats, and therefore these are the main regional parties (ECI Results).

4.	Kerala's Results: Contrariwise, INC won just 9 seats, whereas the other 35 seats succeeded the Kerala Congress (KEC), among the Indian Union Muslim League (IUML), CPI(M), BJP, and RSPi (ECI Results).

5.	Punjab's Landscape: However, the INC bagged 7 seats in Punjab, the Aam Aadmi Party (AAP) 3 seats and the rest were won by the SAD and Independents (ECI Results).

6.	Maharashtra's Split: In Maharashtra, the election of BJP to the Central power in the state with 9 seats while Shiv Sena dominating the local power was the main highlight (ECI Results).

7.	BJP in Delhi: The BJP took full advantage of the situation and won all of Delhi's 7 parliamentary constituencies(ECI Results).

8.	Independent Candidates: Independent contenders won 7 seats across the country which demonstrates the difference in political preferences by regions(ECI Results).

9.	The winners posted by Janata Dal (United) (12 seats), Shiv Sena (Uddhav Balasaheb Thackrey Faction) (9 seats), and Nationalist Congress Party (NCP) (8 seats) are the most miniature parties there in their states  (ECI Results)  (ECI Results).

10.	Apart from a general trend of the high voter turnout that was noticed and the way the electorate was engaged in the states, we can say that every state had such a style of administration that reflected the variability and division of the political entities of India.


CODE Details:

1. Imports and URL List:
   - The script imports `requests` for making HTTP requests, `BeautifulSoup` from `bs4` for parsing HTML, `csv` for handling CSV files, and `os` for file path operations.
   - It defines a list of URLs to scrape election data from.

2. Fetch and Parse Function:
   - `fetch_and_parse(url)`: Fetches the content of the URL using `requests.get()` and parses it using `BeautifulSoup`. It returns a `BeautifulSoup` object if the request is successful, otherwise prints an error message.

3. Downloads Directory:
   - Determines the path to the user's Downloads directory using `os.path.expanduser('~/Downloads')`.

4. Scrape and Save Function:
   - `scrape_and_save(url, filename)`: Fetches and parses the HTML from the given URL. Opens a CSV file in the Downloads directory for writing data.
   - Iterates through HTML tables and rows, extracting and writing data to the CSV file while skipping unwanted rows and headers.

5. Writing Data to CSV:
   - Writes the table headers only once and then writes each row of data to the CSV file. Ensures no extra newlines are added by using `newline=''`.

6. Scraping Loop:
   - Iterates over the list of URLs, generates a CSV filename based on the URL, and calls `scrape_and_save` to scrape the data and save it to the corresponding CSV file. 

This script systematically fetches election data from specified URLs and saves the parsed data into CSV files in the user's Downloads directory.
