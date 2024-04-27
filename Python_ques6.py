import json

def convert_to_milligrams(input_str):
    output = {}
    items = input_str.split(', ')
    for item in items:
        key, value = item.split()
        value_num, unit = int(value[:-1]), value[-1]
        if unit == 'g':
            value_num *= 1000  # Convert grams to milligrams
        if key in output:
            output[key].append(f"{value_num} mg")
        else:
            output[key] = [f"{value_num} mg"]
    return output

input_str = "ABC 1g, XYZ 5g, ABC 20g"
output_json = convert_to_milligrams(input_str)
print(output_json)

# Flattening the output dictionary to a list of key-value pairs
output_list = [f'"{key}": "{value}"' for key, values in output_json.items() for value in values]
print(output_list)
# Joining the list elements with comma and curly braces to form a JSON-like string
output_str = "{" + ", ".join(output_list) + "}"
print(output_str)
