from requests_html import HTMLSession

def weather(query):
    s = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{query}'

    # Fetch the content of the page
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})

    # Extract temperature
    temp = r.html.find('span#wob_tm', first=True)
    if temp:
        temperature = temp.text
    else:
        temperature = "Temperature not found"

    # Extract unit
    unit = r.html.find('span#wob_unit', first=True)
    if unit:
        temperature_unit = unit.text
    else:
        temperature_unit = "Unit not found"

    # Extract weather description
    desc = r.html.find('span#wob_dc', first=True)
    if desc:
        description = desc.text
    else:
        description = "Description not found"

    return f"{temperature} {temperature_unit} - {description}"
