import re, urllib, os, sys
import urllib.request
import urllib.parse
import argparse

user_input = input
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()
urlopen = urllib.request.urlopen

def check_args(args=None):
    parser = argparse.ArgumentParser(description="YOUTUBE MP3 DOWNLOADER LIGHT")
    parser.add_argument('--output', '-o',
                        metavar='PATH',
                        default='downloads/',
                        help="Path to write downloads to")
    return parser.parse_args(args)


def get_title(url):
    website = urlopen(url).read()
    title = str(website).split('<title>')[1].split('</title>')[0]
    return title

def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def init_message():
    print("Built with <3 By Sagar Vakkala (^^) \n")
    print("YOUTUBE MP3 DOWNLOADER LIGHT \n \n")

def exit_message(t):
    print("\n %s Has been downloaded" % t)


def download(song=None, folder_path=None):
    if not song:
        song = user_input('Enter the name of the song or the URL: ')

    if "youtube.com/" not in song:

        try:
            query = encode({"search_query" : song})
            web_content = urlopen("http://www.youtube.com/results?" + query)
            results = re.findall(r'href=\"\/watch\?v=(.{11})', web_content.read().decode())
        except:
            print("There's some problem in your network")
            return None

        command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "{}/%(title)s.%(ext)s" '.format(os.path.normpath(folder_path)) + results[0]

    else:
        command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "{}/%(title)s.%(ext)s" '.format(os.path.normpath(folder_path)) + song[song.find("=")+1:]
        song = get_title(song)
        print(song)

    try:
        print("Downloading %s" % song)
        os.system(command)
        exit_message(song)
    except:
        print('Error downloading %s' %song)
        return None

def main():
    path = check_args(sys.argv[1:]).output
    try:
        screen_clear()
        init_message()
        while True:
            download(folder_path=path)
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
    exit(0)
