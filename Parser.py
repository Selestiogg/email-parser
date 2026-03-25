from bs4 import BeautifulSoup
import requests
import re
from fake_useragent import UserAgent
ua = UserAgent()

url = input()

try:
    headers = {'User-Agent': ua.random}
    response = requests.get(url, timeout=10, headers=headers)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"Ошибка при загрузке страницы: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

find_mail = re.findall(r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}', response.text)

unique_emails = sorted(set(find_mail))


with open('emails.txt', 'w', encoding='utf-8') as file:
    for email in unique_emails:
        file.write(email + '\n')
print(f"Сохранено {len(unique_emails)} email-адресов в файл emails.txt")