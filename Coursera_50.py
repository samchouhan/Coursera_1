#Count_users function is responsible for counting the number of users in a given group.
def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)  # recurse
        else:
            count += 1  # count only users
    return count