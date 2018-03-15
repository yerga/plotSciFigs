#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Short description of this Python module.
Longer description of this module.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Daniel Martin-Yerga"
__email__ = "dyerga@gmail.com"
__copyright__ = "Copyright 2018"
__date__ = "13/03/18"
__license__ = "GPLv3"
__program__ = "plotSciFigs"
__version__ = "0.0.1"

from colors import default_color_cycler as dcc
#from matplotlib.ticker import MultipleLocator


class LinePlot():
    def __init__(self, plotconfig):
        self.plottype, self.filename, self.xlabel1, self.ylabel1, self.ylabel2, self.legends, \
            self.xlimit, self.y1limit, self.y2limit, self.doubleaxis, self.legend1loc, self.legend2loc = plotconfig

    def plot(self, axis, plotdata):
        xdata1, ydata1, xdata2, ydata2 = plotdata

        if self.doubleaxis:
            if self.legends:
                legend1, legend2 = self.legends.split(";;")
                legend1 = legend1.split(";")
                legend2 = legend2.split(";")
            else:
                legend1 = [""]*len(xdata1)
                legend2 = [""]*len(xdata2)
        else:
            if self.legends:
                legend1 = self.legends.split(";")
            else:
                legend1 = [""]*len(xdata1)


        for i in range(len(xdata1)):
            line, = axis.plot(xdata1[i], ydata1[i], ls="-", label=legend1[i])

        self.set_format(axis)

        # TODO: plot colors, plot style (dots, etc.)

        if self.doubleaxis:
            axis2 = axis.twinx()
            for i in range(len(xdata2)):
                line2, = axis2.plot(xdata1[i], ydata1[i], ls="-", color=dcc._left[i+len(xdata1)]['color'], label=legend2[i])

            self.set_format_double(axis2)

            # color=dcc._left[1]['color'], ls="-", label=legends[i+1])

    def set_format(self, axis):
        axis.set_xlabel(self.xlabel1)
        axis.set_ylabel(self.ylabel1)
        if self.xlimit:
            xlim1, xlim2 = self.xlimit.split(";")
            axis.set_xlim(float(xlim1), float(xlim2))
        if self.y1limit:
            ylim1, ylim2 = self.y1limit.split(";")
            axis.set_ylim(float(ylim1), float(ylim2))

        leg = axis.legend(loc=self.legend1loc, shadow=False)

            # if color:
            #     axis.set_ylabel("Abs / a.u.", color=dcc._left[0]['color'])
            #     axis.set_xlabel("Wavelength / nm")
            #     axis.tick_params('y', colors=dcc._left[0]['color'])
            #     axis.set_xlim(250, 750)
            # else:
            #     yml = MultipleLocator(0.5)
            #     axis.xaxis.set_major_locator(yml)
            #     minx = MultipleLocator(0.25)
            #     axis.xaxis.set_minor_locator(minx)

    def set_format_double(self, axis):
        axis.set_ylabel(self.ylabel2)
        axis.legend(loc=self.legend2loc, shadow=False)

        if self.y2limit:
            ylim1, ylim2 = self.y2limit.split(";")
            axis.set_ylim(float(ylim1), float(ylim2))


        #TODO: colors, multiplelocator, annotations, etc.

        #self.ax2.set_ylabel('Intensity / kcounts', color=dcc._left[1]['color'])
        #self.ax2.tick_params('y', colors='r')
        #myl = MultipleLocator(100)
        #ml = MultipleLocator(50)
        #self.ax2.xaxis.set_minor_locator(ml)
        #self.ax2.xaxis.set_major_locator(myl)

        #plt.gcf().text(0.02, 0.98, "a)", fontsize=11, fontweight="bold")
        #plt.gcf().text(0.02, 0.5, "b)", fontsize=11, fontweight="bold")

