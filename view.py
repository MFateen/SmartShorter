from flask import request, jsonify
from app import app
from model import add_short_link, ShortLink, DeviceLink


@app.route('/shortlinks', methods=['GET', 'POST'])
def short_links():
    if request.method == 'GET':
        return "Get shortlinks"
    else:
        return "Post shortlinks"


@app.route('/shortlinks/<slug>', methods=['PUT'])
def update_slug(slug):
    return "update " + slug
