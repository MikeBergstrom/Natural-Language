# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from pos import *
data = pos()

import nltk

def index(request):
    print "at index"
    return render(request, 'natlanguage/index.html')

def evaluate(request):
    if request.method == "POST":
        print "its a post"
        print "at evaluate"
        sentence = request.POST['sentence']
        words = nltk.word_tokenize(sentence)
        request.session['tagged'] = nltk.pos_tag(words)
        print words
        print data['CC']
        print request.session['tagged']
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    result = []
    for i in request.session['tagged']:
        print i[1]
        i[1] = data[i[1]]
    print request.session['tagged']
    return render(request, 'natlanguage/results.html')
# Create your views here.
