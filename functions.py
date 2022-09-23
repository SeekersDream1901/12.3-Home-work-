import json


def load_posts(path='posts.json'):
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def search_posts(substr):
    posts_found = []
    posts_json = load_posts()

    for post in posts_json:
        if substr.lower() in post['content'].lower().split(" "):
            posts_found.append(post)
        elif substr == "":
            posts_found = posts_json

    return posts_found


def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]

    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return

    picture.save(f'./uploads/images/{filename}')
    return f'/uploads/images/{filename}'


def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_post_to_json(posts)


def save_post_to_json(posts, path='posts.json'):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
