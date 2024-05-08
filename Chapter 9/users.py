class User():
    """Define user information: User Name, First Name, Last Name, Job Title, Start Date, Salary"""

    def __init__(self, first_name, last_name, user_name, job_title, start_date, salary):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.start_date = start_date
        self.salary = salary

    def describe_user(self):
        """Prints user information"""

        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"User Name: {self.user_name}")
        print(f"Job Title: {self.job_title.title()}")
        print(f"Start Date: {self.start_date}")
        print(f"Salary: {self.salary}/n")

    def greet_user(self):
        """prints a greeting to the user"""

        print(f"\nHello, {self.first_name}.  Welcome to Johnson Enterprises.  Below is your user information.\n")