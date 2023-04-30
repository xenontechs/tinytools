import os
import sys

# === CONFIG
# IGNORED FILES/FOLDERS
# ignored file or folder names. full name only. this means also sub-folders don't show up
IGNORED_ITEMS = [".git", ".gitignore", ".DS_Store", "venv", ".obsidian", "__pycache__"]
# ignore all files/folders starting with a dot?
IGNORE_HIDDEN = True


# MERMAID COFIGURATION:
# list of characters thrown out of item IDs because they cause trouble
MERMAID_ILLEGAL_CHARACTERS = r":\\\" -äöüÄÖÜ?ß()[]\{\}"
# list of words thrown out of item IDs because they cause trouble
MERMAID_ILLEGAL_PHRASES = ["top"]
# what to replace them with:
MERMAID_REPLACEMENT_CHARACTER = "_"


# OUTPUT CONFIGURATION
def preprint():
    """ADD EXTRA LINES HERE FOR THINGS TO ADD BEFORE THINGS"""
    match output_type:
        case "dash":
            pass
        case "mermaid":
            print("```mermaid")
            print("graph LR")


def postprint():
    """ADD EXTRA LINES HERE FOR THINGS TO ADD AFTER THINGS"""
    match output_type:
        case "dash":
            pass
        case "mermaid":
            print("```")

# === END OF CONFIG


# get args
filepath = sys.argv[1] if len(sys.argv) >= 3 else ""
output_type = sys.argv[2] if len(sys.argv) >= 3 else ""

# which outputs do we have?
# dash, mermaid, cmdtree?
OUTPUT_TYPES = ["dash", "mermaid", "obsidiandash"]

# as we use backslash in path to display depth, we need to cut off a few of them when outputting the pretty
negate_depth = 0


def mermaid_legalize(input):
    """strips mermaid illegal characters from a string"""
    for item in MERMAID_ILLEGAL_CHARACTERS:
        input = input.replace(item, MERMAID_REPLACEMENT_CHARACTER)
    for item in MERMAID_ILLEGAL_PHRASES:
        input = input.replace(item, MERMAID_REPLACEMENT_CHARACTER)
    return input


def print_files(directory):
    """iterate through directory and print all files
    basically a wrapper for os.walk() that throws contents to output() to deal with formatting
    """
    for root, dirs, files in os.walk(directory):
        # only proceed if not part of the patch is in ignore list AND if hidden items are ignored then if the path does not contain "\."
        is_not_ignored = all(item not in root.split("\\") for item in IGNORED_ITEMS)
        contains_dot = root.count("\\.") > 0
        if is_not_ignored and (not contains_dot if IGNORE_HIDDEN else True):
            output(root)
            if root.split("\\")[-1] not in IGNORED_ITEMS:
                for file in files:
                    if file not in IGNORED_ITEMS and (not file[0] == "." if IGNORE_HIDDEN else True):
                        output(root, file)
                for dir in dirs:
                    if dir not in IGNORED_ITEMS and (not dir[0] == "." if IGNORE_HIDDEN else True):
                        output(root, dir)


def output(root, item=""):
    """print the items"""
    depth = root.count("\\")+negate_depth
    match output_type:
        case "dash":
            if not item:
                print("-"*depth + root)
            else:
                print("-"*(depth+1) + item)
 
        case "obsidiandash":
            if not item:
                print("-"*depth + root)
            else:
                print("-"*(depth+1) + "[[" + item + "]]")

        case "mermaid":
            # if we only get a directoy, we add it with pretty name
            if not item:
                item_id = mermaid_legalize(root)
                item_name = root.split("\\")[-1]
                print(f"{item_id}[\"{item_name}\"];")
            else:
                # if we get a directory and a item, we link directory and itemwith pretty name
                # if the item is a directory, the next round it will be created again, creating duplicates
                # we'll let mermaid deal with that *shrug*
                root_id = mermaid_legalize(root)
                item_id = mermaid_legalize(root + "\\" + item)
                item_name = item
                print(f"{root_id} --> {item_id}[\"{item_name}\"]; ")


if __name__ == "__main__":
    """main function"""
    # check for missing inputs, ask user if needed
    if not filepath:
        print("Missing filepath")
        filepath = input("Enter filepath: ")

    # Check if the file path exists
    if not os.path.exists(filepath):
        print(f"File path {filepath} does not exist")
        sys.exit(1)

    # Check if the file path is a directory
    if os.path.isfile(filepath):
        print(f"{filepath} is a file (needs to be directory)")
        sys.exit(1)

    # check if output type exists, else ask again
    if output_type not in OUTPUT_TYPES:
        output_type = input(f"define output type {OUTPUT_TYPES}: ")

    # reset level of base directoy to 0
    negate_depth -= filepath.count("\\")

    # print the things
    preprint()
    print_files(filepath)
    postprint()
