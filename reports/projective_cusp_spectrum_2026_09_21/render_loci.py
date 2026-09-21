"""Reporting-only static figure of the verified loci, not a spectral solver."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(10,4.7),layout='constrained')
for row in (0,1,2):
    ax.hlines(row,-4,4,color='#b9c3cc',linestyle=':',linewidth=1)
for row,c,label in ((1,17,r'$17\pm12\sqrt{2}$'),
                    (0,7,r'$7\pm4\sqrt{3}$')):
    x=np.arccosh(c)
    ax.scatter([-x,x],[row,row],s=100,color='#12677c',zorder=3)
    ax.text(0,row+.12,'q = '+label,ha='center',color='#12677c',fontsize=12)
ax.scatter([0],[2],s=110,marker='D',facecolors='white',edgecolors='#963f71',zorder=3)
ax.text(0,2.2,'q = 1: ordinary H1 only; excluded from the cusp L2 theorem',
        ha='center',color='#963f71',fontsize=10)
ax.axvline(0,color='#dadee2',linewidth=1,zorder=0)
ax.set_yticks([0,1,2],[r'$\chi=\pm i$',r'$\chi=-1$',r'$\chi=1$'])
ax.set_xlim(-4,4)
ax.set_ylim(-.45,2.65)
ax.set_xlabel('log q  (representation parameter, not a physical mass or coupling)',fontsize=10)
ax.set_title('Exact cohomology loci, not a completed physical vacuum',fontsize=14,pad=20)
fig.supxlabel('Filled points: one normalizable coefficient mode in each dual sector,\n'
              'for smooth completions in the declared end-norm class. Generic H1 = 0.',fontsize=10)
ax.spines[['top','right','left']].set_visible(False)
ax.tick_params(axis='y',length=0,pad=12)
fig.savefig(Path(__file__).with_name('EXCEPTIONAL_LOCI.png'),dpi=160)
