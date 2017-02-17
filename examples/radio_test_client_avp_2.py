#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Radio Test Client
# Author: Julian Arnold
# Generated: Thu Feb 16 12:55:41 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from inets_radio import inets_radio  # grc-generated hier_block
from optparse import OptionParser
import gnuradio
import inets
import numpy
import sip
import time
from gnuradio import qtgui
import threading
import csv
import time
import os


class radio_test_client(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Radio Test Client")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Radio Test Client")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "radio_test_client")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.range_rx_gain = range_rx_gain = 10
        self.range_mu = range_mu = 0.6
        self.threshold = threshold = 40
        self.samp_rate = samp_rate = 4e6
        self.rx_gain = rx_gain = range_rx_gain
        
        self.rrc = rrc = firdes.root_raised_cosine(1.0, sps, 1, 0.5, 11*sps)
          
        self.range_noise = range_noise = 0
        self.qpsk_mod = qpsk_mod = gnuradio.digital.constellation_qpsk().base()
        self.qam16_mod = qam16_mod = gnuradio.digital.qam_constellation(16,False).base()
        self.preamble = preamble = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0,0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0,0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1,1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
        self.mu = mu = range_mu
        self.diff_preamble_256 = diff_preamble_256 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0,0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0,0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1,1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
        self.diff_preamble_128 = diff_preamble_128 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0,0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0,0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1,1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0][0:128]
        self.bpsk_mod = bpsk_mod = gnuradio.digital.constellation_bpsk().base()

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'TX')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'RX')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Demod')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'RSSI')
        self.top_layout.addWidget(self.tab)
        self._range_noise_range = Range(0, 1.0, 0.001, 0, 200)
        self._range_noise_win = RangeWidget(self._range_noise_range, self.set_range_noise, 'noise', "counter_slider", float)
        self.top_layout.addWidget(self._range_noise_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.3", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(2e9, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.3", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        	"packet_len",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_center_freq(1.5e9, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self._range_rx_gain_range = Range(0, 60, 1, 10, 200)
        self._range_rx_gain_win = RangeWidget(self._range_rx_gain_range, self.set_range_rx_gain, 'Rx Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._range_rx_gain_win, 1,0,1,1)
        self._range_mu_range = Range(0, 1, 0.01, 0.6, 200)
        self._range_mu_win = RangeWidget(self._range_mu_range, self.set_range_mu, 'BB Derotation Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._range_mu_win, 2,0,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	100000, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-80, -20)
        
        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_3.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	256, #size
        	1, #samp_rate
        	"Frequency Offset", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 1, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	100000, #size
        	samp_rate, #samp_rate
        	"Correlation", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 200)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 20, 0, 1, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"TX Constellation", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "fd")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_const_sink_x_0_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Payload", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "fd")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.inets_rssi_1 = inets.rssi(0.0001, -78, 30000)
        self.inets_radio_0 = inets_radio(
            constellation=qam16_mod,
            matched_filter_coeff=rrc,
            mu=mu,
            preamble=diff_preamble_128,
            samp_rate=samp_rate,
            sps=sps,
            threshold=threshold,
        )
        self.inets_per_logger_0 = inets.per_logger()
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_SERVER", 'localhost', '52001', 10000, False)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 0)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((0, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((range_noise, ))
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 1024)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.inets_radio_0, 'in'))    
        self.msg_connect((self.inets_radio_0, 'out'), (self.inets_per_logger_0, 'payload_in'))    
        self.msg_connect((self.inets_radio_0, 'snr'), (self.inets_per_logger_0, 'snr_in'))    
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.inets_radio_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.inets_radio_0, 2), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.inets_radio_0, 1), (self.blocks_complex_to_mag_0_0, 0))    
        self.connect((self.inets_radio_0, 5), (self.blocks_null_sink_0, 0))    
        self.connect((self.inets_radio_0, 3), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.inets_radio_0, 6), (self.qtgui_const_sink_x_0_0_0, 0))    
        self.connect((self.inets_radio_0, 4), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.inets_radio_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.inets_rssi_1, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.inets_rssi_1, 1), (self.blocks_null_sink_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_add_xx_0, 0))    
        #self.connect((self.blocks_add_xx_0, 0), (self.inets_rssi_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.inets_rssi_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "radio_test_client")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.inets_radio_0.set_sps(self.sps)

    def get_range_rx_gain(self):
        return self.range_rx_gain

    def set_range_rx_gain(self, range_rx_gain):
        self.range_rx_gain = range_rx_gain
        self.set_rx_gain(self.range_rx_gain)

    def get_range_mu(self):
        return self.range_mu

    def set_range_mu(self, range_mu):
        self.range_mu = range_mu
        self.set_mu(self.range_mu)

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.inets_radio_0.set_threshold(self.threshold)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.inets_radio_0.set_samp_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	

    def get_rrc(self):
        return self.rrc

    def set_rrc(self, rrc):
        self.rrc = rrc
        self.inets_radio_0.set_matched_filter_coeff(self.rrc)

    def get_range_noise(self):
        return self.range_noise

    def set_range_noise(self, range_noise):
        self.range_noise = range_noise
        self.blocks_multiply_const_vxx_0.set_k((self.range_noise, ))

    def get_qpsk_mod(self):
        return self.qpsk_mod

    def set_qpsk_mod(self, qpsk_mod):
        self.qpsk_mod = qpsk_mod

    def get_qam16_mod(self):
        return self.qam16_mod

    def set_qam16_mod(self, qam16_mod):
        self.qam16_mod = qam16_mod
        self.inets_radio_0.set_constellation(self.qam16_mod)

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_mu(self):
        return self.mu

    def set_mu(self, mu):
        self.mu = mu
        self.inets_radio_0.set_mu(self.mu)

    def get_diff_preamble_256(self):
        return self.diff_preamble_256

    def set_diff_preamble_256(self, diff_preamble_256):
        self.diff_preamble_256 = diff_preamble_256

    def get_diff_preamble_128(self):
        return self.diff_preamble_128

    def set_diff_preamble_128(self, diff_preamble_128):
        self.diff_preamble_128 = diff_preamble_128
        self.inets_radio_0.set_preamble(self.diff_preamble_128)

    def get_bpsk_mod(self):
        return self.bpsk_mod

    def set_bpsk_mod(self, bpsk_mod):
        self.bpsk_mod = bpsk_mod

    def get_pow_data(self):
        return self.inets_rssi_1.get_pow_data()

    def get_pow(self):
        return self.inets_rssi_1.get_pow()

