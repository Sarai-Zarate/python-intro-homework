day_of_week = input("What day is it? ").lower()
time_of_day = input("What time of day is it? morning, afternoon, or evening? ").lower()

if day_of_week == "monday" and time_of_day == "morning":
    print("It's Monday morning! Get ready for a fun week of python learning!")
elif day_of_week == "monday" and time_of_day == "afternoon":
    print("It's Monday afternoon! Don't forget to eat lunch to fuel your learning.")   
elif day_of_week == "monday" and time_of_day == "evening":
    print("It's Monday evening! Get your 8 hours of sleep!")
elif day_of_week == "wednesday" and time_of_day == "morning":
    print("It's Wednesday morning! Your week is half way through!")
elif day_of_week == "wednesday" and time_of_day == "afternoon":
    print("It's Wednesday afternoon. Humpday marks the middle of the week.")
elif day_of_week == "wednesday" and time_of_day == "evening":
    print("It's Wednesday evening. Getting so close to the weekend!")   
elif day_of_week == "saturday" and time_of_day == "morning":
    print("It's Saturday morning! Time for your weekly grocery run.")
elif day_of_week == "saturday" and time_of_day == "afternoon":
    print("It's Saturday afternoon! I know you love mowing the lawn.")
elif day_of_week == "saturday" and time_of_day == "evening":
    print("It's Saturday evening! You have church in the morning so go to bed soon.")
else:
    print("Uh, oh. We don't recognize your entry. Please try again.")    