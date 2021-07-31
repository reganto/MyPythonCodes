from InstagramAPI import InstagramAPI

if __name__ == "__main__":
    api = InstagramAPI('', '')

    api.login()

    followers =  api.getTotalFollowers(api.username_id)
    print(len(followers))
