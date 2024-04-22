from ranger.ext.img_display import ImageDisplayer, register_image_displayer
from subprocess import Popen, PIPE
import json

@register_image_displayer("swayimg")
class SWAYIMGImageDisplayer(ImageDisplayer):
    """
    Implementation of ImageDisplayer using swayimg
    """
    def __init__(self):
        self.process = None
        self.path = None
        self.start_x = None
        self.ranger_rect = None

    def draw(self, path, start_x, start_y, width, height):
        if not self.path or self.path != path:
            self.clear(start_x, start_y, width, height)
            self.path=path
        if not self.start_x or self.start_x != start_x:
            tree = Popen(['swaymsg','-t','get_tree'],stdout=PIPE)
            tree_json=json.loads(tree.stdout.read())
            tree.terminate()
            for n1 in tree_json.get("nodes"):
                for n2 in n1.get("nodes"):
                    for n3 in n2.get("nodes"):
                        if "ranger" == n3.get("name"):
                            self.ranger_rect = n3.get("rect")
            self.start_x = start_x
        if not self.process:
            ## alacritty font size 9.5
            self.process = Popen(['swayimg','--class','swayimg_ranger','-p',str(int(self.ranger_rect["x"])+int(start_x*8))+','+str(int(self.ranger_rect["y"])+int(start_y*9.5)),'-g',str(int(width*8))+','+str(int(height*9.5)),path], cwd=self.working_dir,stdout=PIPE, stderr=PIPE)

    def clear(self, start_x, start_y, width, height):
        self.start_x = None
        self.ranger_rect = None
        self.quit()

    def quit(self):
        if self.process:
            self.process.terminate()
            self.process = None