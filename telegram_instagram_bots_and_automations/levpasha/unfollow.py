from InstagramAPI import InstagramAPI

def login():
    api = InstagramAPI('', '')

    if(api.login()):
        return api
    return False


def get_user_id(username):
    InstagramAPI.searchUsername(username)
    try:
        return InstagramAPI.LastJson['user']['pk']
    except Exception:
        print('User doesn\'t exist')
        return False


def followers_list(api):
    followers = api.getTotalFollowers(api.username_id)
    f_ers = [f['username'] for f in followers]
    return f_ers


def followings_list(api):
    followings = api.getTotalFollowings(api.username_id)
    f_ings = [f['username'] for f in followings]
    return f_ings

    
def unfollow(api):
    followers = followers_list(api)
    followings = followings_list(api)

    for username in followings:
        if username not in followers:
            pk = get_user_id(username)
            if(api.unfollow(pk)):
                print('Unfollow {} succuesfully'.format(username))
        else:
            continue


if __name__ == "__main__":
    api = login()
    unfollow(api)
