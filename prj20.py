def process_string(title):
  vowels = "aeiouAEIOU"
  consonants = ""
  for char in title:
    if char not in vowels:
      consonants += "." + char.lower()
  return consonants

title = input("Please Enter a title: ")
result = process_string(title)

print("Result Title: " + result)