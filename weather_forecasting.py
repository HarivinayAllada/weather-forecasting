# importing requests module
import requests

print("Welcome to the Weather Forecasting")
print("Enter the city name that you want to know the weather\n\n")

# takes input from the user
# make sure that the first letter in city name is always capital
city = input("Enter the name of the city : ")
print("\n\n")


# Function to generate report
def gen_report(c):
    # to get the information of weather from the below url
    url = 'https://wttr.in/{}'.format(c)

    # performing exception operation
    try:
        data = requests.get(url)
        t = data.text
    except:
        t = "Error Occurred"
    print(t)


gen_report(city)


