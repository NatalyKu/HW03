from datetime import datetime

def get_days_from_today(date):
    your_date = datetime.strptime(date, "%Y-%m-%d")
    today_date = datetime.today()
    diff = (today_date - your_date)
    
    return (diff.days)


print (get_days_from_today('2024-06-10'))

