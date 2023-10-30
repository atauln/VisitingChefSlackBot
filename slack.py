import os
import logging
import time
from datetime import datetime
from slack_sdk import WebClient as SlackWebClient
from slack_sdk.errors import SlackApiError

from dining import find_visiting_chefs_fmt

### FOR TESTING
from dotenv import load_dotenv
load_dotenv()

client = SlackWebClient(
    token = os.environ.get("SLACK_BOT_TOKEN")
)

logger = logging.getLogger(__name__)

def post_message(message: str):
    try:
        result = client.chat_postMessage(
            channel = os.environ.get("SLACK_LUNCH_CHANNEL"),
            text = message
        )
        print(result)
    except SlackApiError as e:
        print(f"Error posting message in <!{channel}>: {e}")

def main():
    print(f"Current Time @ Start: {datetime.now().strftime('%H:%M')}")
    print(f"Current target: {os.environ.get('SLACK_SCHEDULED_HOUR')}:{os.environ.get('SLACK_SCHEDULED_MINUTE')} (-{os.environ.get('UTC_OFFSET')}:00 Offset)")
    
    while (True):
        current_datetime = datetime.now()
        if int(current_datetime.strftime("%H")) - int(os.environ.get("UTC_OFFSET")) == int(os.environ.get("SLACK_SCHEDULED_HOUR")) and current_datetime.minute == int(os.environ.get("SLACK_SCHEDULED_MINUTE")):
            post_message(find_visiting_chefs_fmt(current_datetime))
        time.sleep(60)

if __name__ == "__main__":
    main()
