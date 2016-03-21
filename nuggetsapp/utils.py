import datetime

def date_for_days_from_today(dayCount): 
        today = datetime.date.today(); 
        return today - datetime.timedelta(days=dayCount)