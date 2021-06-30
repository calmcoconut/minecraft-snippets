import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

# mc.postToChat("Hello world")
position = mc.player.getTilePos()
x,y,z = position.x,position.y,position.z
# mc.postToChat(x)

mc.player.setTilePos(-1700,88,-140)

melonBlock = 103
mc.setBlock(x,y,z, melonBlock)
mc.setBlock(x,y+1,z, melonBlock)
mc.setBlock(x,y+2,z, melonBlock)
