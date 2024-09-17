import re
def extract_merchandise_value_in_usd(product_description):
    if product_description and (match := re.search(r"(\d+(\.\d+)?)", product_description)):
        return float(match.group(1))
