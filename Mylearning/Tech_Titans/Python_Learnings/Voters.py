user_name = input("Please input your name:")
user_country = input("Please provide the name of your country:")
user_age = input("Kindly provide your age:")

name = str(user_name)
country = str(user_country)
age = int(user_age)

if age < 18:
    vote_right = "Not Eligible"
    
else:
    vote_right = "Eligible"
    
"""F-string"""
print(f"{name} is {vote_right} to vote in {country}")

"""Modulus operator"""
print("%s is %s to vote in %s" % (name, vote_right, country))    
