from tkinter import Menu, StringVar, _setit
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
from requests.auth import HTTPBasicAuth
from tkinter import *
import requests
import calendar


# option to select if you want the weather forecast for a day or a week
# if you choose day, you can choose which day and display temps for every hour from midnight to midnight on a graph
# if you choose week than display the temp for the next 7 days starting today, show midday and midnight temps for everyday on a graph

coordinates = {"Warsaw": "52.24081,16.54513",
               "London": "51.50722,-0.12750",
               "New York": "40.71278,-74.00602",
               "Paris": "48.85661,2.35222",
               "Berlin": "52.52001,13.40495",
               "Tokyo": "35.68284,139.75945",
               "Barcelona": "41.38506,2.17340"}
locations = ["Warsaw", "London", "New York", "Paris", "Berlin", "Tokyo", "Barcelona"]
# Check current date, to make selecting the day accurate
date = str(datetime.now())
date = date[:10]
print(date)

# Main window
window = Tk()
window.attributes('-fullscreen', True)
window.title('Weather Forecast')
var = StringVar(window)


#custom setit function to allow displaying days in relation to the month
def custom_setit(var, choice, extra_action=None):
    def combined_action():
        _setit(var, choice)()  # Call `_setit` to update `var`
        if extra_action:
            extra_action()  # Run additional command

    return combined_action


#check number of days in month, used mainly to make sure that the get weather for the week function skips to the next month when it reaches the end of the current one
def get_days_in_month(year, month):
    _, num_days = calendar.monthrange(year, month)
    return int(num_days)

monthDays = {
    '01': 31,
    '02': 28,  # 29 in leap years
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
}
# days option menu
# create list of possible days to choose from, if the month ends go back to 1
days = []
day1 = 1
days.append(int(date[8:10]) - 1)

for i in range(10):
    maxDays = monthDays[str(date[5:7])]
    if maxDays in days:
        days.append(day1)
        day1 += 1
    else:
        days.append(int(date[8:10]) + i)

beginMonth = []
endMonth = []
for dayy in days:
    if dayy < 15:
        beginMonth.append(dayy)
    elif dayy > 15:
        endMonth.append(dayy)

# list of months to choose from, default is the current month, however 2 months are available if in range of 11 days
months = [int(date[5:7])]
if max(days) > 28:
    months.append(int(date[5:7]) + 1)


# functions and frames to display and update the date as the user edits his choice
# receives the users inputted date, and passes it into a function that displays the date selected
def displayYear(selection):
    year = selection
    labelYear.config(text=year)


def displayMonth(selection):
    month = selection
    print(f"Selected month: {month}")
    labelMonth.config(text=month)  # Update month label

    # Filter days based on the selected month
    if month == max(months):  # Example: filtering days for February (shorter month)
        filtered_days = beginMonth  # Adjust as needed based on month
    else:
        filtered_days = endMonth  # Default to the end month range

    # Update the day OptionMenu based on the filtered days
    day_menu = d['menu']
    day_menu.delete(0, 'end')  # Clear current day options

    for day in filtered_days:
        # Use `custom_setit` to set `variableDay` and update label via `displayDay`
        day_menu.add_command(label=day, command=custom_setit(variable3, day, lambda d=day: displayDay(d)))


def displayDay(selection):
    daySelected = selection
    print(f"Selected day: {daySelected}")
    labelDay.config(text=daySelected)


def displayLocation(selection):
    location = selection
    labelLocation.config(text=location)


# frame that holds the date and location selection OptionMenus
frame = Frame(window, bg='light blue', bd=5, relief=RAISED)
frame.pack(side=TOP)

# select date label
chooseDateLabel = Label(frame, text="Select date: ")
chooseDateLabel.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7', relief=RAISED)
chooseDateLabel.pack(side=LEFT)

# OptionMenus year-month-day
variable1 = StringVar(frame, "Year")
y = OptionMenu(frame, variable1, date[:4], command=displayYear)
y.config(indicatoron=False, fg='#484F51', bg='#71BFD7', font=('Sans serif', 12), relief=RAISED)
y.pack(side=LEFT)

variable2 = StringVar(frame, "Month")
m = OptionMenu(frame, variable2, command=displayMonth, *months)
m.config(indicatoron=False, fg='#484F51', bg='#71BFD7', font=('Sans serif', 12), relief=RAISED)
m.pack(side=LEFT)

variable3 = StringVar(frame, "Day")
d = OptionMenu(frame, variable3, command=displayDay, *days)
d.config(indicatoron=False, fg='#484F51', bg='#71BFD7', font=('Sans serif', 12), relief=RAISED)
d.pack(side=LEFT)

# frame that holds the displayed date
frameDate = Frame(window, bg='#71BFD7', bd=5, relief=RAISED, padx=10, pady=10)
frameDate.pack(side=TOP)

# displays previously selected date
labelDate = Label(frameDate, text="DATE: ")
labelDate.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')
labelDate.pack(side=LEFT)

