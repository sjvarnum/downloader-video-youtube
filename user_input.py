import os
import sys
import youtube_dl

user = os.getlogin()
home_folder = os.getenv('home')
output_folder = 'downloads'
download_folder = os.path.join(home_folder, output_folder)
video_template = '%(uploader)s/%(title)s.%(ext)s'
playlist_template = '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'


def run(url, template):

    '''Pass URL and options to YoutubeDL'''

    ydl_opts = {
    'outtmpl': f'{template}',
    'restrictfilenames': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():

    '''
    - Prompt user for URL
    - Prompt user for type (single video or playlist)
        - Answer with either p for playlist or v for video
    - Video is downloaded to the users Download folder by default 
    '''

    user = os.getlogin()
    home_folder = os.getenv('home')
    output_folder = 'downloads'
    download_folder = os.path.join(home_folder, output_folder)
    video_template = '%(uploader)s/%(title)s.%(ext)s'
    playlist_template = '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'

    url = input('Enter URL: ')
    if not url:
        sys.exit("You need to enter a URL...Exiting.")
    elif url:
        playlist = input("Is this a playlist or a video (p/v)? Enter p or v: ")
        if playlist == 'p':
            playlist = True
            template = f'{download_folder}\\{playlist_template}'
            # print(template)
        elif playlist == 'v':
            playlist = False
            template = f'{download_folder}\\{video_template}'
            # print(template)
        else:
            print('You need to indicate if this is a playlist or not')

    run(url, template)


if __name__ == '__main__':
    main()