data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

x = input("Введите страну")
y = len(data)
if x in data:
    print(data.get(x, "not found"))
else:
    print("not found")
