### Dictionaries

### 1

month_conversions = {
    "Jan" : "January",
    "Feb" : "Februrary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

# conversions = month_conversions["Dec"]
# print(conversions)


### 2

# conversions = month_conversions.get("Dec")
# print(conversions)


### 3

# conversions = month_conversions.get("Decc")
# print(conversions)


### 4

# conversions = month_conversions.get("Decc", "Not a valid Key")
# print(conversions)