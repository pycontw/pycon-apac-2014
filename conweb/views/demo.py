# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def show(request, page='show'):

    data = {'page': page}

    if request.is_ajax():
        template = 'demo/' + page + '_content.html'
    else:
        template = 'demo/' + page + '.html'

    return render(request, template, data)


def program(request):
    programs = [0, 1]

    programs[0] = {
      '30': [27, '勁成 駱',         'zh', '立委投票指南 -- 從零開始'],
      '71': [61, 'Song Kai',       'en', 'HiPy - Python for High School Students'],
      '88': [37, 'Wisely Chen',    'en', 'PySpark: next generation cluster computing engine'],
      '25': [23, 'Bithin Alangot', 'en', 'Python bindings for RAMCloud'],
      '7' : [12, 'Wei-Ting Kuo',   'en', 'Data Analysis in Python'],
      '55': [53, '信屹 陳',         'zh', 'Python to LiveScript'],
      '87': [68, 'Kushal Das',     'en', 'Teaching Python: To infinity and beyond'],
      '93': [8,  'Yung-Yu Chen',   'en', 'SOLVCON: Software-Engineering Simulations of Conservation Laws'],
      '29': [0, '學聰 郭',         'en', 'VapourSynth comes, does it indicate that AviSynth will shutdown?'],
      '78': [45, 'Ken Hu',         'en', 'Text Analytics for Human: TextBlob'],
      '81': [67, 'Mosky Liu',      'zh', 'Graph-Tool: The Efficient Network Aanalyzing Tool for Python'],
      '51': [47, 'Ambrose Tan',    'en', 'from present import future.curriculum'],
      '35': [19, 'Liang Bo Wang',  'en', 'Statistics in Python with R'],
      '6' : [12, 'Wei-Ting Kuo',   'en', 'Shipping python projects by Docker'],
      '96': [83, '宗哲 李'            , 'zh',  'graph database for python'],
      '102': [82, 'Yuli Zhan'         , 'en',  'Time for Education: Data Mining in High School'],
      '74': [63, 'Wen-Wei Liao'      , 'en',  'DMRL: A versatile Python tool to quantify DNA methylation difference and identify DMRs'],
      '53': [52, 'A. Jesse Jiryu Da' , 'en',  'What Is Async, How Does It Work, and When Should I Use It?'],
      '66': [60, '總理 海'            , 'zh',  '小海嚴選'],
      '60': [56, 'Shih-Ching Yang'   , 'zh',  'OpenOffice Application with Python  教育座談'],
      '91': [79, 'Nikit Saraf'       , 'en',  'Data Matching and Big Data Deduping in Python'],
      '27': [25, 'Sonya Green'       , 'en',  'Supporting continuous deployment with aplomb'],
      '64': [58, '嘉駿 戴'            , 'zh',  'Python in VIM'],
      '58': [46, 'Tzu-ping Chung'    , 'zh',  'Yielding a Tulip'],
      '77': [64, 'Michael McKerns'   , 'en',  'optimization and uncertainty quantification at exascale'],
      '73':  [62, 'Muyueh Lee'        , 'en',  'Real-time visualization with Python and d3.js'],
      '69':  [0, '國棟 高'            , 'zh',  'Openstack 簡介'],

      '65':  [11, 'Chia-Chi Chang'     , 'en', 'Hacking Models with Python'],
    }

    programs[1] = {
      '97':  [0, 'Andy Dai'        ,'zh',  '用 Python 建立你自己的 Summly' ],
      '99':  [38, 'Colin Su'        ,'zh',  'Introduction to Google Cloud Endpoints for Python developers' ],
      '23':  [21, 'Ekta Grover'     ,'en',  'Experiments in data mining, entity disambiguation & thinking data-structures fordesigning algorithm'],
      '67':  [0, '柏任 姜'          ,'en', 'Roboconf: How we held a conference with Django'],
      '70':  [60, '總理 海'          ,'zh', 'StreetVoice 改造後, 現在我們如何進行開發工作'  ],
      '28':  [18, 'Chien Hsun Chen' ,'zh', 'Introduce Google Cloud Platform with BigData Lab'  ],
      '95':  [66, 'Jimmy Lai'       ,'en', 'Building a Knowledge Graph - the new search engine technology'  ],
      '40':  [6, 'Keith Yang'      ,'en', 'How PyCon APAC 2014 Web built'],
      '63':  [55, 'Toomore Chiang'  ,'zh', '如何用 grs 擷取台灣上市股票股價資訊' ],
      '101': [38, 'Colin Su'       ,'zh', 'Google Protocol Buffer - Smaller, Faster, Simpler XML' ],
      '31':  [35, 'Jerry Chou'      ,'en', 'How to integrate Python into a Scala stack to build realtime predictive models' ],
      '75':  [51, 'Amalia Hawkins'  ,'en', 'Narrowing the Gender Gap at Hackathons'],

      '45':  [40, 'Renyuan Lyu',          'zh', 'A Real-time Audio Spectrogram with Application to Sound-Driven Games in Python 3, Pygame and Pyaudio'],
      '86':  [68, 'Kushal Das',           'en', 'Discovering distributed task queue in its simplest form using Retask'],
      '54':  [52, 'A. Jesse Jiryu Davis', 'en', 'Python Performance Profiling: The Guts And The Glory'],
      '61':  [57, 'Carl Su',              'zh', 'Introduction to Robot Framework'],
      '41':  [6, 'Keith Yang',           'zh', '迅速網站前端開發用 Python '],
      '36':  [19, 'Liang Bo Wang',        'en', 'Handy Parallel (Distributed) Computing in Python '],
      '46':  [43, '祐瑋 丘',               'en', 'Social Network Analysis with Python   '],
      '44':  [10, 'Tim Hsu',              'zh', '實戰 Django REST framework '],
      '84':  [50, 'Cheng-Lung Sung',      'zh', 'Using Fabric and Docker for deployment testing  '],
      '37':  [7, 'Jiwon Seo',            'en', 'Designing a Python-integrated query language for distributed computing '],
      '38':  [28, 'zaki akhmad',          'en', 'Python for Application Security Testing  '],
      '26':  [0, 'Sakshi Bansal',        'en', 'Python Request'],
      's0': [0, 'Sponsored Talk by VPon', 'en', 'Item-Based Mobile Advertisement Recommendation System in Python with Hadoop Streaming']
    }

    data = {
      'programs': programs
    }



    return render(request, 'demo/program.html', data)
