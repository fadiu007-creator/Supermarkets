from collectors.http_public import collect_public_page

VIVA_URL = "https://online.vivafresh.shop/"


def collect_viva():
    return collect_public_page("viva-fresh", VIVA_URL)
