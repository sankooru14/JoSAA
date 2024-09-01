import csv
from bs4 import BeautifulSoup


def extract_table_data(html_content, round_number, year):
    soup = BeautifulSoup(html_content, 'html.parser')
    div = soup.find('div', class_='table-responsive')

    table = div.find('table')
    got_header = False
    table_data = []
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=True)
                    for cell in row.find_all(['td', 'th'])]

        if got_header == False:
            row_data.append("Year")
            row_data.append("round")

        else:
            row_data.append(str(year))
            row_data.append(str(round_number))

        if row_data[0].startswith("Indian Institute of Technology") or got_header == False:
            got_header = True
            table_data.append(row_data)

    return table_data


html_files = [
    ('round1_2023.html', 1),
    ('round2_2023.html', 2),
    ('round3_2023.html', 3),
    ('round4_2023.html', 4),
    ('round5_2023.html', 5),
    ('round6_2023.html', 6)
]


year = 2023


all_table_data = []
header_added = False


for file_name, round_number in html_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        html_content = file.read()
    round_data = extract_table_data(html_content, round_number, year)

    if header_added:

        round_data = round_data[1:]
    else:

        round_data = round_data
        header_added = True

    all_table_data.extend(round_data)


csv_file_path = 'merged_all_2023_.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(all_table_data)

print(f"Merged table data has been saved to {csv_file_path}")
