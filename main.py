from gtts import gTTS
from io import BytesIO
import pygame

class Animal:
  #constructor method
  def __init__(self,name,species):
    self.name=name
    self.species=species

  #method to make the animal make a sound.
  def make_sound(self,sound):
    return f"{self.name} makes a {sound} sound"
    #generating AI sound using gTTS
    tts=gTTS(text=text,lang="en")
    mp3_fp = BytesIO()
    tts.save(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()

#creating objects / instances of the Animal class.
cat=Animal("Whiskers","Cat")
dawg=Animal("Max","Dawg")
seal=Animal("Pinniped","Seal")

#Acessinng attributes and calling methods on objects.
print (cat.name)
print (cat.species)
print (dawg.name)
print (dawg.species)
print (seal.name)
print (seal.species)

print (cat.make_sound("Meow! *paw licking noises*"))
print (dawg.make_sound("Arf!, Woof, Arf!, Woof!"))
print (seal.make_sound("Oar! Oar! Oar! Oar!"))

