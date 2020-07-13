'''
We give each account an ID, based on the index of it within the list of accounts:

[
["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
["John", "johnnybravo@mail.com"], # Account 1
["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
["Mary", "mary@mail.com"] # Account 3
]

Next, build an emails_accounts_map that maps an email to a list of accounts,
which can be used to track which email is linked to which account. This is
essentially our graph:

# emails_accounts_map of email to account ID
{
  "johnsmith@mail.com": [0, 2],
  "john00@mail.com": [0],
  "johnnybravo@mail.com": [1],
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}

Next, do a DFS on each account in accounts list and look up emails_accounts_map
to tell us which accounts are lineked to that particular account via common emails.

This will make sure we visit each account only once. This is a recursive
process and we should collect all the emails that we encounter along the way.

Lastly, sort the collected emails and add it to final results, along with the name.
'''


def accounts_merge(accounts):
    merged_accounts = []
    visited_accounts = [False] * len(accounts)
    emails_accounts_map = {}

    # build up the graph
    for i, account in enumerate(accounts):  # accounts
        for j in range(1, len(account)):  # emails in account
            email = account[j]
            if email not in emails_accounts_map:
                emails_accounts_map[email] = [i]
            else:
                emails_accounts_map[email].append(i)

    def dfs(i, emails):
        if visited_accounts[i] == True:
            return

        visited_accounts[i] = True

        for j in range(1, len(accounts[i])):  # emails in account
            email = accounts[i][j]
            emails.add(email)  # add email to user's set
            for associated_account in emails_accounts_map[email]:
                dfs(associated_account, emails)

    # perform DFS for accounts and add to results
    for i, account in enumerate(accounts):
        if visited_accounts[i] == True:
            continue

        name = account[0]  # name of account
        emails = set()  # set of emails that will belong to this user
        dfs(i, emails)
        merged_accounts.append([name] + sorted(emails))

    return merged_accounts


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], [
    "John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(accounts_merge(accounts))
