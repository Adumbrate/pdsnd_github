import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Requests for user to specify a city, month, and day to analyze.
    Returns:
        (str) city - city name to perform analysis on
        (str) month - month name to filter by, or "all" to apply no month filter
        (str) day - day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome! Let\'s explore some US bikeshare data!')
    # Request for user to input city (chicago, new york city, washington).
    while True:
        city = input("Enter the city you wish to analyze? \n")
        #Ensure the user inputs are entered in lowercase
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry!, wrong input entered. Please try again.\n")
    # Request for user to input which month (all, january, february, ... , june)
    while True:

        month = input("Enter a month to explore, type 'all' to explore all months. \n")
        month == month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Sorry!, wrong input entered. Please try again.")
    # Request for user to input the day of the week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day to explore, type 'all' for all days \n").lower()
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Sorry!, wrong input entered. Please try again.")
    print('-'*40)
    return city, month, day

# Load dataset
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # read city data into pandas dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Deriving month column from Start Time column
    df['month'] = df['Start Time'].dt.month

    # Creating Day Of Week column from Start Time column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # This syntax will help  create a new dataframe for any selected specific month
    if month != 'all':
        # using the index of the months list to get the corresponding int
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month) + 1

        # syntax to create a filter by month to create the new dataframe
        df = df[df['month'] == month]

    # #Creating a new dataframe for any selected specific day (if selected)
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Reveal the most common month
    print("The most common month is: {}\n".format(df['month'].mode()[0]))

    # Reveal the most common day of week
    print("The most common day of week  is: {}\n ".format(df['day_of_week'].mode()[0]))

    # Reveal the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("most common start hour is: {}\n ".format( df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Reveal the most commonly used start station
    print("The most commonly used start station is {}\n ".format( df['Start Station'].mode()[0]))

    # Reveal the most commonly used end station
    print("The most commonly used end station is {}\n".format( df['End Station'].mode()[0]))

    # Reveal the most frequent combination of start station and end station trip
    df['The Most Frequent Combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['The Most Frequent Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTo Calculate Trip Duration...\n')
    start_time = time.time()

    # Reveal total travel time
    print("Aggregate travel time is {} seconds \n".format( df['Trip Duration'].sum()))

    # Show mean travel time
    print("Mean travel time is {} seconds \n".format( df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nTo Calculate User Stats...\n')
    start_time = time.time()

    # Show counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types\n", user_types, "\n")
    if city != 'washington':
        # Show counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
        # show earliest, most recent, and most common year of birth. 'by'=birth year
        most_recent_by = df['Birth Year'].max()
        print("Most recent birth year: {}\n".format(most_recent_by))

        earliest_by = df['Birth Year'].min()
        print("Earliest year of birth: {}\n ".format(earliest_by))

        mostfrequent_by = df['Birth Year'].mode()[0]
        print("The most frequent birth year is: {}\n".format(mostfrequent_by))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw_data = input("\nLike to see five lines of raw data? Enter 'YES' or 'NO'.\n")
        if raw_data.upper() == 'YES':
            print(df[x:x+5])
            x = x+5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    