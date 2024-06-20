import pandas as pd
from ase.units import GPa
from calorine.nep import get_parity_data, read_loss, read_structures
from matplotlib import pyplot as plt
from pandas import DataFrame, concat as pd_concat
from sklearn.metrics import r2_score, mean_squared_error

training_structures, _ = read_structures('model/nepmodel_full')

units = dict(
    energy='eV/atom',
    force='eV/?~E',
    virial='eV/A**3/atom',
    stress='GPa',
)

fig, axes = plt.subplots(figsize=(9.0, 2.6), ncols=4, dpi=120)
kwargs = dict(alpha=0.2, s=0.5)

for icol, (prop, unit) in enumerate(units.items()):
    df = get_parity_data(training_structures, prop, flatten=True)
    R2 = r2_score(df.target, df.predicted)
    rmse = mean_squared_error(df.target, df.predicted, squared=False)
    print(rmse)
    ax = axes[icol]
    ax.set_xlabel(f'Target {prop} ({unit})')
    ax.set_ylabel(f'Predicted ({unit})')
    ax.scatter(df.target, df.predicted, **kwargs)
    ax.set_aspect('equal')
    mod_unit = unit.replace('eV', 'meV').replace('GPa', 'MPa')
    ax.text(0.1, 0.75, f'{1e3*rmse:.1f} {mod_unit}\n' + '$R^2= $' + f' {R2:.5f}', transform=ax.transAxes)

fig.tight_layout()
plt.savefig('parity_plots.png')
