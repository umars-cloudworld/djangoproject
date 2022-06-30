import json


def form_error_json(form):
    errors = json.loads(form.errors.as_json())
    error = {'error': None}
    if '__all__' in errors:
        error['error'] = errors['__all__'][0]['message']
    else:
        errors_list = []
        for ket, value in errors.items():
            errors_list.append(value[0]['message'])
        error['error'] = errors_list
    print(error)
    return error
