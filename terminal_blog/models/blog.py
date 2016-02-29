import uuid
from database import Database
import datetime
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id = None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter Post Title: ")
        content = input("Enter post content: ")
        date = input("Enter post date or leave blank for today (in format DDMMYYYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    title=title,
                    author=self.author,
                    content=content,
                    date=date)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blog',
                        data=self.json())

    def json(self):
        return{
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'description': self.description
            }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blog',
                                      query={'id': id})
        return cls(author=blog_data['author'], title=blog_data['title'], description=blog_data['description'],
                   id=blog_data['id'])

