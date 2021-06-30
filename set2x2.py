from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")


pos = mc.player.getTilePos()
x,y,z = pos.x,pos.y,pos.z

stone = 1
#mc.setBlocks(x,y,z,x+1,y+1,z+1,stone)

#create 4x4x4 with 2x3x2 air cube

air =0
lava=10
mc.setBlocks(x,y,z,x+3,y+3,z+3,stone)
mc.setBlocks(x+1,y+1,z+1,x+2,y+3,z+2,lava)
