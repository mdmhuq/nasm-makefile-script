#!/usr/bin/env python3

# Define a function to generate the Makefile
def make_file():

    # Ask the user to specify the global label for the assembly program
    # This could be either "global main" or "global _start"
    start_or_main = input("global main or global _start?: ")

    # Ask the user to enter the name of the assembly file
    file_name = input("Please enter file name: ")

    # If the user enters an empty string, keep asking until a valid file name is provided
    while file_name.rstrip() == "":
        file_name = input("Please enter file name: ")

    # Remove the .asm extension from the file name if it exists
    file_name = file_name.replace(".asm","")

    # Depending on the global label specified by the user, generate the appropriate Makefile
    # The Makefile includes commands for assembling the .asm file into an object file (.o),
    # linking the object file into an executable, and cleaning up the generated files
    if start_or_main == "_start":
        file_string = f"{file_name}: {file_name}.o\n\tld -o {file_name} {file_name}.o\n\tchmod u+x {file_name}\n{file_name}.o: {file_name}.asm\n\tnasm -f elf64 -g -F dwarf {file_name}.asm -l {file_name}.lst\nclean:\n\trm {file_name} {file_name}.o {file_name}.lst\nrun:\n\t./{file_name}"
    else:
        file_string = f"{file_name}: {file_name}.o\n\tgcc -o {file_name} {file_name}.o\n{file_name}.o: {file_name}.asm\n\tnasm -f elf64 -g -F dwarf {file_name}.asm -l {file_name}.lst\nclean:\n\trm {file_name} {file_name}.o {file_name}.lst\nrun:\n\t./{file_name}"

    # Write the generated Makefile to a file named "Makefile"
    with open("Makefile", "w") as f:
        f.write(file_string)

# Call the make_file function to generate the Makefile
make_file()
