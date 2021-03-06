"""Stellar evolution validation figure."""
import numpy as np
import subprocess
import vplot as vpl
import matplotlib.pyplot as pl
cmap = pl.get_cmap('inferno')


star = """#
sName	                  s%02d
saModules	              stellar
dMass                     %.5f
dAge                      1e7
sStellarModel             baraffe
dSatXUVFrac               1.e-3
dSatXUVTime               -0.1
saOutputOrder Age -Luminosity -Radius Temperature -RotPer LXUVStellar
"""

system = """#
sSystemName               system
iVerbose                  0
bOverwrite                1
saBodyFiles               %s
sUnitMass                 solar
sUnitLength               AU
sUnitTime                 YEARS
sUnitAngle                d
bDoLog                    1
iDigits                   6
dMinValue                 1e-10
bDoForward                1
bVarDt                    1
dEta                      0.1
dStopTime                 5e9
dOutputTime               1e7
"""


def write_in(masses):
    """Write the .in files to disk."""
    nfiles = len(masses)

    # Write the vpl.in file
    with open("vpl.in", "w") as file:
        filenames = " ".join(["s%02d.in" % n for n in range(nfiles)])
        print(system % filenames, file=file)

    # Write each star file
    for n in range(nfiles):
        with open("s%02d.in" % n, "w") as file:
            print(star % (n, masses[n]), file=file)


def run(masses):
    """Run vplanet and collect the output."""
    #write_in(masses)
    #subprocess.call(['vplanet', 'vpl.in'])
    output = vpl.GetOutput()
    age = output.bodies[0].Age
    radius = [output.bodies[n].Radius for n in range(len(masses))]
    temp = [output.bodies[n].Temperature for n in range(len(masses))]
    lum = [output.bodies[n].Luminosity for n in range(len(masses))]
    lxuv = [output.bodies[n].LXUVStellar for n in range(len(masses))]
    prot = [output.bodies[n].RotPer for n in range(len(masses))]
    return age, radius, lum, lxuv, temp, prot


# Create the figure
fig, ax = pl.subplots(2, 2, figsize=(10, 6))
fig.subplots_adjust(right=0.825, wspace=0.30)

masses = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
age, radius, lum, lxuv, temp, prot = run(masses)

for n, m in enumerate(masses):
    ax[0, 0].plot(age, radius[n], label="%.1f" % m, color=cmap(0.8 * m))
    ax[0, 1].plot(age, lum[n], label="%.1f" % m, color=cmap(0.8 * m))
    ax[1, 0].plot(age, temp[n], label="%.1f" % m, color=cmap(0.8 * m))
    ax[1, 1].plot(age, prot[n], label="%.1f" % m, color=cmap(0.8 * m))

for axis in ax.flatten():
    axis.set_xscale('log')
ax[0, 1].set_yscale('log')
ax[1, 0].set_xlabel('Time (Gyr)', fontsize=14)
ax[1, 1].set_xlabel('Time (Gyr)', fontsize=14)
ax[0, 0].set_ylabel(r'Radius ($\mathrm{R}_\oplus$)', fontsize=14)
ax[0, 1].set_ylabel(r'Luminosity ($\mathrm{L}_\oplus$)', fontsize=14)
ax[1, 0].set_ylabel(r'Temperature ($\mathrm{K}$)', fontsize=14)
ax[1, 1].set_ylabel(r'Rotation Period (days)', fontsize=14)
leg = ax[1, 1].legend(loc=(1.1, 0.5), title='Mass ($\mathrm{M}_\oplus$)')
leg.get_title().set_fontweight('bold')
fig.savefig('stellar.pdf', bbox_inches='tight')
