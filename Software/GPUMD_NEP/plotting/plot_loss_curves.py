import pandas as pd
from ase.units import GPa
from calorine.nep import get_parity_data, read_loss, read_structures
from matplotlib import pyplot as plt
from pandas import DataFrame, concat as pd_concat
from sklearn.metrics import r2_score, mean_squared_error

loss = read_loss('loss.out')

fig, axes = plt.subplots(figsize=(6.0, 4.0), nrows=2,sharex=True, dpi=120)

ax = axes[0]
ax.set_ylabel('Loss')
ax.plot(loss.total_loss, label='total')
ax.plot(loss.L2, label='$L_2$')
ax.plot(loss.L1, label='$L_1$')
ax.set_yscale('log')
ax.legend()

ax = axes[1]
ax.plot(loss.RMSE_E_train, label='energy (eV/atom)')
ax.plot(loss.RMSE_F_train, label='forces (eV/?~E)')
ax.plot(loss.RMSE_V_train, label='virial (eV/atom)')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Generation')
ax.set_ylabel('RMSE')
ax.legend()

plt.tight_layout()
fig.subplots_adjust(hspace=0, wspace=0)
fig.align_ylabels(axes)
plt.savefig('loss_curves.png')
