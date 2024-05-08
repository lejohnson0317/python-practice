from admin import Admin

user1 = Admin("jim", "johnson", "jjohnson", "engineer", \
             "4/22/2024", "$120,000/yr")

user1.greet_user()
user1.describe_user()
user1.privileges.privileges = ["can delete post", "can ban user", "can add post"]
user1.privileges.show_privileges()
