import logging

exData = {
    "user": "Indika"
}

def anotherFunc():
    logging.warning("warning in anotherFunc", extra=exData)

def main():
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%y %I:%M:%S %p"

    logging.basicConfig(filename="customlog.log", level=logging.DEBUG, format=fmtstr,
                filemode="w", datefmt=datestr)
    logging.info("This is an info log.", extra=exData)
    logging.warning("This is a warning.", extra=exData)
    anotherFunc()


if __name__ == "__main__":
    main()