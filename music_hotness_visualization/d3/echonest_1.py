'''
song object

artist_familiarity	artist_hotttness	artist_id	artist_location	artist_name	audio_summary	cache	get_artist_familiarity	get_artist_hotttnesss	get_artist_location	get_attribute	get_audio_summary	get_foreign_id	get_song_currency	get_song_discovery	get_song_hotttnesss	get_song_type	get_tracks	id	post_attribute	song_currency	song_discoverty	song_hotttnesss	song_type	titleS
'''

'''
audio_summary

'analysis_url'	'audio_md5'	'danceability'	'duration'	'energy'	'key'	'liveness'	'loudness'	'mode'	'speechiness'	'tempo'	'time_signature'
'''
from pyechonest import *
import codecs
import time;

config.ECHO_NEST_API_KEY = "WVLBOJWFXDLQC9TA1"

plist = playlist.static(artist='Art of Noise', results = 100)

for item in plist:
	if item.song_type[0] == '':
		continue
	else:
		time.sleep(0.5);
		dictSum = {}
		dictSum = item.audio_summary
		print item.title.encode('utf8')+';',
		print item.song_type[0]+';',
		print str(dictSum['acousticness'])+';', str(dictSum['danceability'])+';', str(dictSum['duration'])+';', str(dictSum['energy'])+';', str(dictSum['key'])+';', str(dictSum['liveness'])+';', str(dictSum['loudness'])+';', str(dictSum['mode'])+';', str(dictSum['speechiness'])+';', str(dictSum['tempo'])+';', str(dictSum['time_signature'])+';', str(dictSum['valence'])