from datetime import date

from dining import find_visiting_chefs_fmt
from slack import post_message

### FOR TESTING
from dotenv import load_dotenv
load_dotenv()

response = find_visiting_chefs_fmt(date.today())

if response != "":
    post_message(response)
