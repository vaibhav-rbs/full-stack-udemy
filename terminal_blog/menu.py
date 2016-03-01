from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name")
        self.user_blog = None
        if self._user_has_an_account():
            print("Welcome back {}".format(self.user()))

        else:
            self._prompt_for_new_user_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user}) is not None
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title")
        description = input("Enter blog description:")
        blog = Blog(self.user, title, description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to (R)ead or (W)rite blogs")
        if read_or_write == "R":
            pass
        elif read_or_write == "W":
            pass
        else:
            print("Thankyou for blogging!")