# Dictionary: Key-Value pairs, keys must be unique.
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}

print(monthConversions["Feb"])
print(monthConversions.get("Feb"))

# print(monthConversions["Luv"])  # Hibat dobna
print(monthConversions.get("Luv"))  # None
print(monthConversions.get("Luv", "Defalult value in case key param not found."))  # Defalult value in case key param not found.
