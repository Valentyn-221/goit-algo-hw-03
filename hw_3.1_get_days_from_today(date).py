from datetime import datetime, date, timedelta

def get_days_from_today(date):
    try:
        date_1 = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        print ((today-date_1).days)
        return (today-date_1).days
    
    except ValueError:
        print(f"{date} is not a str object")

 