
def format_list_teachers(teachers):              #
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First name</th>' \
             '<th>Last name</th>' \
             '<th>birthdate</th>' \
             '<th>salary</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for tch in teachers:
        string += f'<fr>' \
                  f'<td>{tch.first_name}</td>' \
                  f'<td>{tch.last_name}</td>' \
                  f'<td>{tch.birthdate}</td>' \
                  f'<td>{tch.salary}</td>' \
                  f'<td><a href="/teachers/update/{tch.pk}/">Edit</a></td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return string