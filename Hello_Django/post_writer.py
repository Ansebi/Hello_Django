import random
from hello_app.models import Post
# from misc.dummy_text import dummy_text

DUMMY_PATH = 'C:/Documents/Python/Hello_Django/misc/dummy_text.txt'
N = 10
AUTHOR_IDS = [1, 2]
dummy_text = list(open(DUMMY_PATH, encoding='utf-8'))[0]
print(dummy_text)
# def post_writer(n=N, author_ids=author_ids):
for i in range(N):
    content = f'The text number {i}.\n'
    content += dummy_text
    post = Post(
        title=f'Post {i}. Title.',
        content=content,
        author_id=random.choice(AUTHOR_IDS)
    )
    post.save()
    print(f'{i} ok')
