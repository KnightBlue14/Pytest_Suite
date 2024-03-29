import pandas as pd
import re
     

filename = 'project_dataset.csv'
df = pd.read_csv(filename)
     

def hrs(time):
  numbers = re.findall(r'\d+', time)
  hours = int(numbers[0]) if numbers and 'hr' or 'hours' in time else 0
  minutes = int(numbers[1]) if len(numbers) > 1 and 'mins' or 'minutes' in time else 0
  total_minutes = hours * 60 + minutes
  return total_minutes
df['time'] = df.time.apply(hrs)
     

def star_call(string):
  string = string.replace('Not rated yet','0 out of 5 stars0 ratings')
  string = re.split('(stars)',string)
  string = string[0]
  string = string.replace(' out of ',',')
  string = string.replace(' of ',',').split(',')
  string = ''.join(str(i) for i in string[0])
  string = float(string)
  return string

df['rating'] = df.stars.apply(star_call)
     

def rating_call(string):
  string = string.replace('Not rated yet','0 out of 5 stars0 ratings')
  string = re.split('(stars)',string)
  string = string[-1]
  string = string.replace(' ratings','')
  string = string.replace(' rating','')
  string = string.replace(',','')  
  string = string.replace('with','')
  string = int(float(string))
  return string

df['number_of_ratings'] = df.stars.apply(rating_call)


df.releasedate = pd.to_datetime(df.releasedate, format='%d-%m-%y')
     

df.releasedate = df.rename(columns = {'releasedate': 'release_date'},inplace = True)
     

df.price = df.price.str.replace(',', '')
df.price = df.price.str.replace('Free', '0.00')
df.price = pd.to_numeric(df.price)
     

def fix_name(name):
  name = name.replace('Writtenby:','')
  name = name.replace('Narratedby:','')
  name = name.replace('fullcast,','')
  name = re.sub( r"([A-Z])", r" \1",name).strip()
  name = name.replace('Mc ', 'Mc')
  return name

df.author = df.author.apply(fix_name)
df.narrator = df.narrator.apply(fix_name)
     

df = df[['name','author','narrator','time','release_date','language','price','rating','number_of_ratings']]
     

filename = filename.replace('.csv', '_clean_update.csv')
     

df.to_csv(filename, index=False)