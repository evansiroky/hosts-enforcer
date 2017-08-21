import re

hosts_file = '/etc/hosts'

new_contents = []

with open(hosts_file, 'r') as f:
    for line in f:
        if re.search('#\s*127', line):
             new_contents.append(re.sub(r'#\s*(127.*)', r'\1', line))
        else:
            new_contents.append(line)

with open(hosts_file, 'w') as f:
    f.writelines(new_contents)
