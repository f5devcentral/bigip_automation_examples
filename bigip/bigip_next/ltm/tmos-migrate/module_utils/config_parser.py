def extract_ltm_policies(text):
    policies = []
    lines = text.splitlines()
    capture = False
    current_policy = []
    brace_count = 0

    for line in lines:
        if line.startswith('ltm policy'):
            capture = True
            current_policy = [line]
            brace_count = line.count('{') - line.count('}')
        elif capture:
            current_policy.append(line)
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0:
                policies.append('\n'.join(current_policy))
                capture = False

    return policies
