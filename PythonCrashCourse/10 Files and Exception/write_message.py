from pathlib import Path

contents = "I love Python!\n"
contents += "I love creating new games. \n"
contents += "I also love working with data. \n"

path = Path('programming.txt')

# path.write_text("I Love Python!")

path.write_text(contents)
