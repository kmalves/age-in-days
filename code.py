def leap_year (year):
  if year % 400 == 0:
    return True # leap year
  if year % 100 == 0:
    return False #not leap year
  if year % 4 == 0:
    return True # leap year
  else:
    return False

def days_in_years (birth_year, current_year):
  year_list = [] #creates a list of years from birth year through the year before current to determine the amnt of leap years
  start_year = birth_year
  while start_year < current_year:
     year_list.append(start_year)
     start_year = start_year + 1
  extra_days = 0
  for year in year_list:
     if leap_year (year) == True:
      extra_days = extra_days + 1 #amnt of leap years (1 extra day per leap year) in the segment, current year not included, if it is leap we'll account for it later
  total_years = current_year - birth_year #amnt of years in the segment
  total_years_days = total_years * 365 #amnt of days not counting leap days from Jan 1st of birth year through Dec 31 year before current
  total_years_days_leap = total_years_days + extra_days #amnt of days with leap days from Jan 1st of birth year through Dec 31 year before current
  return total_years_days_leap  

def age_in_days (birth_year, birth_month, birth_day, current_year, current_month, current_day):
  list_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if leap_year (birth_year) == True:  
    list_of_months [1] = 29
  if leap_year (current_year) == True:  
    list_of_months [1] = 29
  result = days_in_years(birth_year, current_year) - (sum (list_of_months [:birth_month-1]) + (birth_day-1)) + (sum (list_of_months [:current_month-1]) + current_day)
  return result
