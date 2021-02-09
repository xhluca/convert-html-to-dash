from black import format_str, FileMode
from lxml import etree
import dash_html_components as html

def parse_format(element):
    param_map = {
        'class': 'className'
    }
    tag = 'html.' + element.tag.capitalize()
    text = element.text.replace('\n', '').strip()
    args = ", ".join(map(lambda x: f'{param_map.get(x[0], x[0])}="{x[1]}"', element.items()))
    children = element.getchildren()

    if len(children) > 0:
        parsed_children = [parse_format(child) for child in children]
        args += f", children=[{', '.join(parsed_children)}]"
    elif text != "":
        args += f'"{text}"'

    return f"{tag}({args})"

element_str = """
  <div class="row">
    <div class="col s12 m6">
      <div class="card blue-grey darken-1">
        <div class="card-content white-text">
          <span class="card-title">Card Title</span>
          <p>I am a very simple card. I am good at containing small bits of information.
          I am convenient because I require little markup to use effectively.</p>
        </div>
        <div class="card-action">
          <a href="#">This is a link</a>
          <a href="#">This is a link</a>
        </div>
      </div>
    </div>
  </div>
"""


root = etree.fromstring(element_str)
parsed = parse_format(root)
print(format_str(parsed, mode=FileMode()))