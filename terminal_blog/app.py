from database import Database
from models.post import Post
from models.blog import Blog

Database.initialize()

blog = Blog(author="vaibhav", title="vaibhav is best in the world", description="about my success")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.get_from_mongo(blog.id)

print(blog.get_post())

