from users import User

class Admin(User):
    """Define a class for admins which inherits UserClass"""

    def __init__ (self, first_name, last_name, user_name, job_title, start_date, salary):
        """Initialize attribites of the class User"""
        super().__init__ (first_name, last_name, user_name, job_title, start_date, salary)
        self.privileges =  Privileges()

class Privileges:
    """Define privilages assigned to a user."""

    def __init__ (self, privileges=[]):
        """Initialize privilages attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """Print a list of privilages assigned to admins."""
        print("The following privilages are assigned to this admin: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

#user1 = Admin("jim", "johnson", "jjohnson", "engineer", \
#             "4/22/2024", "$120,000/yr")
#user1.greet_user()
#user1.describe_user()
#user1.privileges.privileges = ["can delete post", "can ban user", "can add post"]
##user1.privileges.privileges = user1_privileges
#user1.privileges.show_privileges()
#
#user2 = User("betty", "travis", "btravis", "developer", \
#             "01/10/2023", "$113,300/yr")
#user2.greet_user()
#user2.describe_user()
