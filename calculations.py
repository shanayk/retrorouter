import constants

# Function to calculate Spectrum Bar position and display size
def SpectrumChannelPositioner(channel,num_of_channels):
    bw_to_pixel = int((constants.width/(num_of_channels-1)))
    chan_x = bw_to_pixel*(channel)
    chan_y = int(9*constants.height/10)
    return {"chan_x": chan_x,"chan_y": chan_y,"bw_to_pixel": bw_to_pixel}
# Function to display Channel Name
def channel_name_disp(surf,channel,chan_x,chan_y,font):
    text_surface = font.render("Channel %d" % channel, True, constants.GREEN)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (chan_x,chan_y+25)
    surf.blit(text_surface, text_rect)
# Function to display Data
def stats(surf,data,font):
    text_surface = font.render("Data Transferred: %d" % data, True, constants.GREEN)
    text_rect = text_surface.get_rect()
    text_rect.center = (100, 20)
    surf.blit(text_surface, text_rect)

def button_click(counter,click):
    counter = counter + click
    if counter>10:
        counter = 0
    elif counter<0:
        counter = 10
    else:
        pass

    return counter
