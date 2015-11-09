#!/usr/bin/env python
# coding: utf-8

import random
r = 0;
pos = 0;
q = 0;
alpha = 0.01;
gamma = 0.9;
max_q = 0;

def environment(a):
	global pos,r;
	#road = {0,1,2,3,4};
	if(a == "L"): pos = pos - 1;
	if(a == "R"): pos = pos + 1;
	if(pos < 0): pos = 0;
	if(pos == 4):
		r = 1
		pos = 0;
	print "position:" + str(pos)
	init(r,pos);
	# return r;


def init(r,pos):
	global q,alpha,gamma;
	Q = [[0]*2]*5;
	print "reward:" + str(r)
	if(r == 1):
		# print a
		#Q[pos][a] = alpha * r
		return
	randomNum = random.randint(0,1);
	if(randomNum == 0): a = "L";
	if(randomNum == 1): a = "R";
	print "action:" + str(a)
	# max_q = Q[pos+]
	q = q + alpha*(r+gamma*max_q-q);
	Q[pos][randomNum] = q;
	environment(a);

# def agent(r,pos):
# 	global q,alpha,gamma,Q;
# 	print "reward:" + str(r)
# 	if(r == 1):
# 		print Q
# 		return
# 	print "action:" + str(a)
# 	max_q = Q[pos+]
# 	q = q + alpha*(r+gamma*max_q-q);
# 	Q[pos][a] = q;
# 	environment(a);

if __name__ == "__main__":
	init(r,pos)
	# agent(r,pos)