labelYear = Label(frameDate, text="Year")
labelYear.pack(side=LEFT)
labelYear.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')
labelDash1 = Label(frameDate, text="-")
labelDash1.pack(side=LEFT)
labelDash1.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')

labelMonth = Label(frameDate, text="Month")
labelMonth.pack(side=LEFT)
labelMonth.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')
labelDash2 = Label(frameDate, text="-")
labelDash2.pack(side=LEFT)
labelDash2.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')

labelDay = Label(frameDate, text="Day")
labelDay.pack(side=LEFT)
labelDay.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')
labelDash3 = Label(frameDate, text=" ")
labelDash3.pack(side=LEFT)
labelDash3.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')

#Location and coordinates
#Select location label
chooseLocationLabel = Label(frame, text="Select location: ")
chooseLocationLabel.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7', relief=RAISED)
chooseLocationLabel.pack(side=LEFT)

#Optionmenu locations
variable4 = StringVar(frame, "Location")
y = OptionMenu(frame, variable4, command=displayLocation, *locations)
y.config(indicatoron=False, fg='#484F51', bg='#71BFD7', font=('Sans serif', 12), relief=RAISED)
y.pack(side=LEFT)

# frame that holds the displayed location
frameLocation = Frame(window, bg='#71BFD7', bd=5, relief=RAISED, padx=10, pady=10)
frameLocation.pack(side=TOP)

# displays previously selected location
labelLocation = Label(frameLocation, text="LOCATION:")
labelLocation.config(font=('Sans serif', 20), fg='#484F51', bg='#71BFD7')
labelLocation.pack(side=LEFT)


# weather for a chosen day (from midnight to midnight)
# possible choice of location (any location if possible, else a choice of previously selected latitudes and longitudes)
def weatherForecast(year, month, day, location):
    # earliest possible time is the day before at midnight
    # latest possible time is 10 days ahead
    print(location)
    time = '00'
    dateWeather = str(datetime(year, month, day)).removesuffix(" 00:00:00")
    print(dateWeather)

    url = f"https://api.meteomatics.com/{dateWeather}T{time}:00:00Z--{dateWeather}T{str(int(time) + 23)}:00:00Z:PT1H/t_2m:C/{location}/json"
    response = requests.get(url, auth=HTTPBasicAuth('self_madyavanhu_dominik', 'eddO7j82JE'))
    print(f"Response: {response}")
    data = response.json()  # Assuming the response is in JSON format
    print(data)

    result = []
    for j in range(24):
        weatherForecastDate = data['data'][0]['coordinates'][0]['dates'][j]['date'][
                              11:16]  # Extract time part from date
        temperature = data['data'][0]['coordinates'][0]['dates'][j]['value']  # Get temperature
        result.append((weatherForecastDate, temperature))  # Append tuple (date, temperature)
    return result


# weather for the following week
def weatherForecastWeekDay(location):
    timeDay = '14'
    dateWeek = str(datetime.now())
    dateWeekBegin = dateWeek[0:10]
    dayEnd = str(int(date[8:10]) + 7)
    endOfMonthDay = 0

    print(dateWeek)

    year = int(dateWeek[:4])
    month = int(dateWeek[5:7])

    daysInMonth = get_days_in_month(year, month)
    for day in range(endOfMonthDay, daysInMonth + 1):
        endOfMonthDay = day  # Update `dayEnd2` to the current day

    finalDayCount = 0
    check = False
    for l in range(7):
        dayEnd = int(dateWeek[8:10]) + finalDayCount
        finalDayCount += 1
        if dayEnd == endOfMonthDay:
            dayEnd = 7 - finalDayCount
            check = True
            break

    dateWeekEnd = dateWeekBegin[0:8] + str(dayEnd)
    if check:
        nextMonth = (int(dateWeekEnd[5:7]) + 1)
        dateWeekEnd = dateWeekEnd[:5] + str(nextMonth) + dateWeekEnd[7:]

    urlDay = f"https://api.meteomatics.com/{dateWeekBegin}T{timeDay}:00:00Z--{dateWeekEnd}T{timeDay}:00:00Z:PT24H/t_2m:C/{location}/json"
    print(urlDay)
    responseDay = requests.get(urlDay, auth=HTTPBasicAuth('self_madyavanhu_dominik', 'eddO7j82JE'))
    dataDay = responseDay.json()  # Assuming the response is in JSON format
    print("day: " + str(dataDay))

    resultDay = []
    for j in range(7):
        weatherForecastWeekDateDay = dataDay['data'][0]['coordinates'][0]['dates'][j]['date'][
                                     5:10]  # Extract time part from date
        temperature = dataDay['data'][0]['coordinates'][0]['dates'][j]['value']  # Get temperature
        resultDay.append((weatherForecastWeekDateDay, temperature))  # Append tuple (date, temperature)
    return resultDay


