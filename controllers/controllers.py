# -*- coding: utf-8 -*-
from odoo import http
import json

class Jthsalesplugg(http.Controller):
	@http.route('/test/test', auth='public')
	def test(self, **kwargs):
		#jsval = json.dumps({"1": ['Elem1','Elem2','Elem3','Elem4','Elem5'], "2": ['Elem21','Elem22','Elem23','Elem24','Elem25']})
	    #return jsval
	    jsv = json.dumps({'0':['val1','val2','val3'],'1':['val1','val2','val3','val4','val5']})
	    return jsv
    	#print "no implemente - dead code"