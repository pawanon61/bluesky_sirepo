#  get graph for simulation data
import argparse
from extract_simulation_data import *
import matplotlib
matplotlib.use("Agg")  # so that matplotlib doesnot look for display environment
import matplotlib.pyplot as plt

def plot_simulation_data():

    parser = argparse.ArgumentParser(description='Plot image based on input file')
    # TODO make it required = True
    parser.add_argument('-d', '--data_file', dest='data_file', default='',
                        help ='input data file')
    parser.add_argument('-g', '--graph', dest='graph', default='',
                        help='create graph', action='store_true')
    args = parser.parse_args()

    initial_data = {'photon': {}, 'horizontal': {}, 'vertical': {},}
    matrix = [[]]
    try:
        get_parameters(initial_data, file_name=args.data_file)
    except:
        print('no data file found - specify with (-d <filename>)')
        quit()
    number_of_horizontal_points = initial_data['horizontal']['points']
    number_of_vertical_points = initial_data['vertical']['points']

    if args.graph and args.data_file:

        img = np.loadtxt(args.data_file)
        img = img.reshape((number_of_vertical_points, number_of_horizontal_points))

        # return tuple (row,column)
        max_index = np.where(img == np.amax(img))
        horizontal = img[max_index[0] , :][0]
        vertical = img[: , max_index[1]]
        f = plt.figure()
        import matplotlib.gridspec as gridspec
        gs = gridspec.GridSpec(2, 2, width_ratios=[2, 1], height_ratios=[2, 1])
        ax1 = plt.subplot(gs[0])
        ax2 = plt.subplot(gs[1])
        ax3 = plt.subplot(gs[2])
        ax4 = plt.subplot(gs[3])

        ax1.imshow(img, aspect = 'auto')
        ax1.tick_params(labelbottom = False, labelleft = False)
        yh = list(range(0,len(vertical)))
        ax2.plot(vertical[::-1], yh)
        ax2.tick_params(labelleft=False)
        ax3.plot(horizontal)
        ax3.tick_params(labelbottom=False)
        ax4.text(0, 0.6, "Horizontal range (%.3f, %.3f) um\nVertical range (%.3f, %.3f) um" %(initial_data['horizontal']['initial_position']*10**6, initial_data['horizontal']['final_position']*10**6,\
            initial_data['vertical']['initial_position']*10**6, initial_data['vertical']['final_position']*10**6), fontsize = 6)
        ax4.tick_params(labelbottom = False, labelleft = False)
        ax4.set_axis_off()

        plt.savefig("image.png")

    else:
        if args.data_file:
            file = args.data_file
            matrix = populate_matrix_smart(matrix, number_of_horizontal_points, number_of_vertical_points, data_file=file)
            print(initial_data)

plot_simulation_data()



