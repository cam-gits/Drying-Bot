from xml.etree import ElementTree
import requests
from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'ACCESS_TOKEN',
    api_base_url = 'INSTANCE'
)

url = 'https://www.met.ie/Open_Data/xml/fcom.xml'
response = requests.get(url)
xml_root = ElementTree.fromstring(response.content)

for x in xml_root.findall('drying_conditions'):
    conditions =x.find('text').text

mastodon.status_post(conditions + "#Irish #Weather")