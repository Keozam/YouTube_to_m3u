#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/benmoose39     #
#########################################################################
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    import subprocess, sys
    for client in ["tv", "android"]:
        try:
            result = subprocess.run(
                ["yt-dlp", "-g", "--no-warnings",
                 "--extractor-args", f"youtube:player_client={client}",
                 url],
                capture_output=True, text=True, timeout=12
            )
            link = result.stdout.strip().splitlines()
            if link and link[0].startswith("http"):
                print(link[0])
                return
            else:
                print(f"# FALLO {client}: {result.stderr.strip()[:200]}", file=sys.stderr)
        except Exception as e:
            print(f"# ERROR {client}: {e}", file=sys.stderr)
    print('https://raw.githubusercontent.com/Keozam/YouTube_to_m3u/main/assets/moose_na.m3u')
    return
print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}" CUID="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    #os.system('rm temp.txt')
    os.system('rm watch*')
