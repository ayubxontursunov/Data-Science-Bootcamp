# analytics.py
import logging
from random import randint
import requests
import config

# Configure logging
logging.basicConfig(
    filename='analytics.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class Research:
    def __init__(self, path):
        self.path = path
        logger.debug(f'Initialized Research with path: {path}')

    def file_reader(self, has_header=True):
        logger.debug('Reading file...')
        try:
            with open(self.path, 'r') as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]

            if has_header:
                lines = lines[1:]  # Skip header

            data = []
            for line in lines:
                parts = line.split(',')
                if len(parts) != 2:
                    raise ValueError(f"Invalid line format: {line}")
                if not all(part in ['0', '1'] for part in parts):
                    raise ValueError(f"Invalid values: {line}")
                data.append([int(parts[0]), int(parts[1])])

            logger.debug(f'Read {len(data)} data entries.')
            return data
        except Exception as e:
            logger.error(f'Error reading file: {e}')
            raise

    class Calculations:
        def counts(self, data):
            logger.debug('Calculating counts of heads and tails...')
            head_count = sum(pair[0] for pair in data)
            tail_count = sum(pair[1] for pair in data)
            logger.debug(f'Heads: {head_count}, Tails: {tail_count}')
            return head_count, tail_count

        def fractions(self, heads, tails):
            logger.debug('Calculating fractions...')
            total = heads + tails
            if total == 0:
                logger.warning('Total observations are zero.')
                return 0.0, 0.0
            head_frac = (heads / total) * 100
            tail_frac = (tails / total) * 100
            logger.debug(f'Head fraction: {head_frac}%, Tail fraction: {tail_frac}%')
            return head_frac, tail_frac

    class Analytics(Calculations):
        def predict_random(self, total):
            logger.debug(f'Generating {total} random predictions...')
            predictions = [[x, 1 - x] for x in (randint(0, 1) for _ in range(total))]
            logger.debug(f'Predictions: {predictions}')
            return predictions

        def predict_last(self, data):
            logger.debug('Fetching last prediction...')
            return data[-1] if data else None

        def save_file(self, data, filename, extension):
            logger.debug(f'Saving data to {filename}.{extension}...')
            try:
                with open(f"{filename}.{extension}", 'w') as file:
                    for line in data:
                        file.write(f"{line}\n")
                logger.debug('Data saved successfully.')
            except Exception as e:
                logger.error(f'Error saving file: {e}')
                raise

        def send_telegram_message(self, message):
            logger.debug('Sending message to Telegram...')
            try:
                url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    'chat_id': config.TELEGRAM_CHAT_ID,
                    'text': message
                }
                response = requests.post(url, data=payload)
                if response.status_code == 200:
                    logger.debug('Message sent successfully.')
                else:
                    logger.error(f'Failed to send message: {response.status_code}')
            except Exception as e:
                logger.error(f'Error sending Telegram message: {e}')
                raise
