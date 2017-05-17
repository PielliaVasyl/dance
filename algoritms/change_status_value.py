from datetime import date


def get_current_status(status, start_date=None, end_date=None):
    if status in ['PL', 'CL', 'HL']:
        if status == 'PL':
            if start_date and start_date < date.today():
                if end_date and end_date < date.today():
                    status = 'CL'
                else:
                    status = 'HL'
            if end_date and end_date < date.today():
                status = 'CL'
            elif end_date == date.today():
                status = 'HL'

        if status == 'HL':
            if start_date:
                if start_date > date.today():
                    status = 'PL'
            if end_date:
                if end_date < date.today():
                    status = 'CL'

        if status == 'CL':
            if start_date:
                if start_date < date.today():
                    if end_date:
                        if end_date >= date.today():
                            status = 'HL'
                elif start_date > date.today():
                    status = 'PL'
    return status


def change_status_value_in_values(values, field_names):
    status = values[field_names.index('status')]
    start_date = values[field_names.index('start_date')]
    end_date = values[field_names.index('end_date')]
    try:
        status = get_current_status(status, start_date, end_date)
    except:
        pass

    return values[:field_names.index('status')] + (status,) + values[field_names.index('status') + 1:]
