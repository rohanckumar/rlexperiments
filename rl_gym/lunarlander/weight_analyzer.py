import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

WEIGHTS_FILENAME = "weights.npy"

with open(WEIGHTS_FILENAME, 'rb') as f:
    data = np.load(f, allow_pickle=True)

def weights_diff(model_1, model_2):
    assert model_1.keys() == model_2.keys(), "Layer names not identical."
    ret = {}
    for key in model_1.keys():
        weights_1 = model_1[key]
        weights_2 = model_2[key]
        assert weights_1.shape == weights_2.shape, "Layer {} not same shape for both models.".format(key)
        ret[key] = weights_2 - weights_1
    return ret

def heatmap(model, title="Plot", set_abs=True, save=False, save_as="plot.png"):
    fig = plt.figure(figsize=(12, 12))
    gs = GridSpec(len(model.keys())*3, 2)

    vcount = 0
    for count, (name, weights) in enumerate(model.items()):
        if len(weights.shape) == 1:
            weights = weights.reshape(1, -1)
            ax = plt.subplot(gs[vcount, 1])
            vcount += 6
        else:
            ax = plt.subplot(gs[vcount:vcount+4, 0])
        ax.set_title(name)
        if set_abs:  # SET WEIGHTS TO ABS FOR PLOTTING
            weights = np.absolute(weights)
        ax.imshow(weights, cmap='hot', interpolation='nearest')

    plt.suptitle(title)
    if save:
        plt.savefig(save_as, bbox_inches='tight')

def npy_save(file, model):
    with open(file, 'wb') as f:
        np.save(f, model)

# Sets values in model below limit to 0 for readability
def truncate(model, lim):
    for arr in model.values():
        arr[arr<lim] = 0

# Episodes of models to compare
# EP_1 = 100
# EP_2 = 200
# EP_3 = 300

# diff_1_2 = weights_diff(data[EP_1-1], data[EP_2-1])
# diff_2_3 = weights_diff(data[EP_2-1], data[EP_3-1])

# diff_updates = weights_diff(diff_1_2, diff_2_3)

# print("\n\n------------------------------ DIFFERENCE B/W UPDATES FROM {} TO {} AND {} TO {} ------------------------------\n\n".format(EP_1, EP_2, EP_2, EP_3))
# print(diff_1_2)
# print("\n\n------------------------------ DIFFERENCE B/W UPDATES FROM {} TO {} AND {} TO {} ------------------------------\n\n".format(EP_1, EP_2, EP_2, EP_3))
# print(diff_2_3)
# print("\n\n------------------------------ DIFFERENCE B/W UPDATES FROM {} TO {} AND {} TO {} ------------------------------\n\n".format(EP_1, EP_2, EP_2, EP_3))
# print(diff_updates)

# heatmap(diff_1_2, "Difference b/w weights at ep {} and ep {}".format(EP_1, EP_2), save=False, save_as="EPS_{}_{}.png".format(EP_2, EP_1))
# heatmap(diff_2_3, "Difference b/w weights at ep {} and ep {}".format(EP_2, EP_3), save=False, save_as="EPS_{}_{}.png".format(EP_3, EP_2))
# heatmap(diff_updates, "Difference b/w updates from {} to {} and {} to {}".format(EP_3, EP_2, EP_2, EP_1), set_abs=False, save=False, save_as="Update_diff_{}_{}_{}.png".format(EP_1, EP_2, EP_3))
# plt.show()

w200 = data[199]
w500 = data[499]

diff_200_500 = weights_diff(data[199], data[499])
new_200 = weights_diff(diff_200_500, data[199])
npy_save("new_200.npy", new_200)