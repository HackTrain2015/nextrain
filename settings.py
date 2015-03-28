DOMAIN = {'trains': {}}

schema = {
	'platform': {
		'type': 'string',
		'minlength': 1,
		'maxlength': 3,
	},
	'destination' : {
		'type': 'string',
		'minlength': 3,
		'maxlength': 35,
	},
	'schedule' : {
		'type': 'datetime'
	},
	'due': {
		'type':'string'
	},
	'operator': {
		'type' : 'string',
		'minlength': 4,
		'maxlength': 35
	}

	


}