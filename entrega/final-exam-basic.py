# Tasks to complete:
# T1: Load file
  # T1.1: Open the file "base_de_datos_de_clientes.csv" without a fixed path
  # T1.2: Read file "base_de_datos_de_clientes.csv"
  # T1.3: Split in columns the information inside the file "base_de_datos_de_clientes.csv"
  # T1.4: Add columns to a list
  # T1.5: Add previous list into a list of lists
# T2: Data cleansing
  # T2.1: Remove characters from the begining of the first column 
  # T2.2: Remove dash "#" from the birthdate
  # T2.3: Extract the year of a person
  # T2.4: Calculate the age of a person
  # T2.5: Add calculated age into a column (create if it doesn't exists)
# T3: Save changes
  # T3.1: Open a new file "clientes_limpios.csv"
  # T3.2: Write the changes inside the new file
  # T3.3: Close the open file

from datetime import datetime
# Using this module the calculation of the age will be easier and more accurate everytime we run the code


# T1.1 Open a file in read mode
# In order to open the file, I will ask the user to input the file path.
filePath = input("\nEnter the file path / Ingresa la ruta del archivo (*.csv): \n")

# Using Visual Studio Code, I detected that the encoding of the file is windows-1252
# However, to ensure compatibility, I will use utf-8 encoding by saving the file again with the new encoding, so that it works on all systems
file = open(filePath,"r",encoding="utf-8")


# T1.2 Read all the lines of the file
lines = file.readlines()

# Close the file after reading
# This is a good practice to avoid memory leaks and file locks
# In this case, it is not strictly necessary since we are not writing to the file,
# but it is a good habit to close files after use
file.close()

# T1.3 Split in columns the information of every line divided by a semicolon (;) and remove any extra spaces like \n
# T1.4: Add columns to a list
# T1.5: Add previous list into a list of lists
customers = [line.strip().split(';') for line in lines]

# Lets print the first 3 customers to verify the data
for customer in customers[:3]:
    print(customer)


#T2.1 Clean the first column of the customers list
# The first column contains some extra characters 'A.!--' at the begining of the RUTs, so we will remove them.
# There are 5 characters to remove. So we will use slicing to remove the first 5 characters of each RUT.
# We could also use the `replace` method, but since we know the exact characters to remove, slicing is more efficient.
# We will also remove any extra spaces that may be present just in case.

# Lets print the first 3 RUTs to compare the data before and after the cleaning
print("Original RUTs:")
for customer in customers[:3]:
    print(customer[0])

for customer in customers:
    # Check if the first element starts with 'A.!--'
    if customer[0].startswith('A.!--'):
        # Remove the first 5 characters and strip any extra spaces
        customer[0] = customer[0].strip()[5:len(customer[0].strip())]

# Lets print the first 3 cleaned RUTs to verify the data
print("Cleaned RUTs:")
for customer in customers[:3]:
    print(customer[0])

#T2.2: Clean dash '-' from the birthdate column
# The birthdate column is the 4th column (index 3) in the customers list.
# We will remove the dash '-' from the birthdate column and strip any extra spaces that may be present.
# We will use the `replace` method to remove the dash and the `strip` method to remove any extra spaces.
# We are not using slicing here because we want to remove the dash from anywhere in the string, not just from the beginning or end.
print("Original Birthdates:")
for customer in customers[:3]:
    print(customer[3])


for customer in customers:
    # Check if the birthdate column contains a dash '-'
    if '-' in customer[3]:
        # Remove the dash and strip any extra spaces
        customer[3] = customer[3].replace('-', '').strip()

# Lets print the first 3 cleaned birthdates to verify the data
print("Cleaned Birthdates:")
for customer in customers[:3]:
    print(customer[3])

# Lets print the original ages to compare the data before and after the cleaning
print("Original ages...")
for customer in customers[:3]:
    print(customer[4])


for customer in customers:
    # T2.3: Extract the year of a person
    year = int(customer[3][:4]) # The format is YYYY/MM/DD, so we take the first 4 characters
    #T2.4: Calculate the age of a person
    age = datetime.now().year - year
    #T2.5: Add the age to the customer list
    # Actually, the age replaces the age value in the 5th column (index 4) of the customer list
    # Previously, the age was a string with 'xxx' value in it, so we will replace it with the calculated age
    customer[4] = str(age)  # Convert age to string to maintain consistency with other columns

# Lets print the first 3 calculated ages to verify the data
print("Calculated ages...")
for customer in customers[:3]:
    print(customer[4])

# Lets print the first 3 customers after cleaning to verify the data
print("First 3 customers after cleaning:")
for customer in customers[:3]:
    print(customer)


# T3.1: Open a file in write mode
output_file_path = 'clientes_limpio.csv'

print(f"Saving cleaned data to {output_file_path}...")

file = open(output_file_path, 'w', encoding='utf-8')
# T3.2: Write the cleaned data to the file
for customer in customers:
    # Join the customer data with semicolons and write to the file
    file.write(';'.join(customer) + '\n')

# T3.3: Close the file
file.close()

# Notify the user that the data has been saved
print(f"Data saved to {output_file_path} successfully!")