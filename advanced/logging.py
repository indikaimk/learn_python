import logging

def main():
    #basicConfig() would be executed only once
    logging.basicConfig(level=logging.DEBUG, filename="log.txt", filemode="w")
    logging.debug("This is debug message.")
    logging.info("This is info message.")
    logging.warning("This is warning message.")
    logging.error("This is error message.")
    logging.critical("This is critical message.")
    logging.info("Here is a {0} and int: {1}".format("string", 10))
    

if __name__ == "__main__":
    main()