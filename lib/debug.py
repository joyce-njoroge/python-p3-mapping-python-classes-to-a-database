#!/usr/bin/env python3

import config
import song

CONN = config.CONN
CURSOR = config.CURSOR
Song = song.Song

#from config import CONN, CURSOR
#from song import Song
Song.create_table()
#CURSOR.execute("PRAGMA table_info(songs)").fetchall()
hello = Song("Hello", "25")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()

hello.id
# => 1
despacito.id
# => 2
song = Song("Hold On", "Born to Sing")
song.save()
song.id

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
