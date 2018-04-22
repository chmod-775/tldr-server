import json
from datetime import datetime # FIXME: Currently only used for placeholder data

from flask import Flask, request, g, config
app = Flask(__name__)


with app.app_context():
  @app.route('/')
  def hello():
      return "Hello World!"

  @app.route('/comment-stats')
  def gen_comment_stats():
      app_type = request.args.get('app_type')
      app_id = request.args.get('app_id')
      placeholder = {
          'ranked_entities': {
              'reason': 5.0,
              'sucks': 0.1,
              'Sam': 0.0
          },
          'title': 'Sam sucks',
          'description': 'The reason Sam sucks is that he just does.',
          'rating': '0',
          'app_id': app_id,
          'app_type': app_type,
          'comments': [
              {
                  'title': 'Wow, it really is true!!',
                  'content': 'I thought Sam was probably an ok guy, but this app totally convinced me otherwise!',
                  'updated_at': int(datetime.now().timestamp()),
                  'rating': 5,
                  'sentiment': 0.95,
                  'entities': ['Sam', 'guy', 'app', 'convinced']
              },
              {
                  'title': 'Doesn\'t this app seem kind of petty?',
                  'content': 'I mean, regardless of whether or not Sam sucks, why go through the trouble of making an app about it?',
                  'updated_at': int(datetime.now().timestamp()),
                  'rating': 2,
                  'sentiment': 0.35,
                  'entities': ['Sam', 'trouble', 'app']
              },
              {
                  'title': 'Petty? You\'re petty!!' ,
                  'content': 'People should be free to make any app they want! Maybe you don\'t like it, and that\'s fine, but let those of us who ant to see Sam for what he really is be free!!',
                  'updated_at': int(datetime.now().timestamp()),
                  'rating': 5,
                  'sentiment': 0.05,
                  'entities': ['People', 'free', 'app', 'want']
              }
          ]
      }
      return json.dumps(placeholder)


if __name__ == '__main__':
    app.run()
