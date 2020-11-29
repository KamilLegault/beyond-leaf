from flask import render_template, flash, redirect, request, make_response, jsonify
from app import app,df
from werkzeug.utils import secure_filename
import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index-simple-ed.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    terpenes = ['cis-Nerolidol', 'trans-Nerolidol',
       'trans-Nerolidol 1', 'trans-Nerolidol 2', 'trans-Ocimene', '3-Carene',
       'Camphene', 'Caryophyllene Oxide', 'Eucalyptol', 'Geraniol', 'Guaiol',
       'Isopulegol', 'Linalool', 'Ocimene', 'Terpinolene', 'alpha-Bisabolol',
       'alpha-Humulene', 'alpha-Pinene', 'alpha-Terpinene',
       'beta-Caryophyllene', 'beta-Myrcene', 'beta-Ocimene', 'beta-Pinene',
       'delta-Limonene', 'gamma-Terpinene', 'p-Cymene']
       
    cannabinoids = ['delta-9 THC-A',
       'delta-9 THC', 'delta-8 THC', 'THC-A', 'THCV', 'CBN', 'CBD-A', 'CBD',
       'CBDV', 'CBDV-A', 'delta-9 CBG-A', 'delta-9 CBG', 'CBC',]
    terp_labels = list(df.sample(1)[terpenes].iloc[0].index)
    terp_values = list(df.sample(1)[terpenes].iloc[0].values)
    cann_labels = list(df.sample(1)[cannabinoids].iloc[0].index)
    cann_values = list(df.sample(1)[cannabinoids].iloc[0].values)
    strain = df.sample(1)['Sample Name'].iloc[0]
    import random
    r = lambda: random.randint(0,255)
    terp_colors = ['#%02X%02X%02X' % (r(),r(),r()) for _ in terp_labels]
    cann_colors = ['#%02X%02X%02X' % (r(),r(),r()) for _ in cann_labels]
    return render_template('services-ed.html',strain=strain,terp_values=terp_values,terp_labels=terp_labels,terp_colors=terp_colors,cann_values=cann_values,cann_labels=cann_labels,cann_colors=cann_colors)