# A bot posting to Mastodon via Pipedream

Follow this guide for instructions on opening an account for use with automation: https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/

Data source and licencing at https://data.gov.ie/en_GB/dataset/met-eireann-live-text-forecast-data/resource/92109c2e-00ef-4530-875c-becadd7f0d2f

Farming Commentary from Met Éireann updates daily at no set time. Bot set up to post every 24 hours.

---
## Pipedream Workflow:
1. Schedule (Daily)
2. Python > Run Python code
3. Test the connection:

```

from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'ACCESS_TOKEN',
    api_base_url = 'INSTANCE'
)

mastodon.status_post("hello world!")

``` 

4. If the account successfully posts this snippet can be replaced with the code in the .py and deployed


![image](https://github.com/cam-gits/Drying-Bot/assets/136761134/8a1b6f00-3f53-4086-9eb4-f7c71b844896)
