import re

with open('include/linux/sched.h', 'r') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
in_block = False
for line in lines:
    if line.strip().startswith('#ifdef CONFIG_SYSVIPC'):
        in_block = True
    elif in_block and line.strip().startswith('#endif'):
        in_block = False
    if in_block and ('sysvsem' in line or 'sysvshm' in line):
        leading = line[:len(line) - len(line.lstrip())]
        new_lines.append(leading + '//' + line.lstrip())
    else:
        new_lines.append(line)
content = '\n'.join(new_lines)

pattern = r'(ANDROID_KABI_RESERVE\(1\);\s*\n\s*ANDROID_KABI_RESERVE\(2\);\s*\n\s*ANDROID_KABI_RESERVE\(3\);)'
replacement = (
    '#ifdef CONFIG_SYSVIPC\n'
    '\tANDROID_KABI_USE(1, struct sysv_sem sysvsem);\n'
    '\t_ANDROID_KABI_REPLACE(ANDROID_KABI_RESERVE(2); ANDROID_KABI_RESERVE(3), struct sysv_shm sysvshm);\n'
    '#else\n'
    '\tANDROID_KABI_RESERVE(1);\n'
    '\tANDROID_KABI_RESERVE(2);\n'
    '\tANDROID_KABI_RESERVE(3);\n'
    '#endif'
)
content = re.sub(pattern, replacement, content)

with open('include/linux/sched.h', 'w') as f:
    f.write(content)

print('sched.h Droidspaces 适配完成')