try:
    a = int("abc")
except (ValueError, TypeError):
    print("Error occurred")
