#!/usr/bin/env python

from __future__ import print_function
from __future__ import division


if SCRATCH:

	def assign_defauts0(
	    Dic,
	    Required_arguments_dic_or_list={},
	    Default_values={},
	):
		"""
		e.g.,
	        assign_defauts(
	            Dic=D,
	            Required_arguments={
	                'dir' : (str,int)
	            },
	            Default_values={
	                'path' : opjh('Desktops_older')
	            },
	        )
		"""
		R = Required_arguments_dic_or_list
		
        for k in R:
            if k not Dic:
                assert(False)
            if type(R) == dic:
	            assert type(Dic[k]) in R[k]

	    for k in Default_values:
            if k not in Dic:
                Dic[l] = Default_values[k]
	                


#EOF