class per_test_avp:
    def __init__(self, block):
        self.doWork = True
        self.tb = block
	self.timestamp = int(time.time())
	self.count = 0

        # ---X--- #
        self.csv_fields_stats_X = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_X = '/home/inets/Documents/Log/RSSI_avp_X.csv'

        with open(self.stats_log_file_name_X,'w+') as log_file_X:
            csv_writer = csv.DictWriter(log_file_X, fieldnames=self.csv_fields_stats_X)
            csv_writer.writeheader()

	#####1#####

        # --- A--- #
        self.csv_fields_stats_A = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_A = '/home/inets/Documents/Log/RSSI_avp_A.csv'

        with open(self.stats_log_file_name_A,'w+') as log_file_A:
            csv_writer = csv.DictWriter(log_file_A, fieldnames=self.csv_fields_stats_A)
            csv_writer.writeheader()

        # ---AB--- #
        self.csv_fields_stats_AB = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_AB = '/home/inets/Documents/Log/RSSI_avp_AB.csv'

        with open(self.stats_log_file_name_AB,'w+') as log_file_AB:
            csv_writer = csv.DictWriter(log_file_AB, fieldnames=self.csv_fields_stats_AB)
            csv_writer.writeheader()

        # --- B--- #
        self.csv_fields_stats_B = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_B = '/home/inets/Documents/Log/RSSI_avp_B.csv'

        with open(self.stats_log_file_name_B,'w+') as log_file_B:
            csv_writer = csv.DictWriter(log_file_B, fieldnames=self.csv_fields_stats_B)
            csv_writer.writeheader()

        # ---BC--- #
        self.csv_fields_stats_BC = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_BC = '/home/inets/Documents/Log/RSSI_avp_BC.csv'

        with open(self.stats_log_file_name_BC,'w+') as log_file_BC:
            csv_writer = csv.DictWriter(log_file_BC, fieldnames=self.csv_fields_stats_BC)
            csv_writer.writeheader()

        # --- C--- #
        self.csv_fields_stats_C = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_C = '/home/inets/Documents/Log/RSSI_avp_C.csv'

        with open(self.stats_log_file_name_C,'w+') as log_file_C:
            csv_writer = csv.DictWriter(log_file_C, fieldnames=self.csv_fields_stats_C)
            csv_writer.writeheader()

	#####2#####

        # ---AD--- #
        self.csv_fields_stats_AD = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_AD = '/home/inets/Documents/Log/RSSI_avp_AD.csv'

        with open(self.stats_log_file_name_AD,'w+') as log_file_AD:
            csv_writer = csv.DictWriter(log_file_AD, fieldnames=self.csv_fields_stats_AD)
            csv_writer.writeheader()

        # ---AE--- #
        self.csv_fields_stats_AE = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_AE = '/home/inets/Documents/Log/RSSI_avp_AE.csv'

        with open(self.stats_log_file_name_AE,'w+') as log_file_AE:
            csv_writer = csv.DictWriter(log_file_AE, fieldnames=self.csv_fields_stats_AE)
            csv_writer.writeheader()

        # ---BE--- #
        self.csv_fields_stats_BE = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_BE = '/home/inets/Documents/Log/RSSI_avp_BE.csv'

        with open(self.stats_log_file_name_BE,'w+') as log_file_BE:
            csv_writer = csv.DictWriter(log_file_BE, fieldnames=self.csv_fields_stats_BE)
            csv_writer.writeheader()

        # ---BF--- #
        self.csv_fields_stats_BF = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_BF = '/home/inets/Documents/Log/RSSI_avp_BF.csv'

        with open(self.stats_log_file_name_BF,'w+') as log_file_BF:
            csv_writer = csv.DictWriter(log_file_BF, fieldnames=self.csv_fields_stats_BF)
            csv_writer.writeheader()

        # ---CF--- #
        self.csv_fields_stats_CF = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_CF = '/home/inets/Documents/Log/RSSI_avp_CF.csv'

        with open(self.stats_log_file_name_CF,'w+') as log_file_CF:
            csv_writer = csv.DictWriter(log_file_CF, fieldnames=self.csv_fields_stats_CF)
            csv_writer.writeheader()

	#####3#####

        # --- D--- #
        self.csv_fields_stats_D = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_D = '/home/inets/Documents/Log/RSSI_avp_D.csv'

        with open(self.stats_log_file_name_D,'w+') as log_file_D:
            csv_writer = csv.DictWriter(log_file_D, fieldnames=self.csv_fields_stats_D)
            csv_writer.writeheader()

        # ---DE--- #
        self.csv_fields_stats_DE = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_DE = '/home/inets/Documents/Log/RSSI_avp_DE.csv'

        with open(self.stats_log_file_name_DE,'w+') as log_file_DE:
            csv_writer = csv.DictWriter(log_file_DE, fieldnames=self.csv_fields_stats_DE)
            csv_writer.writeheader()

        # --- E--- #
        self.csv_fields_stats_E = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_E = '/home/inets/Documents/Log/RSSI_avp_E.csv'

        with open(self.stats_log_file_name_E,'w+') as log_file_E:
            csv_writer = csv.DictWriter(log_file_E, fieldnames=self.csv_fields_stats_E)
            csv_writer.writeheader()

        # ---EF--- #
        self.csv_fields_stats_EF = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_EF = '/home/inets/Documents/Log/RSSI_avp_EF.csv'

        with open(self.stats_log_file_name_EF,'w+') as log_file_EF:
            csv_writer = csv.DictWriter(log_file_EF, fieldnames=self.csv_fields_stats_EF)
            csv_writer.writeheader()

        # --- F--- #
        self.csv_fields_stats_F = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_F = '/home/inets/Documents/Log/RSSI_avp_F.csv'

        with open(self.stats_log_file_name_F,'w+') as log_file_F:
            csv_writer = csv.DictWriter(log_file_F, fieldnames=self.csv_fields_stats_F)
            csv_writer.writeheader()

	#####4#####

        # ---DG--- #
        self.csv_fields_stats_DG = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_DG = '/home/inets/Documents/Log/RSSI_avp_DG.csv'

        with open(self.stats_log_file_name_DG,'w+') as log_file_DG:
            csv_writer = csv.DictWriter(log_file_DG, fieldnames=self.csv_fields_stats_DG)
            csv_writer.writeheader()

        # ---DH--- #
        self.csv_fields_stats_DH = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_DH = '/home/inets/Documents/Log/RSSI_avp_DH.csv'

        with open(self.stats_log_file_name_DH,'w+') as log_file_DH:
            csv_writer = csv.DictWriter(log_file_DH, fieldnames=self.csv_fields_stats_DH)
            csv_writer.writeheader()

        # ---EH--- #
        self.csv_fields_stats_EH = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_EH = '/home/inets/Documents/Log/RSSI_avp_EH.csv'

        with open(self.stats_log_file_name_EH,'w+') as log_file_EH:
            csv_writer = csv.DictWriter(log_file_EH, fieldnames=self.csv_fields_stats_EH)
            csv_writer.writeheader()

        # ---EI--- #
        self.csv_fields_stats_EI = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_EI = '/home/inets/Documents/Log/RSSI_avp_EI.csv'

        with open(self.stats_log_file_name_EI,'w+') as log_file_EI:
            csv_writer = csv.DictWriter(log_file_EI, fieldnames=self.csv_fields_stats_EI)
            csv_writer.writeheader()

        # ---FI--- #
        self.csv_fields_stats_FI = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_FI = '/home/inets/Documents/Log/RSSI_avp_FI.csv'

        with open(self.stats_log_file_name_FI,'w+') as log_file_FI:
            csv_writer = csv.DictWriter(log_file_FI, fieldnames=self.csv_fields_stats_FI)
            csv_writer.writeheader()

	#####5#####

        # --- G--- #
        self.csv_fields_stats_G = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_G = '/home/inets/Documents/Log/RSSI_avp_G.csv'

        with open(self.stats_log_file_name_G,'w+') as log_file_G:
            csv_writer = csv.DictWriter(log_file_G, fieldnames=self.csv_fields_stats_G)
            csv_writer.writeheader()

        # ---GH--- #
        self.csv_fields_stats_GH = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_GH = '/home/inets/Documents/Log/RSSI_avp_GH.csv'

        with open(self.stats_log_file_name_GH,'w+') as log_file_GH:
            csv_writer = csv.DictWriter(log_file_GH, fieldnames=self.csv_fields_stats_GH)
            csv_writer.writeheader()

        # --- H--- #
        self.csv_fields_stats_H = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_H = '/home/inets/Documents/Log/RSSI_avp_H.csv'

        with open(self.stats_log_file_name_H,'w+') as log_file_H:
            csv_writer = csv.DictWriter(log_file_H, fieldnames=self.csv_fields_stats_H)
            csv_writer.writeheader()

        # ---HI--- #
        self.csv_fields_stats_HI = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_HI = '/home/inets/Documents/Log/RSSI_avp_HI.csv'

        with open(self.stats_log_file_name_HI,'w+') as log_file_HI:
            csv_writer = csv.DictWriter(log_file_HI, fieldnames=self.csv_fields_stats_HI)
            csv_writer.writeheader()

        # --- I--- #
        self.csv_fields_stats_I = ['Number','Timestamp', 'Avg. RSSI']
        self.stats_log_file_name_I = '/home/inets/Documents/Log/RSSI_avp_I.csv'

        with open(self.stats_log_file_name_I,'w+') as log_file_I:
            csv_writer = csv.DictWriter(log_file_I, fieldnames=self.csv_fields_stats_I)
            csv_writer.writeheader()

    def run_per_test_avp(self):

	print("...")
	print("...")
	print("...")
	print("Move to A...")
	print("...")
	print("...")
	print("...")
	time.sleep(5)

        while self.doWork:
            time.sleep(1)
	    self.timestamp = int(time.time())
	    self.count = self.count + 1

	    print("Number   : " + str(self.count))
            print("Timestamp: " + str(self.timestamp))
	    print("Avg. RSSI: " + str(self.tb.get_pow()))

	    #####1#####

	    # --- A--- #
	    if (self.count >= 1 and self.count <= 10):
            	with open(self.stats_log_file_name_A, 'a') as log_file_A:
                	csv_writer = csv.DictWriter(log_file_A, fieldnames=self.csv_fields_stats_A)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 10:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to AB...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---AB--- #
	    if (self.count >= 11 and self.count <= 20):
            	with open(self.stats_log_file_name_AB, 'a') as log_file_AB:
                	csv_writer = csv.DictWriter(log_file_AB, fieldnames=self.csv_fields_stats_AB)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 20:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to B...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # --- B--- #
	    elif (self.count >= 21 and self.count <= 30):
            	with open(self.stats_log_file_name_B, 'a') as log_file_B:
                	csv_writer = csv.DictWriter(log_file_B, fieldnames=self.csv_fields_stats_B)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 30:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to BC...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---BC--- #
	    elif (self.count >= 31 and self.count <= 40):
            	with open(self.stats_log_file_name_BC, 'a') as log_file_BC:
                	csv_writer = csv.DictWriter(log_file_BC, fieldnames=self.csv_fields_stats_BC)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 40:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to C...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # --- C--- #
	    elif (self.count >= 41 and self.count <= 50):
            	with open(self.stats_log_file_name_C, 'a') as log_file_C:
                	csv_writer = csv.DictWriter(log_file_C, fieldnames=self.csv_fields_stats_C)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 50:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to AD...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    #####2#####

	    # ---AD--- #
	    if (self.count >= 51 and self.count <= 60):
            	with open(self.stats_log_file_name_AD, 'a') as log_file_AD:
                	csv_writer = csv.DictWriter(log_file_AD, fieldnames=self.csv_fields_stats_AD)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 60:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to AE...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---AE--- #
	    if (self.count >= 61 and self.count <= 70):
            	with open(self.stats_log_file_name_AE, 'a') as log_file_AE:
                	csv_writer = csv.DictWriter(log_file_AE, fieldnames=self.csv_fields_stats_AE)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 70:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to BE...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---BE--- #
	    if (self.count >= 71 and self.count <= 80):
            	with open(self.stats_log_file_name_BE, 'a') as log_file_BE:
                	csv_writer = csv.DictWriter(log_file_BE, fieldnames=self.csv_fields_stats_BE)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 80:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to BF...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---BF--- #
	    if (self.count >= 81 and self.count <= 90):
            	with open(self.stats_log_file_name_BF, 'a') as log_file_BF:
                	csv_writer = csv.DictWriter(log_file_BF, fieldnames=self.csv_fields_stats_BF)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 90:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to CF...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---CF--- #
	    if (self.count >= 91 and self.count <= 100):
            	with open(self.stats_log_file_name_CF, 'a') as log_file_CF:
                	csv_writer = csv.DictWriter(log_file_CF, fieldnames=self.csv_fields_stats_CF)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 100:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to D...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    #####3#####

	    # --- D--- #
	    if (self.count >= 101 and self.count <= 110):
            	with open(self.stats_log_file_name_D, 'a') as log_file_D:
                	csv_writer = csv.DictWriter(log_file_D, fieldnames=self.csv_fields_stats_D)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 110:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to DE...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---DE--- #
	    if (self.count >= 111 and self.count <= 120):
            	with open(self.stats_log_file_name_DE, 'a') as log_file_DE:
                	csv_writer = csv.DictWriter(log_file_DE, fieldnames=self.csv_fields_stats_DE)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 120:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to E...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # --- E--- #
	    if (self.count >= 121 and self.count <= 130):
            	with open(self.stats_log_file_name_E, 'a') as log_file_E:
                	csv_writer = csv.DictWriter(log_file_E, fieldnames=self.csv_fields_stats_E)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 130:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to EF...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---EF--- #
	    if (self.count >= 131 and self.count <= 140):
            	with open(self.stats_log_file_name_EF, 'a') as log_file_EF:
                	csv_writer = csv.DictWriter(log_file_EF, fieldnames=self.csv_fields_stats_EF)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 140:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to F...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---F--- #
	    if (self.count >= 141 and self.count <= 150):
            	with open(self.stats_log_file_name_F, 'a') as log_file_F:
                	csv_writer = csv.DictWriter(log_file_F, fieldnames=self.csv_fields_stats_F)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 150:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to DG...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    #####4#####

	    # ---DG--- #
	    if (self.count >= 151 and self.count <= 160):
            	with open(self.stats_log_file_name_DG, 'a') as log_file_DG:
                	csv_writer = csv.DictWriter(log_file_DG, fieldnames=self.csv_fields_stats_DG)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 160:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to DH...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---DH--- #
	    if (self.count >= 161 and self.count <= 170):
            	with open(self.stats_log_file_name_DH, 'a') as log_file_DH:
                	csv_writer = csv.DictWriter(log_file_DH, fieldnames=self.csv_fields_stats_DH)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 170:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to EH...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---EH--- #
	    if (self.count >= 171 and self.count <= 180):
            	with open(self.stats_log_file_name_EH, 'a') as log_file_EH:
                	csv_writer = csv.DictWriter(log_file_EH, fieldnames=self.csv_fields_stats_EH)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 180:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to EI...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---EI--- #
	    if (self.count >= 181 and self.count <= 190):
            	with open(self.stats_log_file_name_EI, 'a') as log_file_EI:
                	csv_writer = csv.DictWriter(log_file_EI, fieldnames=self.csv_fields_stats_EI)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 190:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to FI...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---FI--- #
	    if (self.count >= 191 and self.count <= 200):
            	with open(self.stats_log_file_name_FI, 'a') as log_file_FI:
                	csv_writer = csv.DictWriter(log_file_FI, fieldnames=self.csv_fields_stats_FI)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 200:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to G...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    #####5#####

	    # --- G--- #
	    if (self.count >= 201 and self.count <= 210):
            	with open(self.stats_log_file_name_G, 'a') as log_file_G:
                	csv_writer = csv.DictWriter(log_file_G, fieldnames=self.csv_fields_stats_G)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 210:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to GH...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---GH--- #
	    if (self.count >= 211 and self.count <= 220):
            	with open(self.stats_log_file_name_GH, 'a') as log_file_GH:
                	csv_writer = csv.DictWriter(log_file_GH, fieldnames=self.csv_fields_stats_GH)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 220:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to H...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # --- H--- #
	    if (self.count >= 221 and self.count <= 230):
            	with open(self.stats_log_file_name_H, 'a') as log_file_H:
                	csv_writer = csv.DictWriter(log_file_H, fieldnames=self.csv_fields_stats_H)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 230:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to HI...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # ---HI--- #
	    if (self.count >= 231 and self.count <= 240):
            	with open(self.stats_log_file_name_HI, 'a') as log_file_HI:
                	csv_writer = csv.DictWriter(log_file_HI, fieldnames=self.csv_fields_stats_HI)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 240:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("Move to I...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    # --- I--- #
	    if (self.count >= 241 and self.count <= 250):
            	with open(self.stats_log_file_name_I, 'a') as log_file_I:
                	csv_writer = csv.DictWriter(log_file_I, fieldnames=self.csv_fields_stats_I)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})
		if  self.count == 250:
	    		print("...")
	    		print("...")
	    		print("...")
	    		print("E N D ...")
	    		print("...")
	    		print("...")
	    		print("...")
			time.sleep(5)

	    #####X#####

	    # ---X--- #
	    else:
            	with open(self.stats_log_file_name_X, 'a') as log_file_X:
                	csv_writer = csv.DictWriter(log_file_X, fieldnames=self.csv_fields_stats_X)
                	csv_writer.writerow({'Number' : self.count,
				'Timestamp' : self.timestamp,
			'Avg. RSSI' : self.tb.get_pow_data()})


def main(top_block_cls=radio_test_client, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    my_per_test_avp = per_test_avp(tb)
    per_thread = threading.Thread(target=my_per_test_avp.run_per_test_avp)
    per_thread.start()
    tb.show()

    def quitting():
        my_per_test_avp.doWork = False
        per_thread.join()
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()