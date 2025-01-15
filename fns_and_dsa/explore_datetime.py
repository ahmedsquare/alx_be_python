from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ",current_date)

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date:  "))
    future_date  = (datetime.now() + timedelta(days=10))
    print("Future date: " , future_date.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()