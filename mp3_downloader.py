from pytube import YouTube
import os


print('''
     __       ___       __   ___
\ / /  \ |  |  |  |  | |__) |__
 |  \__/ \__/  |  \__/ |__) |___

 __   __                  __        __   ___  __
|  \ /  \ |  | |\ | |    /  \  /\  |  \ |__  |__)
|__/ \__/ |/\| | \| |___ \__/ /~~\ |__/ |___ |  \.
 ''')

# url input from user
yt = YouTube(str(input("\nEnter the URL of the YouTube video: \n>> ")))

audios = yt.streams.filter(only_audio=True, mime_type="audio/mp4")
print('')
print('Title:', yt.title)
print('Author:', yt.author)

print('\nEnter the number of the audio:')
j = 1
for i in audios:
    print(f' {j}. {i.abr}')
    j+=1
id = int(str(input(">> ")) or '0')

# - check input selection
while (id <= 0) or (id >= j):
    print('\nWrong selection. Try again...')
    j = 1
    for i in audios:
        print(f' {j}. {i.abr}')
        j+=1

    id = int(str(input(">> ")) or '0')

audio = yt.streams.filter(only_audio=True, mime_type="audio/mp4")[id-1]

# check for destination to save file
print("\nEnter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = audio.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(f"\n{yt.title} has been successfully downloaded.")
