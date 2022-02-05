def solution(id_list, reports, k):
    reports = set(reports)
    n_reported = {user: 0 for user in id_list}
    reported_by = {user: [] for user in id_list}
    for report in reports:
        reporter, reported = report.split()
        n_reported[reported] += 1
        reported_by[reporter].append(reported)
    
    n_emails = []
    for user in id_list:
        cnt = 0
        for reported in reported_by[user]:
            if n_reported[reported] >= k:
                cnt += 1
        n_emails.append(cnt)
        
    return n_emails
            
