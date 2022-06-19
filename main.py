from Libraries import *
from showPrediction import from_img, from_selfcamera, HarryPotter_test, video_test
import MainWindow



if __name__ == '__main__':
    model = load_model('fer_model.h5')
    # main = MainWindow.MainWindow(Tk(), model)
    # main.draw_widgets()
    # main.root.mainloop()
    video_test(model)

