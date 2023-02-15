

def format_list_courses(courses):          #
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>Course name </th>' \
             '<th> Start course</th>' \
             '<th>Text</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for grp in courses:
        string += f'<fr>' \
                  f'<td>{grp.name}</td>' \
                  f'<td>{grp.course_start}</td>' \
                  f'<td>{grp.course_text}</td>' \
                  f'<td><a href="/courses/update/{grp.pk}/">Edit</a></td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return string