def weatherForecastWeekNight(location):
    timeNight = '02'
    dateWeek = str(datetime.now())
    dateWeekBegin = dateWeek[0:10]
    dayEnd = str(int(date[8:10]) + 7)
    endOfMonthNight = 0

    print(dateWeek)

    year = int(dateWeek[:4])
    month = int(dateWeek[5:7])

    daysInMonth = get_days_in_month(year, month)
    for day in range(endOfMonthNight, daysInMonth + 1):
        endOfMonthNight = day  # Update `dayEnd2` to the current day

    finalDayCount = 0
    check = False
    for l in range(7):
        dayEnd = int(dateWeek[8:10]) + finalDayCount
        finalDayCount += 1
        if dayEnd == endOfMonthNight:
            dayEnd = 7 - finalDayCount
            check = True
            break

    dateWeekEnd = dateWeekBegin[0:8] + str(dayEnd)
    if check:
        nextMonth = (int(dateWeekEnd[5:7]) + 1)
        dateWeekEnd = dateWeekEnd[:5] + str(nextMonth) + dateWeekEnd[7:]

    urlNight = f"https://api.meteomatics.com/{dateWeekBegin}T{timeNight}:00:00Z--{dateWeekEnd}T{timeNight}:00:00Z:PT24H/t_2m:C/{location}/json"
    responseNight = requests.get(urlNight, auth=HTTPBasicAuth('self_madyavanhu_dominik', 'eddO7j82JE'))
    dataNight = responseNight.json()  # Assuming the response is in JSON format
    print("Night: " + str(dataNight))

    resultNight = []
    for j in range(7):
        weatherForecastWeekDateDay = dataNight['data'][0]['coordinates'][0]['dates'][j]['date'][
                                     5:10]  # Extract time part from date
        temperature = dataNight['data'][0]['coordinates'][0]['dates'][j]['value']  # Get temperature
        resultNight.append((weatherForecastWeekDateDay, temperature))  # Append tuple (date, temperature)
    return resultNight


# button to display the weather forecast on matplotlib graph once its clicked
def click():
    readYear = int(labelYear['text'])
    readMonth = int(labelMonth['text'])
    readDay = int(labelDay['text'])
    readLocation = labelLocation['text']
    print(readYear, readMonth, readDay, readLocation)

    coords = coordinates[readLocation]

    # function to extract times
    get_times = lambda x: [t[0] for t in x]

    #function to extract temperatures
    get_temps = lambda x: [t[1] for t in x]

    # Get the list of times and temperatures
    data = weatherForecast(readYear, readMonth, readDay, coords)
    times = get_times(data)
    temps = get_temps(data)

    ax.clear()
    xAxis = times
    yAxis = temps
    ax.scatter(xAxis, yAxis, color='blue')
    ax.set_aspect(aspect=1.0, adjustable='datalim')
    canvas.draw()
    label2.config(text="Weather forecast for the day: ")


selectButton = Button(window, text='Select', command=click)
selectButton.config(fg='#484F51', bg='#71BFD7', pady=5, padx=5, font=('Sans serif', 17), relief=RAISED)
selectButton.pack()


def clickWeek():
    readLocation = labelLocation['text']
    coords = coordinates[readLocation]
    print(weatherForecastWeekDay(coords))
    print(weatherForecastWeekNight(coords))

    # function to extract times
    get_times = lambda x: [t[0] for t in x]

    #function to extract temperatures
    get_temps = lambda x: [t[1] for t in x]

    dataDay = weatherForecastWeekDay(coords)
    timesDay = get_times(dataDay)
    tempsDay = get_temps(dataDay)

    dataNight = weatherForecastWeekNight(coords)
    timesNight = get_times(dataNight)
    tempsNight = get_temps(dataNight)

    ax.clear()

    xAxisDay = timesDay
    yAxisDay = tempsDay

    xAxisNight = timesNight
    yAxisNight = tempsNight

    ax.plot(xAxisDay, yAxisDay, color='yellow')
    ax.plot(xAxisNight, yAxisNight, color='black')
    ax.set_aspect(aspect=0.1, adjustable='datalim')
    canvas.draw()
    label2.config(text="Weather forecast for the week: ")


weekForecastButton = Button(window, text="Show forecast for the week", command=clickWeek)
weekForecastButton.config(fg='#484F51', bg='#71BFD7', pady=5, padx=5, font=('Sans serif', 17), relief=RAISED)
weekForecastButton.pack()

# shows a message to user
label2 = Label(window, text="Weather forecast", wraplength=0, justify="center", fg='#484F51',
               bg='#71BFD7', relief=RAISED)
label2.config(font=('Sans serif', 32))
label2.pack(pady=10, padx=10)

# matplotlib graph to display the weather forecast
fig, ax = plt.subplots()
ax.set_aspect(aspect=1.0, adjustable='datalim')
plt.tight_layout()
plt.xticks(rotation=45)

# canvas contains the graph
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(fill=BOTH, expand=True)

window.mainloop()
