

def ts(h, m, tf):
    x = " "
    if tf == False and  h > 12:
         x = (f"{h - 12}:{m} PM")
    elif tf == False and h <= 12:
         x = (f"{h}:{m} AM")
    else:
        x = (f"{h}:{m}")
    return x

    
h = int(input("hours: "))
m = int(input("minutes: "))
tf = input('is Timeframe 24h? (y/n): ').lower().strip() == 'y'

print(ts(h, m, tf))




