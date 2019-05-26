from string import Template

def main():
    #string formatted with format()
    str1 = "You're watching {0} by {1}.".format("advanced python", "joe")
    print(str1)

    #create template with placeholder
    #template method is better suited when using stings from external sources. (Ex- web form)
    templ = Template("You are watching ${title} by ${author}.")

    #using the substitute() method
    str2 = templ.substitute(title="Advanced Python", author="joe")
    print(str2)

    #using a dictionary to substitute
    data = {
        "author": "joe",
        "title": "advanced python"
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == "__main__":
    main()