# Taking input (file name) 
file = input("File name: ").lower()

# Checking the suffix of file and printing relevent output
if ".gif" in file:
    print("image/gif")
elif ".jpg" in file:
    print("image/jpeg")
elif ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
