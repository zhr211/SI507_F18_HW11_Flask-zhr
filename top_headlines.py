
from flask import Flask,render_template
import secrets
import requests

app = Flask(__name__)
nm='Haoran'
nyt_key = secrets.api_key

def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': nyt_key}
    return requests.get(extendedurl, params).json()

def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []
    for r in results:
        headlines.append(r['title'])
    return headlines


@app.route('/name/<nm>')
def user(nm):

    story_list_json = get_stories('technology')
    headlines = get_headlines(story_list_json)
    newlist=[]
    for i in range(5):
        newlist.append(headlines[i])

    return render_template('user.html', my_list=newlist, name=nm)




if __name__ == '__main__':
    app.run(debug=True)
