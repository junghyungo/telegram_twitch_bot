from twitchAPI import Twitch
from datetime import datetime

now = datetime.now()

client_ID = "5t87ha3qac9e90zox8asdd51uhun21"
client_secret = "m0vb6pp50eoqw4vmezd8jtj7tb7n4o"
twitch = Twitch(client_ID, client_secret)

def isLive(cid):
	channel_info = twitch.get_users(logins=cid)
	channel_numID = channel_info["data"][0]["id"]
	stream_info = twitch.get_streams(user_id=channel_numID)
	return stream_info

def getChannel(cid):
	channel_info = twitch.get_users(logins=cid)
	if not channel_info["data"]:
		return "Please check channel name or ID ;("
	else:
		channel_numID = channel_info["data"][0]["id"]
		channel_name = channel_info["data"][0]["display_name"]
		channel_profile = channel_info["data"][0]["profile_image_url"]
		
		stream_info = twitch.get_streams(user_id=channel_numID)
	
		print(channel_info)
		print(stream_info)
		
		if not stream_info["data"]:
			ans = channel_profile + "\n\n" + channel_name + " is not streaming :3"
			return ans
		else:
			stream_title = stream_info["data"][0]["title"]
			stream_gameName = stream_info["data"][0]["game_name"]
			stream_viewer = stream_info["data"][0]["viewer_count"]
			stream_upTime = stream_info["data"][0]["started_at"]
			H = now.hour - int(stream_upTime[11:13])
			M = now.minute - int(stream_upTime[14:16])
			ans = channel_profile + "\n\n" + channel_name + " is on Live!\n" + stream_title + "\n" + str(stream_viewer) + "명 시청 중" + "\n" + str(H) + "시간 " + str(M) + "분 동안" + "\n" + stream_gameName + "하는 중!\n"
			return ans