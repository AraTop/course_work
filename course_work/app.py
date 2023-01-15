import json
from flask import Flask , request , render_template , jsonify , redirect
from utils import get_posts_all , get_posts_by_user , get_comments_by_post_id , search_for_posts , get_post_by_pk
import logging

logging.basicConfig(filename="logs/api.log", level=logging.INFO)
logger = logging.getLogger()

app = Flask(__name__)

@app.route("/")
def home():
   items = get_posts_all()
   with open("bookmarks.json", encoding="utf-8") as f:
      data = json.load(f)
      len_data = len(data['posts'])
   return render_template("index.html", items=items , len_data=len_data)

@app.route("/posts/<int:postid>")
def viewing(postid):
   comments = get_comments_by_post_id(postid)
   item = get_post_by_pk(postid)
   len_post = len(comments)
   return render_template("post.html", item=item, comments=comments , len_post=len_post)

@app.route("/search")
def search():
   word_url = request.args.get("s")
   print(word_url)
   posts = search_for_posts(word_url)
   len_post = len(posts)
   return render_template("search.html", posts=posts , word_url=word_url, len_post=len_post) 

@app.route("/users/<username>")
def users(username):
   post_user = get_posts_by_user(username)
   return render_template("user-feed.html", post_user=post_user)

@app.route("/meow")
def meow():
   return ''

@app.route("/api/posts")
def all_posts():
   logger.info(f'request /api/posts')
   all_posts = get_posts_all()
   return jsonify(all_posts)

@app.route("/api/posts/<int:post_id>")
def post(post_id):
   logger.info(f'request /api/posts/{post_id}')
   post = get_post_by_pk(post_id)
   return jsonify(post)

@app.route("/bookmarks/add/<int:postid>")
def add(postid):
   post = get_post_by_pk(postid)
   with open("bookmarks.json", encoding="utf-8") as f:
      data = json.load(f)
      data['posts'].append(post)
      with open('bookmarks.json' ,"w", encoding="utf-8") as outfile:
         json.dump(data,outfile, indent=6)
   
   return redirect("http://127.0.0.1:5000", code = 302) 

@app.route("/bookmarks/remove/<int:postid>")
def remove(postid):
   with open("bookmarks.json" , "r", encoding="utf-8") as f:
      data = json.load(f)
      while True:
         index = 0
         for item in data["posts"]:
            if item["pk"] == postid:
               data["posts"].pop(index)
               break
            else:
               index += 1
         break
         
   # загружаем обновленный data обратно в bookmarks.json
   open("bookmarks.json", "w").write(
    json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
   ) 

   return redirect("http://127.0.0.1:5000", code = 302) 

@app.route("/bookmarks")
def all_bookmarks():
   with open("bookmarks.json", "r" , encoding="utf-8") as f:
      data = json.load(f)
   return render_template("bookmarks.html", data=data["posts"])

app.run(debug=True)