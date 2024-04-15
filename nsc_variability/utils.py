'''
Compilation of utilities that are useful for timeseries manipulation.
'''

import numpy as np
import matplotlib.pyplot as plt


def phase_fold(mjd, period, mjd0=None, centeredzero=False):
    '''
    Given a series of dates and a period, it phase folds them into 
    a number of cycles.
    
    Parameters
    ----------
    mjd: array-like
        Array of dates to phase fold in Mean Julian Date (MJD).
    period: float
        Period to use for the phase fold, in days.
    mjd0: float, optional
        Initial day to use for the phase fold. Default is the earliest 
        date in mjd.
    centeredzero: boolean, optional
        Whether the phase goes from 0 to 1 or -0.5 to 0.5. Default 
        is False (0 to 1).
    
    Returns
    -------
    phase: array-like
        Converted mjd to phase values.
    '''
    
    if mjd0==None:
        mjd0 = min(mjd)
    
    temp = mjd - mjd0
    nonfold_phase = temp/period
    cycle = np.array(nonfold_phase, dtype=int)
    phase = nonfold_phase - cycle 
    
    if centeredzero:
        phase -= 0.5
    
    return phase

def plot_periodogram(frequency, power, filename='periodogram.png', units='days'):
    '''
    Plots a periodogram based on the power and frequency given.
    
    Parameters
    ----------
    frequency: array-like
        Frequency as 1/period, where the period is measured in days. 
    power: array-like
        Corresponding power for each frequency. Must be the same shape as frequency.
    filename: str, optional
        Name of the file where to store the plot.
    units: str, optional
        Units used for the periodogram plot. Default is days.
        
    Returns
    -------
    Saves a file to disk.
    '''
    
    periods = 1/frequency
    
    fig = plt.figure()
    ax = fig.add_subplot()
        
    ax.plot(periods, power, lw=1.5, color='k')
    ax.set_ylabel('Power')
    ax.set_xlabel(f'Period ({units})')
    ax.set_xscale('log')
    
    fig.savefig(filename,bbox_inches = 'tight')