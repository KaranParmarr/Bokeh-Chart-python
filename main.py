from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap, dodge
from bokeh.palettes import Blues7
from bokeh.embed import components
import pandas

# Read in csv
df = pandas.read_csv('bikes.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

output_file('index.html')

# Bike list
bike_list = source.data['Bike'].tolist()


# Add plot
p = figure(
    y_range=bike_list,
    width=800,
    height=600,
    title='Bikes with highest Cubic Capacity',
    x_axis_label='Cubic Capacity Engine Power',
    y_axis_label='Bike',
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph
p.hbar(
    y='Bike',
    right='CubicCapacity',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
      'Bike', 
      palette=Blues7,
      factors=bike_list
    ),
    fill_alpha=0.9,
    source=source,
)

p.vbar_stack(
    ["Bike", "Bike", "Bike", "Bike", "Bike", "Bike", "Bike"],
    x="Bike", 
    source=df, 
    fill_color=['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#eff3ff'],
    legend_label=["Harley-Davison Fat 114", "HayaBusa","Kawasaki-Ninja-H2R",
              "Ducati-superleggera-v4","BMW F 900R", "Triumph-Street","Suzuki V-Strom 650XT"]
)


# Add Legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '15px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@Bike</h3>
    <div><strong>Price: </strong>@Price</div>
    <div><strong>CC: </strong>@CubicCapacity <strong>Cubic Capacity</strong></div>
    <div><strong>Speed: </strong>@Km <strong>Km/Hr</strong></div>
    <div><img src="@Image" alt="" width="200" /></div>
  </div>
"""
p.add_tools(hover)

# Show results
show(p)

# Save file
save(p)

# Print out div and script
script, div = components(p)
print(div)
print(script)
