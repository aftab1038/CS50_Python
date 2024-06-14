# Main function : taking input
def main():
    text = input()
    convert(text)

# Convert function : convert ":)" to "🙂" and ":(" to "☹️"
def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "☹️"))

# Calling main function
main()