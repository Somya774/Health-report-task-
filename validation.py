import re
from datetime import datetime


def checkemail(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))


def checkdob(dob):

    try:

        dobdate = datetime.strptime(dob, "%Y-%m-%d")

        return dobdate.date() <= datetime.today().date()

    except:

        return False


def checknumbers(glucose, hemoglobin, cholestrol):

    try:

        float(glucose)
        float(hemoglobin)
        float(cholestrol)

        return True

    except:

        return False