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
      '30': ['勁成 駱',         'zh', '立委投票指南 -- 從零開始'],
      '71': ['Song Kai',       'en', 'HiPy - Python for High School Students'],
      '88': ['Wisely Chen',    'en', 'PySpark: next generation cluster computing engine'],
      '25': ['Bithin Alangot', 'en', 'Python bindings for RAMCloud'],
      '7' : ['Wei-Ting Kuo',   'en', 'Data Analysis in Python'],
      '55': ['信屹 陳',         'zh', 'Python to LiveScript'],
      '87': ['Kushal Das',     'en', 'Teaching Python: To infinity and beyond'],
      '93': ['Yung-Yu Chen',   'en', 'SOLVCON: Software-Engineering Simulations of Conservation Laws'],
      '29': ['學聰 郭',         'en', 'VapourSynth comes, does it indicate that AviSynth will shutdown?'],
      '78': ['Ken Hu',         'en', 'Text Analytics for Human: TextBlob'],
      '81': ['Mosky Liu',      'zh', 'Graph-Tool: The Efficient Network Aanalyzing Tool for Python'],
      '51': ['Ambrose Tan',    'en', 'from present import future.curriculum'],
      '35': ['Liang Bo Wang',  'en', 'Statistics in Python with R'],
      '6' : ['Wei-Ting Kuo',   'en', 'Shipping python projects by Docker'],
      '96':  [ '宗哲 李'            , 'zh',  'graph database for python'],
      '102': [ 'Yuli Zhan'         , 'en',  'Time for Education: Data Mining in High School'],
      '74':  [ 'Wen-Wei Liao'      , 'en',  'DMRL: A versatile Python tool to quantify DNA methylation difference and identify DMRs'],
      '53':  [ 'A. Jesse Jiryu Da' , 'en',  'What Is Async, How Does It Work, and When Should I Use It?'],
      '66':  [ '總理 海'            , 'zh',  '小海嚴選'],
      '60':  [ 'Shih-Ching Yang'   , 'zh',  'OpenOffice Application with Python  教育座談'],
      '91':  [ 'Nikit Saraf'       , 'en',  'Data Matching and Big Data Deduping in Python'],
      '27':  [ 'Sonya Green'       , 'en',  'Supporting continuous deployment with aplomb'],
      '64':  [ '嘉駿 戴'            , 'zh',  'Python in VIM'],
      '58':  [ 'Tzu-ping Chung'    , 'zh',  'Yielding a Tulip'],
      '77':  [ 'Michael McKerns'   , 'en',  'optimization and uncertainty quantification at exascale'],
      '73':  [ 'Muyueh Lee'        , 'en',  'Real-time visualization with Python and d3.js'],
      '69':  [ '國棟 高'            , 'zh',  'Openstack 簡介'],

      '65':  ['Chia-Chi Chang'     , 'en', 'Hacking Models with Python'],
    }

    programs[1] = {
      '97':  ['Andy Dai'        ,'zh',  '用 Python 建立你自己的 Summly' ],
      '99':  ['Colin Su'        ,'zh',  'Introduction to Google Cloud Endpoints for Python developers' ],
      '23':  ['Ekta Grover'     ,'en',  'Experiments in data mining, entity disambiguation & thinking data-structures fordesigning algorithm'],
      '67':  ['柏任 姜'          ,'en', 'Roboconf: How we held a conference with Django'],
      '70':  ['總理 海'          ,'zh', 'StreetVoice 改造後, 現在我們如何進行開發工作'  ],
      '28':  ['Chien Hsun Chen' ,'zh', 'Introduce Google Cloud Platform with BigData Lab'  ],
      '95':  ['Jimmy Lai'       ,'en', 'Building a Knowledge Graph - the new search engine technology'  ],
      '40':  ['Keith Yang'      ,'en', 'How PyCon APAC 2014 Web built'],
      '63':  ['Toomore Chiang'  ,'zh', '如何用 grs 擷取台灣上市股票股價資訊' ],
      '101': ['Colin Su'       ,'zh', 'Google Protocol Buffer - Smaller, Faster, Simpler XML' ],
      '31':  ['Jerry Chou'      ,'en', 'How to integrate Python into a Scala stack to build realtime predictive models' ],
      '75':  ['Amalia Hawkins'  ,'en', 'Narrowing the Gender Gap at Hackathons'],

      '45':  ['Renyuan Lyu',          'zh', 'A Real-time Audio Spectrogram with Application to Sound-Driven Games in Python 3, Pygame and Pyaudio'],
      '86':  ['Kushal Das',           'en', 'Discovering distributed task queue in its simplest form using Retask'],
      '54':  ['A. Jesse Jiryu Davis', 'en', 'Python Performance Profiling: The Guts And The Glory'],
      '61':  ['Carl Su',              'zh', 'Introduction to Robot Framework'],
      '41':  ['Keith Yang',           'zh', '迅速網站前端開發用 Python '],
      '36':  ['Liang Bo Wang',        'en', 'Handy Parallel (Distributed) Computing in Python '],
      '46':  ['祐瑋 丘',               'en', 'Social Network Analysis with Python   '],
      '44':  ['Tim Hsu',              'zh', '實戰 Django REST framework '],
      '84':  ['Cheng-Lung Sung',      'zh', 'Using Fabric and Docker for deployment testing  '],
      '37':  ['Jiwon Seo',            'en', 'Designing a Python-integrated query language for distributed computing '],
      '38':  ['zaki akhmad',          'en', 'Python for Application Security Testing  '],
      '26':  ['Sakshi Bansal',        'en', 'Python Request'],
      's0': ['Sponsored Talk by VPon', 'en', 'Item-Based Mobile Advertisement Recommendation System in Python with Hadoop Streaming']
    }

    data = {
      'programs': programs
    }



    return render(request, 'demo/program.html', data)
