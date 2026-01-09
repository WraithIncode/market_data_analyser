import matplotlib.pyplot as plt


def plot(z, title):
    fig = plt.figure(figsize=(10, 5))
    plt.plot(z)
    plt.title(title)
    plt.xlabel('Time Period')
    plt.ylabel('Price (In trading units)')
    return fig
