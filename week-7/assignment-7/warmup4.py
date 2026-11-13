# Use datetime.now() and .strftime() to print today's date (the day you turn the script)

from datetime import datetime
current_date = datetime.now()
readable_date = current_date.strftime("%B %d, %Y")
print(f"Today is {readable_date}.")


