import re


def get_max_page(headers):
    if headers:
        max_page_in_header = max([int(number) for number in re.findall(r'page=([0-9]+)>', headers)])
        return max_page_in_header if 'rel="last"' in headers else max_page_in_header + 1
    else:
        return 0
