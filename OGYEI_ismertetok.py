import datetime
import urllib.request
import os

month_names = [
    "januar",
    "februar",
    "marcius",
    "aprilis",
    "majus",
    "junius",
    "julius",
    "augusztus",
    "szeptember",
    "oktober",
    "november",
    "december"
]

url_template = "https://ogyei.gov.hu/dynamic/ismertetok_%Y{month}%d.xlsx"
output_folder = "c:/Tamás/Egis/OGYEI/2/"

start_date = datetime.date(2014, 1, 1)
end_date = datetime.date.today()

delta = datetime.timedelta(days=1)
current_date = start_date

while current_date <= end_date:
    month = month_names[current_date.month - 1]
    url = current_date.strftime(url_template.format(month=month))
    filename = os.path.join(output_folder, f"ismertetok_{current_date.strftime('%Y%m%d')}.xlsx")

    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Letöltve: {filename}")
    except urllib.error.HTTPError:
        print(f"A(z) {url} URL nem érhető el.")

    current_date += delta
