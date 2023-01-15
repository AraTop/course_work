import json

def get_posts_all():
   with open("posts.json", "r" , encoding="utf-8") as f:
      posts = json.load(f)
      return posts

def get_posts_by_user(user_name):
   post = []
   for post_one in get_posts_all():
      if post_one["poster_name"] in user_name:
         post.append(post_one)
   
   return post

def get_comments_by_post_id(post_id):
   with open("comments.json", "r", encoding="utf-8") as f:
      comment = []
      comments = json.load(f)
      for comment_one in comments:
         if comment_one["post_id"] == post_id:
            comment.append(comment_one)
      if comment == None:
         comment.append(ValueError) 
      else:
         return comment

def search_for_posts(query):
   posts = []
   for post in get_posts_all():
      if query.lower() in post["content"].lower():
         posts.append(post)
   return posts

def get_post_by_pk(pk):
   number = []
   number.append(int(pk))
   for post in get_posts_all():
      if post["pk"] in number:
         return post


