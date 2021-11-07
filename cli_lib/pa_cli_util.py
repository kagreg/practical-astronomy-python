import json

def display_error(error_description):
	'''
	Return error details for a failed call.
	'''
	error_dict = dict(errorDescription=error_description)

	print(json.dumps(error_dict))
