import datetime

class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer

#print(now.year, now.month, now.day, now.hour, now.minute, now.second)