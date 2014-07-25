# state = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'PALAU', 'Pennsylvania', 'PUERTO RICO', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
# state_abbr = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

with open("states.csv", "r") as states_file:
	states = states_file.read().split("\n")

	for index, state in enumerate(states):
		states[index] = state.split(",")

		with open("states.html", "w") as states_file:
			states_file.write('<select name="states">')
		
			for state in states:
				states_file.write('\n \t<option value="{0}">{1}</option>'.format(state[0],state[1]))
		
			states_file.write('\n </select>')

		
			
#this is the HTML
		
# <select name="states">
# 	<option value="AL">Alabama</option>
# 	<option value="AK">Alaska</option>
# 	<option value="AZ">Arizona</option>
# 	<option value="AR">Arkansas</option>
# 	<option value="CA">California</option>
# 	<option value="CO">Colorado</option>
# 	<option value="CT">Connecticut</option>
# 	<option value="DE">Delaware</option>
# 	<option value="DC">District Of Columbia</option>
# 	<option value="FL">Florida</option>
# 	<option value="GA">Georgia</option>
# 	<option value="HI">Hawaii</option>
# 	<option value="ID">Idaho</option>
# 	<option value="IL">Illinois</option>
# 	<option value="IN">Indiana</option>
# 	<option value="IA">Iowa</option>
# 	<option value="KS">Kansas</option>
# 	<option value="KY">Kentucky</option>
# 	<option value="LA">Louisiana</option>
# 	<option value="ME">Maine</option>
# 	<option value="MD">Maryland</option>
# 	<option value="MA">Massachusetts</option>
# 	<option value="MI">Michigan</option>
# 	<option value="MN">Minnesota</option>
# 	<option value="MS">Mississippi</option>
# 	<option value="MO">Missouri</option>
# 	<option value="MT">Montana</option>
# 	<option value="NE">Nebraska</option>
# 	<option value="NV">Nevada</option>
# 	<option value="NH">New Hampshire</option>
# 	<option value="NJ">New Jersey</option>
# 	<option value="NM">New Mexico</option>
# 	<option value="NY">New York</option>
# 	<option value="NC">North Carolina</option>
# 	<option value="ND">North Dakota</option>
# 	<option value="OH">Ohio</option>
# 	<option value="OK">Oklahoma</option>
# 	<option value="OR">Oregon</option>
# 	<option value="PW">PALAU</option>
# 	<option value="PA">Pennsylvania</option>
# 	<option value="PR">PUERTO RICO</option>
# 	<option value="RI">Rhode Island</option>
# 	<option value="SC">South Carolina</option>
# 	<option value="SD">South Dakota</option>
# 	<option value="TN">Tennessee</option>
# 	<option value="TX">Texas</option>
# 	<option value="UT">Utah</option>
# 	<option value="VT">Vermont</option>
# 	<option value="VA">Virginia</option>
# 	<option value="WA">Washington</option>
# 	<option value="WV">West Virginia</option>
# 	<option value="WI">Wisconsin</option>
# 	<option value="WY">Wyoming</option>
# </select>
