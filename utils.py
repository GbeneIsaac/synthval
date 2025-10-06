import matplotlib.pyplot as plt

def plot_jsd_comparison(jsd_scores):
    plt.barh(list(jsd_scores.keys()), list(jsd_scores.values()))
    plt.xlabel('JSD Score')
    plt.ylabel('Feature')
    plt.title('Feature-wise Jensen-Shannon Divergence')
    plt.show()
