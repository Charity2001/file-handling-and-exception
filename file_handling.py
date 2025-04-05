# 📁 File Reader and Writer with Error Handling

def read_and_modify_file():
    # Step 1: Ask the user for the file name
    filename = input("Enter the name of the file you want to read (example: myfile.txt): ")

    try:
        # Step 2: Try to open the file and read the content
        with open(filename, 'r') as file:
            content = file.read()
            print("\n✅ File read successfully!\n")
            print("Original content:")
            print(content)

            # Step 3: Modify the content (for example, make it uppercase)
            modified_content = content.upper()

            # Step 4: Save the modified content to a new file
            new_filename = "modified_" + filename
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_content)

            print(f"\n✅ Modified content has been saved to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Oops! The file you entered does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Something went wrong while trying to read the file.")

# Let's call the function to run the program
read_and_modify_file()
