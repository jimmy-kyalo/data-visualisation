import json
from pygal.maps.world import World
from country_codes import get_country_code
from pygal.style import RotateStyle

# load the data into a list
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

# build a dictionary of world data
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population

# group countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

# see how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0 - 10m', cc_pops_1)
wm.add('10m - 1b', cc_pops_2)
wm.add(' > 1b', cc_pops_3)

wm.render_to_file('world_population.svg')

"""
		Lightening the Color Theme
Pygal tends to use dark themes by default. For the purposes of printing, I’ve
lightened the style of my charts using LightColorizedStyle . This class changes
the overall theme of the chart, including the background and labels as well
as the individual country colors. To use it, first import the style:
			from pygal.style import LightColorizedStyle
You can then use LightColorizedStyle on its own, as such:
			wm_style = LightColorizedStyle
But this class gives you no direct control over the color used, so Pygal
will choose a default base color. To set a color, use LightColorizedStyle as a
base for RotateStyle . Import both LightColorizedStyle and RotateStyle :
			from pygal.style import LightColorizedStyle, RotateStyle
Then create a style using RotateStyle , but pass it an additional base_style
argument:
			wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
This gives you a light overall theme but bases the country colors on the
color you pass as an argument. With this style you’ll see that your charts
match the screenshots here a bit more closely.
While you’re experimenting to find styling directives that work
well for different visualizations, it can help to use aliases in your import
statements:
			from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
This will result in shorter style definitions:
			wm_style = RS('#336699', base_style=LCS)
Using just this small set of styling directives gives you significant control
over the appearance of charts and maps in Pygal.
"""	