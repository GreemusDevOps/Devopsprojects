#to count vowels in a string
def vowel_count(string):
    vowels="AEIOUaeiou"
    count=len([char for char in string if char in vowels])
    print("Count of vowels:", count)
string="HAI My Name is Durga"
vowel_count(string)
  