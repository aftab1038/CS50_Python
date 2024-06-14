# main function: Take input (mass)
def main():
    m = int(input("m: "))
    print("E:", energy(m))

# energy function: Convert mass to energy - E = mc^2
def energy(m):
    c = 300000000
    return m*pow(c, 2)

# Calling main function
main()