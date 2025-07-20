from datetime import datetime
from zoneinfo import ZoneInfo

CZECH_TIMEZONE = ZoneInfo("Europe/Prague")

if __name__ == "__main__":
    utc_time = datetime(2025, 10, 26, 3, 3, tzinfo=ZoneInfo("UTC"))
    cet_time = datetime(2025, 10, 26, 3, 3, tzinfo=CZECH_TIMEZONE)

    print(f"UTC:    {utc_time}")
    print(f"Prague: {cet_time}")

