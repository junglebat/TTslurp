from TikTokApi import TikTokApi
import string
import random

api = TikTokApi.get_instance()

# set details below:
# verify contents of the cookie "s_v_web_id' as found in your webbrowser
# TTusername is the name of the user you want to download vids from
# maxdl is the maximum amount of vids you want to get. Set this to 0 (zero)
# if you want to download all the vids.

verify = ""
TTusername = ""
maxdl = 10

class TTuser:
    def __init__(self, user, ttverify):
        self.userinfo = api.get_user(username=user, custom_verifyFp=ttverify)
        self.ttid = self.userinfo['userInfo']['user']['id']
        self.ttsecuid = self.userinfo['userInfo']['user']['secUid']
        self.avatar = self.userinfo['userInfo']['user']['avatarLarger']
        self.vidcount = self.userinfo['userInfo']['stats']['videoCount']

    def downloadvids(self, maxvids, ttverify):
        if maxvids == 0:
            maxvids = self.vidcount
        custom_did = ''.join(random.choice(string.digits) for num in range(19))
        self.vidlist = api.user_posts(self.ttid, self.ttsecuid, count=maxvids, custom_did=custom_did)
        for vid in self.vidlist:
            vidname = str(vid['video']['id']) + ".mp4"
            vidurl = (vid['video']['downloadAddr'])
            tiktokdata = api.get_video_by_download_url(vidurl, custom_did=custom_did)
            with open(vidname, "wb") as out:
                out.write(tiktokdata)


ttuser = TTuser(TTusername, verify)
ttuser.downloadvids(maxdl, verify)
