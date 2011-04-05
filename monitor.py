#!/usr/bin/python

import os
import time
import shutil
import eyeD3

print "Waiting until file appears..."
while 1 :

        doesExist = False
        while doesExist == False :
                if os.path.exists("4Music/Cache/_cache.tmp") :
                        doesExist = True
                else :
                        time.sleep(1)

        print "File has appeared! Waiting until downloaded..."

        oldfilesize = 0
        theSame = 0

        while theSame < 10 :
                if oldfilesize == os.path.getsize("4Music/Cache/_cache.tmp") :
                        theSame = theSame + 1
                else :
                        oldfilesize = os.path.getsize("4Music/Cache/_cache.tmp")
                time.sleep(1)

        print "The file is completely downloaded. Copying now..."

	tempFile = "4Music/"+str(time.time())+".mp3"

        shutil.copyfile("4Music/Cache/_cache.tmp",tempFile)

	audioFile = eyeD3.Mp3AudioFile(tempFile)
	tag = audioFile.getTag()

	if len(tag.getArtist()) > 0 and len(tag.getTitle()) > 0 :
		shutil.copyfile(tempFile,"4Music/"+tag.getArtist()+" - "+tag.getTitle()+".mp3")
		os.remove(tempFile)

        print "File is copied. You can now skip to the next song..."

        doesExist = True
        while doesExist == True :
                if os.path.exists("4Music/Cache/_cache.tmp") == False :
                        doesExist = False
                else :
                        time.sleep(1)

        print "File has been deleted... Sleeping for a second or two..."

        time.sleep(5)

        print "Waiting until next file appears..."

