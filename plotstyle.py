# -*- coding: utf-8 -*-
from colors import default_color_cycler

class PlotStyle():
    def __init__(self, singlecolumn, plotnumber, verticalplot, journal):

        _width, _height = self.makesize(singlecolumn, plotnumber, verticalplot, journal)


        acsparams = {'font.family': 'sans-serif',
                   'font.serif': ['Times', 'Computer Modern Roman'],
                   'font.sans-serif': ['Helvetica', 'Computer Modern Sans serif'],
                   'font.size': 9,
                   'text.usetex': True,
                   # To force LaTeX use Helvetica fonts.
                   'text.latex.preamble': [r'\usepackage{siunitx}',
                                           r'\sisetup{detect-all}',
                                           r'\usepackage{helvet}',
                                           r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
                                           r'\sansmath'],
                   'axes.prop_cycle': default_color_cycler,
                   'axes.labelsize': 9.5,
                   'axes.linewidth': 1,
                   'figure.figsize': (_width, _height),
                   'figure.subplot.left': 0.125,
                   'figure.subplot.right': 0.95,
                   'figure.subplot.bottom': 0.1,
                   'figure.subplot.top': 0.95,

                   'savefig.dpi': 300,
                   'savefig.format': 'tiff',

                   'legend.fontsize': 8.5,
                   'legend.frameon': False,
                   'legend.numpoints': 1,
                   'legend.handlelength': 2,
                   'legend.scatterpoints': 1,
                   'legend.labelspacing': 0.5,
                   'legend.markerscale': 0.9,
                   'legend.handletextpad': 0.5,  # pad between handle and text
                   'legend.borderaxespad': 0.5,  # pad between legend and axes
                   'legend.borderpad': 0.5,  # pad between legend and legend content
                   'legend.columnspacing': 1,  # pad between each legend column

                   # 'text.fontsize' : 8,
                   'xtick.labelsize': 9,
                   'ytick.labelsize': 9,

                   'lines.linewidth': 1.1,
                   'lines.markersize': 4,
                   # 'lines.markeredgewidth': 0,
                   # 0 will make line-type markers, such as '+', 'x', invisible
                   }

        rscparams = {'font.family': 'sans-serif',
                   'font.serif': ['Times', 'Computer Modern Roman'],
                   'font.sans-serif': ['Helvetica', 'Arial',
                                       'Computer Modern Sans serif'],
                   'font.size': 8,
                   'text.usetex': True,
                   # To force LaTeX use Helvetica fonts.
                   'text.latex.preamble': [r'\usepackage{siunitx}',
                                           r'\sisetup{detect-all}',
                                           r'\usepackage{helvet}',
                                           r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
                                           r'\sansmath'],
                   'axes.prop_cycle': default_color_cycler,
                   'axes.labelsize': 8,
                   'axes.linewidth': 1,

                   'figure.figsize': (_width, _height),
                   'figure.subplot.left': 0.125,
                   'figure.subplot.right': 0.95,
                   'figure.subplot.bottom': 0.1,
                   'figure.subplot.top': 0.95,

                   'savefig.dpi': 300,
                   'savefig.format': 'eps',

                   'legend.fontsize': 8,
                   'legend.frameon': False,
                   'legend.numpoints': 1,
                   'legend.handlelength': 2,
                   'legend.scatterpoints': 1,
                   'legend.labelspacing': 0.5,
                   'legend.markerscale': 0.9,
                   'legend.handletextpad': 0.5,  # pad between handle and text
                   'legend.borderaxespad': 0.5,  # pad between legend and axes
                   'legend.borderpad': 0.5,  # pad between legend and legend content
                   'legend.columnspacing': 1,  # pad between each legend column

                   # 'text.fontsize' : 7,  # use font.size for Matplotlib 1.4.2+
                   'xtick.labelsize': 8,
                   'ytick.labelsize': 8,

                   'lines.linewidth': 1,
                   'lines.markersize': 4,
                   # 'lines.markeredgewidth' : 0,
                   # 0 will make line-type markers, such as '+', 'x', invisible
                   }

        webparams = {'font.family': 'sans-serif',
                   'font.serif': ['Bitstream Vera Serif', 'Computer Modern Roman'],
                   'font.sans-serif': ['Helvetica', 'Arial', 'Lucida Grande'],
                   'font.size': 7,
                   'font.weight': 'normal',
                   'text.usetex': True,
                   # To force LaTeX use Helvetica fonts.
                   'text.latex.preamble': [r'\usepackage{siunitx}',
                                           r'\sisetup{detect-all}',
                                           r'\usepackage{helvet}',
                                           r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
                                           r'\sansmath'],
                   'axes.prop_cycle': default_color_cycler,
                   'axes.labelsize': 'medium',
                   'axes.labelweight': 'normal',
                   'axes.linewidth': 0.8,

                   'figure.figsize': (_width, _height),
                   'figure.subplot.left': 0.125,
                   'figure.subplot.right': 0.95,
                   'figure.subplot.bottom': 0.1,
                   'figure.subplot.top': 0.95,

                   'savefig.dpi': 150,
                   'savefig.format': 'png',

                   'legend.fontsize': 'small',
                   'legend.frameon': False,
                   'legend.numpoints': 1,
                   'legend.handlelength': 2,
                   'legend.scatterpoints': 1,
                   'legend.labelspacing': 0.5,
                   'legend.markerscale': 0.9,
                   'legend.handletextpad': 0.5,  # pad between handle and text
                   'legend.borderaxespad': 0.5,  # pad between legend and axes
                   # pad between legend and legend content
                   'legend.borderpad': 0.5,
                   # pad between each legend column
                   'legend.columnspacing': 1,

                   # 'text.fontsize' : 'medium',

                   'xtick.major.size': 3,
                   # 'xtick.minor.size': 2,
                   'xtick.major.width': 0.8,
                   # 'xtick.minor.width': 0.5,
                   'xtick.major.pad': 2,
                   # 'xtick.minor.pad': 4,
                   # 'xtick.color' : k,
                   'xtick.labelsize': 'medium',
                   # 'xtick.direction': 'in',

                   'ytick.major.size': 3,
                   # 'ytick.minor.size': 2,
                   'ytick.major.width': 0.8,
                   # 'ytick.minor.width': 0.5,
                   'ytick.major.pad': 2,
                   # 'ytick.minor.pad': 4,
                   # 'ytick.color': k,
                   'ytick.labelsize': 'medium',
                   # 'ytick.direction' : 'in',

                   'lines.linewidth': 0.8,
                   'lines.markersize': 3,
                   # 'lines.markeredgewidth' : 0,
                   # 0 will make line-type markers, such as '+', 'x', invisible
               }

        presparams = {'font.family': 'sans-serif',
                   'font.serif': ['Times', 'Computer Modern Roman'],
                   'font.sans-serif': ['Helvetica', 'Arial', 'Lucida Grande'],
                   'font.size': 12,
                   'font.weight': 'normal',
                   'text.usetex': True,
                   # To force LaTeX use Helvetica fonts.
                   'text.latex.preamble': [r'\usepackage{siunitx}',
                                           r'\sisetup{detect-all}',
                                           r'\usepackage{helvet}',
                                           r'\usepackage[eulergreek,EULERGREEK]{sansmath}',
                                           r'\sansmath'],
                   'axes.prop_cycle': default_color_cycler,
                   'axes.labelsize': 'medium',
                   'axes.labelweight': 'normal',
                   'axes.linewidth': 1.5,

                   'figure.figsize': (_width, _height),
                   'figure.subplot.left': 0.125,
                   'figure.subplot.right': 0.95,
                   'figure.subplot.bottom': 0.1,
                   'figure.subplot.top': 0.95,

                   'savefig.dpi': 300,
                   'savefig.format': 'pdf',

                   'legend.fontsize': 'small',
                   'legend.frameon': False,
                   'legend.numpoints': 1,
                   'legend.handlelength': 2,
                   'legend.scatterpoints': 1,
                   'legend.labelspacing': 0.5,
                   'legend.markerscale': 0.9,
                   'legend.handletextpad': 0.5,  # pad between handle and text
                   'legend.borderaxespad': 0.5,  # pad between legend and axes
                   'legend.borderpad': 0.5,  # pad between legend and legend content
                   'legend.columnspacing': 1,  # pad between each legend column

                   # 'text.fontsize': 'medium',

                   'xtick.major.size': 6,
                   # 'xtick.minor.size' : 2,
                   'xtick.major.width': 1.5,
                   # 'xtick.minor.width' : 0.5,
                   # 'xtick.major.pad' : 4,
                   # 'xtick.minor.pad' : 4,
                   # 'xtick.color' : k,
                   'xtick.labelsize': 'medium',
                   # 'xtick.direction' : 'in',

                   'ytick.major.size': 6,
                   # 'ytick.minor.size' : 2,
                   'ytick.major.width': 1.5,
                   # 'ytick.minor.width' : 0.5,
                   # 'ytick.major.pad' : 4,
                   # 'ytick.minor.pad' : 4,
                   # 'ytick.color' : k,
                   'ytick.labelsize': 'medium',
                   # 'ytick.direction' : 'in',

                   'lines.linewidth': 1.5,
                   'lines.markersize': 6,
                   # 'lines.markeredgewidth' : 0,
                   # 0 will make line-type markers, such as '+', 'x', invisible
                   }

        if journal == "ACS":
            self._params = acsparams
        elif journal == "RSC":
            self._params = rscparams
        elif journal == "Web":
            self._params = webparams
        elif journal == "Presentation":
            self._params = presparams

    def get_params(self):
        return self._params

    def makesize(self, singlecolumn, plotnumber, verticalplot, journal):
        # Constants from ACS Authour Guidelines.
        if journal == "ACS":
            width_single_column = 3.25
            width_double_column = 7.00
        elif journal == "RSC":
            width_single_column = 3.26  # 8.3 cm
            width_double_column = 6.73  # 17.1 cm
        elif journal == "Web":
            _width_normal_px = 440
            save_dpi = 150
            width_normal = self.point2inch(_width_normal_px, save_dpi)
            width_tiny = 0.5 * width_normal
            width_small = 0.8 * width_normal
            width_large = 1.2 * width_normal
            width_large2 = 1.5 * width_normal
            width_huge = 1.8 * width_normal
            width_single_column, width_double_column = width_normal, width_normal
        elif journal == "Presentation":
            _width_full_pt = 1024  # Units in number of points (or dots)
            _width_normal_pt = int(_width_full_pt / 3.0)
            width_normal = self.point2inch(_width_normal_pt)
            width_tiny = 0.5 * width_normal
            width_small = 0.8 * width_normal
            width_large = 1.2 * width_normal
            width_large2 = 1.5 * width_normal
            width_huge = 1.8 * width_normal
            width_full = 0.9 * self.point2inch(_width_full_pt)  # use 90% of presentation page.
            width_single_column, width_double_column = width_normal, width_normal


        if singlecolumn:
            hwr = 0.8
            if (plotnumber == 2) and verticalplot:
                hwr = 1.5
            if (plotnumber == 3) and verticalplot:
                hwr = 2.2
            if (plotnumber == 4) and verticalplot:
                hwr = 2.6
        else:
            hwr = 0.5
            if plotnumber == 2:
                hwr = 0.46
            if plotnumber == 3:
                hwr = 0.3
            if plotnumber == 4:
                hwr = 0.7

        height_width_ratio = hwr * 1.1  # = height / width

        if singlecolumn:
            _width = width_single_column
            _height = width_single_column * height_width_ratio
            if plotnumber == 4 and not verticalplot:
                _width = 2*_width
                _height = 2*_height
        else:
            _width = width_double_column
            _height = width_double_column * height_width_ratio

        return _width, _height


    def point2inch(self, npt, dpi=72.0):
        return 1.0 * npt / dpi