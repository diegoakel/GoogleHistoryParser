# Google History Parser
A parser for Google Chrome's history takeout.

It only takes your Google Chrome history json file (which you can get at https://myaccount.google.com/data-and-personalization) and creates a .csv file with the following data:

- Page transition
- Title
- Domain
- Year
- Month
- Day
- Hour
- Minute
- Second

I left URL, client_id and favicon_url out because I think it cannot give any useful insights, but it is easily addable through the toCSV function.

When reading "Title" data, you need to decode it with utf-8, with:

    title = data["Title"].decode("utf-8")