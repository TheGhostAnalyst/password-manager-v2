from datetime import datetime
import pyinputplus as Pyip
import shelve


def save(app, contact, password):
   with shelve.open('Manager', writeback=True) as db:
         now  = datetime.now().strftime('%Y-%m-%d %H:%M')
         if app in db:
            if isinstance(db[app], list):
               db[app].append({'Contact': contact, 'Password': password, 'Date saved': now})
            else:
               db[app] = [{'Contact': contact, 'Password': password, 'Date saved': now}]
         else:
            db[app] = [{'Contact': contact, 'Password': password, 'Date saved': now}]
   

def search(app):
   with shelve.open('Manager') as db:
         if app in db:
            print(f'Here are the details for {app}:\n')
            for i, entry in enumerate(db[app], start=1):
                  print(f"#Entry {i}:")
                  print(f"Contact: {entry['Contact']}\nPassword: {entry['Password']}\nDate saved: {entry['Date saved']}\n")
         else:
            print(f'No entries found for {app}.')

def debug_show_all():
    with shelve.open('Manager') as db:
        for key in db:
            print(f"App: {key}")
            for entry in db[key]:
               if isinstance(entry, dict):
                  contact = entry.get('Contact', 'N/A')
                  password = entry.get('Password', 'N/A')
                  date = entry.get('Date saved', 'N/A')

                  print('--------------------------------')
                  print(f"Contact: {contact}")
                  print(f"Password: {password}")
                  print(f"Date saved: {date}\n")
                  print('--------------------------------\n')
               else:
                   print("Skipping invalid entry format.") 
while True:
   try:
      print('\nPassword manager tool by The Ghost Analyst')
      first = Pyip.inputNum("""Which of these operations would you like to perform:
      1. Save a new password
      2. Find likely websites you stored passwords for 
      3. Show all saved passwords   
      4. Exit                  
      >>>>>> """)
      if first == 1:
            print('Save a new password')
            app_name = input('Enter the website or app you want to save password for: ').lower()
            contact = input('Enter your phone number, email or username: ')
            password = input('Enter your password for the app or website you want to save: ')
            save(app_name, contact, password)
            print('Details saved successfully! in Ghost Database')

      elif first == 2:
            search_web = input('What app or website do you want to search for: ').lower()
            search(search_web)

      elif first == 3:
         debug_show_all()
      elif first == 4:
         print('Preparing a smooth exit........')
         break
   except KeyboardInterrupt:
      print("Exit successful")
      break
    
