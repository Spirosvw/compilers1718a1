
def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """
	if pos < 0 or pos >= len(text):
        	return None
    	elif (text[pos]>='0' and text[pos]<='1'):
	        return 'zero_one'
   	elif text[pos]=='2':
       		return 'two'
    	elif text[pos]=='3':
        	return 'three'
    	elif (text[pos]=='4' or text[pos]=='5'):
        	return 'four_five'
    	elif (text[pos]==':' or text[pos]=='.'):
        	return 'dot_time'
    	elif (text[pos]>='6' and text[pos]<='9'):
        	return 'six_nine'
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

td =    {
        "q0": {"zero_one":"q1","two":"q2","three":"q3","four_five":"q3","six_nine":"q3"},
        "q1":{"zero_one":"q3","two":"q3","three":"q3","four_five":"q3","six_nine":"q3","dot_time":"q4"},
        "q2": {"zero_one":"q3","two":"q3","three":"q3","dot_time":"q4"},
        "q3":{"dot_time":"q4"},
        "q4":{"zero_one":"q5","two":"q5","three":"q5","four_five":"q5"},
        "q5":{"zero_one":"q6","two":"q6","three":"q6","four_five":"q6","six_nine":"q6"}

} # transition di
ad = {
        "q6": "TIME_TOKEN"
}


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
	
