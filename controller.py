import random
import string

from flask import jsonify, abort

from model import *


def get_single_short_link(slug):
    response = get_link_by_slug(slug)
    if response is None:
        abort(404)
    return jsonify(response.to_json_type())


def get_all_short_links():
    return jsonify(get_all_links())


def generate_new_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def add_new_short_link(request):
    if 'slug' in request:
        new_slug = request['slug']

        if get_link_by_slug(new_slug):
            response = {
                "status": "failed",
                "slug": new_slug,
                "message": "slug already exists"
            }
            return jsonify(response), 400
    else:
        new_slug = generate_new_slug()
        while get_link_by_slug(new_slug):
            new_slug = generate_new_slug()

    new_short_link = ShortLink(
        slug=new_slug,
        web=request['web'],
        android=DeviceLink(
            primary=request['android']['primary'],
            fallback=request['android']['fallback']
        ),
        ios=DeviceLink(
            primary=request['ios']['primary'],
            fallback=request['ios']['fallback']
        )
    )
    add_short_link(new_short_link)
    response = {
        "status": "successful",
        "slug": new_slug,
        "message": "created successfully"
    }
    return jsonify(response), 201
