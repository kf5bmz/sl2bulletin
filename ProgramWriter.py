#
# Sugar Land 2nd Ward HTML Program Writer
#
# Pete Slater
# June 2022

import hymndict # Titles and links to hymns
import htmlpy
from htmlpy import oneliner as e
import artlinks # Links to artwork
import sys

'''
Define functions for formatting each of the items that can appear in a program.
Build the program in the main script by calling the functions.

'''
def officer(role, officer, page):
    page.p(e.b(role+":")+" "+officer,align="center")

def pagetitle(unit, meeting, meetdate,page):
    page.h1(unit, align="center")
    page.h2(meeting, align="center")
    page.h2(meetdate, align="center")

def speaker(name, page):
    page.h2("Speaker", align="center")
    page.p(name,align="center")
    
def testimonies(page):
    page.h2("Bearing of Testimonies", align="center")

def music(number, description, page):
    page.h2(description,align="center")
    [hymntitle, hymnurl] = hymndict.hymns[number]
    page.p(e.a("#" + str(number)+", "+hymntitle, href=hymnurl),align="center")
    
def specialmusic(performers,page,title=None,accompanist=None):
    page.h2("Special Musical Number",align="center")
    if title != None:
        page.p(e.i(title),align="center")
    page.p(performers,align="center")
    if accompanist != None:
        page.p("Acc. by " + accompanist, align="center")
        
def thought(text, author, page):
    page.hr()
    page.p(text, align="center")
    page.p("- "+author,align="center")
 
# Announcements are passed as a list if text strings
def announcements(textlist,page):
    page.hr()
    page.h1("Announcements", align="center")
    for txt in textlist:
        page.p(txt,align="center")

# Place some links, passed as a list containing text and url
def links(linklist, page):
    page.hr()
    page.h1("Links", align="center")
    for link in linklist:
        page.p(e.a(link[0], href=link[1], target="_blank", rel="noreferrer noopener"),align="center")
    
title = "Sugar Land Second Ward"
header = "Sacrament Meeting"
footer = ""
styles = ( 'layout.css', 'alt.css', 'images.css' )

page = htmlpy.page( )
page.init()
page.br( )
 
# Make sure it will look good on all devices
page.meta(name="viewport", content="width=device-width, initial-scale=1.0")

# Define the elements on the current week's programs here

pagetitle("Sugar Land 2nd Ward", "Sacrament Meeting", "July 17, 2022", page)

# Place an artwork from the imported dictionary of links
#page.p(e.img(width=299, height=300*0.8, src=artlinks.art[2]), align="center")
page.p(e.img(style="max-width:50%;height:auto;", src=artlinks.art[3]), align="center")

officer("Presiding","Bishop Joey Powell", page)
officer("Conducting","Bishop Joey Powell", page)

music(78,"Opening Hymn",page)  
music(196,"Sacrament Hymn", page) 

# Uncomment this line for fast and testimony meeting
#testimonies(page)

# Use lines like these to form the speaking part of the program
speaker("Reuben Ozomah", page)
speaker("Rita Ozomah", page)
#specialmusic("Diana Quam (Violin), Dallin Arnold (Viola), Claire Draney (Viola), and Jared Draney (Piano)",
#             page, "Be Still My Soul")
speaker("Ben Powell", page)
music(118,"Closing Hymn",page)

# Spiritual thought
quote = ('I am the resurrection, and the life: he that believeth in me. though he were dead, yet shall he live.')
author = "John 11:25"
thought(quote, author, page)

# Make a list of announcements, then post to the page
txtlist = (
           "Stake Family Beach Day, Saturday August 27 10:00 am at Freeport Beach",
           "Send announcements to bvl2clerk@gmail.com"
           )
announcements(txtlist, page)

# Make a list of links, then post
linklist = (
        ("Sign up to feed the missionaries","https://www.signupgenius.com/go/10c0e4baca82ea7fb6-dinner2"),
        ("Help at secondmile.org","https://secondmile.org")
        )
links(linklist, page)

print (page)# -*- coding: utf-8 -*

original_stdout = sys.stdout
with open('program.html', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(page)
    sys.stdout = original_stdout # Reset the standard output to its original value
"""
End of script
"""

