import datetime as dt

datetime = dt.datetime.now()
sec = datetime.timestamp()

print(f"Seconds since January 1, 1970: {sec:,.4f} or {sec:e} in scientific notation")
print(f"{datetime.strftime("%B %d %Y")}")