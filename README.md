# promocode_generator

This is a simple promocode generator that creates unique codes and write it to json file

To install project write 'poetry init' to create poetry environment

There are two management commands wich available:

1. python manage.py generatepromo amount group

to create promocodes you must add two options - amount, wich is responsible for concrete amount of codes you want to create.
group - for what group you want to create codes.

example: 
    
   python manage.py generatepromo 10 'example'
   
On success you will recieve a message to the command line: "Successfully create 10 promocodes for 'example' group"

Result will be written to a file promocodes.json in the project source 

2. python manage.py checkuniquecodes file code

This command will check code that you set in option are unique and check file wich name you should set as first option

example:
   
   python manage.py checkuniquecodes 'promocodes.json' 'VZDRG8VCB102'
   
On success you will see a message: "Value are unique"

If this is not true, will raise error message




