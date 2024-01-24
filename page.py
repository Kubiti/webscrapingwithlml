page_number = 2
url = f'a{f"?page={page_number}" if page_number != 1 else ""}'
print(url)