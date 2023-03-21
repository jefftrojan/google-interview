def most_common_email_count(emails):
    counts = {}
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        normalized_email = local + '@' + domain
        counts[normalized_email] = counts.get(normalized_email, 0) + 1
    if counts:
        return max(counts.values())
    else:
        return 0
