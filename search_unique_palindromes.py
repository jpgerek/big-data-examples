from mredu import simul
import re

input_test = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non auctor quam, in tempus erat. Morbi imperdiet lorem a tempus pellentesque. Integer cursus, nibh non tristique blandit, diam lacus mollis est, at convallis risus sapien pharetra sapien. Quisque vulputate lectus orci, ac placerat metus consequat sagittis. Vestibulum cursus accumsan dui ac tincidunt. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean blandit, justo ac tincidunt porttitor, eros diam placerat dolor, vitae luctus tortor erat et tortor. Suspendisse risus libero, vulputate et consectetur nec, tristique vitae est. Praesent vulputate ipsum vel pretium ornare. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas ac est auctor, tristique dui at, auctor nunc.

Maecenas lacus libero, ornare ut ante id, bibendum viverra nunc. Nulla facilisi. Proin sollicitudin diam ac tellus dapibus gravida id ut felis. Nullam laoreet turpis pharetra ligula placerat, id lacinia risus gravida. Duis a tincidunt purus. Proin id fringilla elit. Aenean bibendum dapibus posuere. Nullam maximus ac ligula porttitor vehicula. Quisque vel posuere massa, non tristique lectus. Morbi id cursus magna.

tenet

Sed semper lectus sed orci facilisis, eu laoreet nisl semper. Mauris nec odio ac quam viverra congue et nec justo. Nullam aliquet dui risus, eu lacinia justo aliquet ut. Ut egestas nisi eget efficitur tempor. Maecenas ac pulvinar odio. Curabitur congue, justo ut vehicula mattis, erat nisi placerat velit, a lobortis ante eros eu libero. Nam sed nulla sit amet sapien tristique interdum vel nec eros. Aenean viverra justo justo, at laoreet risus pretium id. Donec et ultricies erat, ut commodo sem. Mauris et nulla sed lorem cursus dignissim euismod eu odio. Praesent posuere vulputate turpis. Sed egestas, diam cursus ornare gravida, ipsum sapien consectetur urna, a vestibulum nunc sem sed neque. Fusce aliquet commodo rutrum. Quisque iaculis convallis nisi. Pellentesque cursus luctus ligula.

Otto

Nulla eu purus ultricies, pharetra tellus in, interdum diam. Curabitur sed efficitur nisi, eget varius justo. Ut nec felis quis purus semper placerat ut sed nibh. Maecenas cursus iaculis ex vel efficitur. Quisque pretium non nunc vel imperdiet. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed malesuada ipsum purus, sit amet viverra nulla molestie vel. Morbi nec nibh non arcu molestie commodo et ut nisi. Nulla facilisi. Etiam eu augue vulputate, maximus turpis ac, vehicula ligula. Nulla interdum est vitae ultricies pretium.

summus

foooo

summus

Quisque elementum, sapien vel maximus porttitor, augue risus faucibus tellus, bibendum condimentum odio risus id odio. Cras varius vel odio at posuere. Nam lobortis sit amet eros vehicula accumsan. Sed hendrerit eleifend mauris, vel aliquet dolor ultricies at. Morbi elit est, porttitor eget orci id, vestibulum tristique lacus. Sed interdum tortor vitae aliquet semper. Duis at dictum sapien. Etiam iaculis erat sapien, ut congue mi aliquet ut. Sed diam lorem, facilisis quis est nec, elementum gravida turpis. Nulla commodo diam nec quam sodales, id euismod lacus pretium. Vivamus porttitor enim sapien, et ultrices nunc iaculis sed. Sed blandit quam in mi placerat, et vestibulum neque porta.
"""

# normalize and clean input text
data = [ (word, None) for word in re.split(r'\s+', re.sub(r'[^a-záéíóú ]', ' ', input_test.lower()).strip()) ]

def mapper(word, _):
    if len(word) == 1:
        return None
    palindrome = word[::-1]
    if word != palindrome:
        return None
    return (word, 1)
            
def reducer(word, timesList):
    if sum(timesList) != 1:
        return None
    return (word, None)


result_mapred = simul.map_red(data, mapper, reducer)

print("result_mapred:")

for item in result_mapred:
    print("\t", item)


"""
output:

result_mapred:
         ('tenet', None)
         ('otto', None)
"""
