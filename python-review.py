def create_youtube_video(title,description):

	video = {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return video

def likes (video):
	if "likes"in video:
		video["likes"]  = video["likes"]+1

	return video

def dislikes (video):
	if "dislikes"in video:
		video["dislikes"]  = video["dislikes"]+1

	return video


def add_comment (youtubevideo,username,comment_text):

	comments = {username:comment_text}
	youtubevideo["comments"]= comments

	return youtubevideo

x = create_youtube_video("ghgh","tytyty")

print(dislikes(likes(add_comment(x,"yazan","tt"))))


for i in range(496):
	likes(x)

print(x)