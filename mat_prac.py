import numpy as np
import matplotlib.pyplot as plt


gary = np.arange(0, 10, 0.1)
y = gary * 2 + 4

plt.plot(gary)
plt.plot(y)
plt.legend('celery')
plt.show()
