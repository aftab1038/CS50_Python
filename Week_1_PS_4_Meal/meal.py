def main():
    # TODO
    time = input("What time is it? ")
    time = convert(time)

    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")


def convert(time):
    # TODO
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    return hours + (minutes/60.0)


if __name__ == "__main__":
    main()
