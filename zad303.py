format24 =input('Enter time (24-hour format): ')

hours, minutes = map(int,format24.split(':'))
try:
    if 0 <= hours < 24 and 0 <= minutes < 60:
        if hours < 12:
            period = "am"
            if hours == 12:
                hours = 0
        if hours > 12:
            period = 'pm'
            hours -= 12
    print(f"Time in 12-hour format{hours}:{minutes}{period}")
except ValueError:
    print("Niepoprawny format czasu.")
