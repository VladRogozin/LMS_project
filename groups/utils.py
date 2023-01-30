

def format_list_groups(groups):          #
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>Group name </th>' \
             '<th> Start group</th>' \
             '<th>Text</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for grp in groups:
        string += f'<fr>' \
                  f'<td>{grp.group_name}</td>' \
                  f'<td>{grp.group_start}</td>' \
                  f'<td>{grp.group_text}</td>' \
                  f'<td><a href="/groups/update/{grp.pk}/">Edit</a></td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return string