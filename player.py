from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('MP3 Music Player')
# root.iconbitmap()
root.geometry("500x300")

# Initialize Pygame Box
pygame.mixer.init()

global paused
paused = False


# add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # clean up song name
    song = song.replace("/Users/dan/PycharmProjects/docker/musicPlayer/audio/", "")
    song = song.replace(".mp3", "")
    # add song to song box
    song_box.insert(END, song)


def add_multi_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # loop thru song list and replce dir info and mp3
    for song in songs:
        song = song.replace("/Users/dan/PycharmProjects/docker/musicPlayer/audio/", "")
        song = song.replace(".mp3", "")
        # put in playlist
        song_box.insert(END, song)


# play highlighted song
def play_song():
    song = song_box.get(ACTIVE)
    song = f'/Users/dan/PycharmProjects/docker/musicPlayer/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


# stop playing current song
def stop_song():
    song = song_box.get(ACTIVE)
    song = f'/Users/dan/PycharmProjects/docker/musicPlayer/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.stop()


# pause current song
def pause_song(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# play next song
def next_song():
    # current song
    song_box.select_set(0)
    next_one = song_box.curselection()

    # Add one to curr song
    next_one = len(next_one)
    song_box.select_set(next_one)

    # get song
    song = song_box.get(next_one)
    song = f'/Users/dan/PycharmProjects/docker/musicPlayer/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def last_song():
    # current song
    song_box.select_set(0)
    next_one = song_box.curselection()

    # Add one to curr song
    next_one = len(next_one)
    print(next_one)
    prev = next_one - 1
    print(f'last song {prev}')
    song_box.select_set(prev)

    # get song
    song = song_box.get(prev)
    song = f'/Users/dan/PycharmProjects/docker/musicPlayer/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


# only delete one song
def del_one_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


# delete all selected songs in song box
def del_all():
    song_box.delete(0, END)
    pygame.mixer.music.stop()


# create playlist box
song_box = Listbox(root, bg="white", fg="black", width=60, selectbackground="blue", selectforeground='white')
song_box.pack(pady=20)

# creating buttons
back_btn = PhotoImage(file='playerImages/004-rewind.png')
forward_btn = PhotoImage(file='playerImages/003-forward.png')
play_btn = PhotoImage(file='playerImages/001-play.png')
pause_btn = PhotoImage(file='playerImages/002-pause.png')
stop_btn = PhotoImage(file='playerImages/005-stop.png')

# create player control frame
controls_frame = Frame(root)
controls_frame.pack()

# create control buttons
back_button = Button(controls_frame, image=back_btn, borderwidth=0, command=last_song)
forward_button = Button(controls_frame, image=forward_btn, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn, borderwidth=0, command=play_song)
pause_button = Button(controls_frame, image=pause_btn, borderwidth=0, command=lambda: pause_song(paused))
stop_button = Button(controls_frame, image=stop_btn, borderwidth=0, command=stop_song)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=3, padx=10)
play_button.grid(row=0, column=1, padx=10)
pause_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Song", menu=add_song_menu)
add_song_menu.add_command(label='Add One Song To Playlist', command=add_song)

# add many songs
add_song_menu.add_command(label='Add Songs To Playlist', command=add_multi_songs)

# delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)

remove_song_menu.add_command(label="Delete song from playlist", command=del_one_song)
remove_song_menu.add_command(label="Delete all songs from playlist", command=del_all)

root.mainloop()
