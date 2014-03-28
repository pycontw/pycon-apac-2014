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
      '30': [u'勁成 駱',         'zh', u'立委投票指南 -- 從零開始'],
      '71': [u'Song Kai',       'en', u'HiPy - Python for High School Students'],
      '88': [u'Wisely Chen',    'en', u'PySpark: next generation cluster computing engine'],
      '25': [u'Bithin Alangot', 'en', u'Python bindings for RAMCloud'],
      '7' : [u'Wei-Ting Kuo',   'en', u'Data Analysis in Python'],
      '55': [u'信屹 陳',         'zh', u'Python to LiveScript'],
      '87': [u'Kushal Das',     'en', u'Teaching Python: To infinity and beyond'],
      '93': [u'Yung-Yu Chen',   'en', u'SOLVCON: Software-Engineering Simulations of Conservation Laws'],
      '29': [u'學聰 郭',         'en', u'VapourSynth comes, does it indicate that AviSynth will shutdown?'],
      '78': [u'Ken Hu',         'en', u'Text Analytics for Human: TextBlob'],
      '81': [u'Mosky Liu',      'zh', u'Graph-Tool: The Efficient Network Aanalyzing Tool for Python'],
      '51': [u'Ambrose Tan',    'en', u'from present import future.curriculum'],
      '35': [u'Liang Bo Wang',  'en', u'Statistics in Python with R'],
      '6' : [u'Wei-Ting Kuo',   'en', u'Shipping python projects by Docker'],
      '96':  [ u'宗哲 李'            , 'zh',  u'graph database for python'],
      '102': [ u'Yuli Zhan'         , 'en',  u'Time for Education: Data Mining in High School'],
      '74':  [ u'Wen-Wei Liao'      , 'en',  u'DMRL: A versatile Python tool to quantify DNA methylation difference and identify DMRs'],
      '53':  [ u'A. Jesse Jiryu Da' , 'en',  u'What Is Async, How Does It Work, and When Should I Use It?'],
      '66':  [ u'總理 海'            , 'zh',  u'小海嚴選'],
      '60':  [ u'Shih-Ching Yang'   , 'zh',  u'OpenOffice Application with Python  教育座談'],
      '91':  [ u'Nikit Saraf'       , 'en',  u'Data Matching and Big Data Deduping in Python'],
      '27':  [ u'Sonya Green'       , 'en',  u'Supporting continuous deployment with aplomb'],
      '64':  [ u'嘉駿 戴'            , 'zh',  u'Python in VIM'],
      '58':  [ u'Tzu-ping Chung'    , 'zh',  u'Yielding a Tulip'],
      '77':  [ u'Michael McKerns'   , 'en',  u'optimization and uncertainty quantification at exascale'],
      '73':  [ u'Muyueh Lee'        , 'en',  u'Real-time visualization with Python and d3.js'],
      '69':  [ u'國棟 高'            , 'zh',  u'Openstack 簡介'],
    }

    data = {
      'programs': programs
    }



    return render(request, 'demo/program.html', data)
