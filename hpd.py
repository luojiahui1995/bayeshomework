import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


def naive_hpd(post):
    sns.kdeplot(post)
    HPD = np.percentile(post, [5, 95])
    plt.plot(HPD, [0, 0], label='HPD {:.2f} {:.2f}'.format(*HPD), linewidth=8, color='k')
    plt.legend(fontsize=16);
    plt.xlabel(r'$\theta$', fontsize=14)
    plt.gca().axes.get_yaxis().set_ticks([])
np.random.seed(1)
post = stats.lognorm.rvs(1,1, size=1000)
naive_hpd(post)
plt.xlim(0, 10)
plt.show()

#np.random.seed(1)
#post = stats.beta.rvs(5, 11, size=1000)
#naive_hpd(post)
#plt.xlim(0, 1)
