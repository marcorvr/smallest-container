import logging
import datetime
import time

LOG_FORMAT = "%(levelname)s - %(name)s - %(funcName)s - %(thread)d - %(message)s"

logger = logging.getLogger('SimpleClock')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():
    logger.info("LEVELNAME - NAME - FUNCNAME - THREAD - MESSAGE")
    while True:
        time_of_day = datetime.datetime.now()
        logger.info(f"The time is: {datetime.date.today().isoformat()} @ {time_of_day.hour}:{time_of_day.minute}:{time_of_day.second}")
        # print(f"The time is: {datetime.date.today().isoformat()} @ {time_of_day.hour}:{time_of_day.minute}:{time_of_day.second}")
        time.sleep(10)

if __name__ == "__main__":
    main()
